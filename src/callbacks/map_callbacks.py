from dash.dependencies import Input, Output
import dash
from src.figures import generate_us_map, generate_default_map
from src.data import df, state_abbreviations
from urllib.request import urlopen
import json

# Load the GeoJSON data for counties once to avoid repeated loading
with urlopen('https://raw.githubusercontent.com/plotly/datasets/master/geojson-counties-fips.json') as response:
    counties = json.load(response)

state_mapping = {abbrev: name for name, abbrev in state_abbreviations.items()}

def register_map_callbacks(app):
    @app.callback(
        Output('usa-map', 'figure'),
        [Input('state-dropdown', 'value'),
         Input('city-dropdown', 'value'),
         Input('square-footage-slider', 'value'),
         Input('price-range-slider', 'value'),
         Input('ppsf-range-slider', 'value'),
         Input('hi-range-slider', 'value'),
         Input('beds-min-input', 'value'),
         Input('beds-max-input', 'value'),
         Input('baths-min-input', 'value'),
         Input('baths-max-input', 'value')],
        prevent_initial_call=True)
    def update_usa_map(state, city, square_footage_range, price_range, ppsf_range, household_income_range, beds_min, beds_max, baths_min, baths_max):
        
        filtered_df = df.copy()

        min_sqft, max_sqft = square_footage_range
        filtered_df = filtered_df[(filtered_df['Living Space'] >= min_sqft) & (filtered_df['Living Space'] <= max_sqft)]
        
        min_price, max_price = price_range
        filtered_df = filtered_df[(filtered_df['Price'] >= min_price) & (filtered_df['Price'] <= max_price)]
        
        min_ppsf, max_ppsf = ppsf_range
        filtered_df = filtered_df[(filtered_df['Price per SqFt'] >= min_ppsf) & (filtered_df['Price per SqFt'] <= max_ppsf)]
        
        min_hi, max_hi = household_income_range
        filtered_df = filtered_df[(filtered_df['Median Household Income'] >= min_hi) & (filtered_df['Median Household Income'] <= max_hi)]
        
        filtered_df = filtered_df[(filtered_df['Beds'] >= beds_min) & (filtered_df['Beds'] <= beds_max)]
        
        filtered_df = filtered_df[(filtered_df['Baths'] >= baths_min) & (filtered_df['Baths'] <= baths_max)]

        if state and state != 'All':
            filtered_df = filtered_df[filtered_df['State'] == state]
            if city != 'All':
                filtered_df = filtered_df[filtered_df['City'] == city]
            geojson_data = counties
            location_field = 'fips_str'
            return generate_us_map(filtered_df, geojson_data, location_field, hover_info=['County', 'City'])
        else:
            # Call a function to generate the default map (e.g., national overview)
            return generate_default_map()

    @app.callback(
    Output('state-dropdown', 'value'),
    [Input('usa-map', 'clickData')],
    prevent_initial_call=True)
    def select_state_on_map_click(clickData):
        if clickData is not None:
            clicked_state_abbr = clickData['points'][0]['location']
            clicked_state_full = state_mapping.get(clicked_state_abbr)
            if clicked_state_full:
                return clicked_state_full
        raise dash.exceptions.PreventUpdate
