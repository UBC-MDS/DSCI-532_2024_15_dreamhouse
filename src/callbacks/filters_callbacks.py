
from dash.dependencies import Input, Output
from src.data import df

def register_filter_callbacks(app):
    @app.callback(
        Output('city-dropdown', 'options'),
        Output('city-dropdown', 'value'),
        Input('state-dropdown', 'value'))
    def set_cities_options(selected_state):
        if selected_state == 'All':
            return [{'label': 'All', 'value': 'All'}] + [{'label': city, 'value': city} for city in df['City'].unique()], 'All'
        else:
            cities_in_state = df[df['State'] == selected_state]['City'].unique()
            return [{'label': 'All', 'value': 'All'}] + [{'label': city, 'value': city} for city in cities_in_state], 'All'



#@app.callback(
#    [Output('state-dropdown', 'value'),
#     Output('city-dropdown', 'value'),
#     Output('square-footage-slider', 'value'),
#     Output('price-range-slider', 'value'),
#     Output('ppsf-range-slider', 'value'),
#     Output('hi-range-slider', 'value'),
#     Output('beds-min-input', 'value'),
#     Output('beds-max-input', 'value'),
#     Output('baths-min-input', 'value'),
#     Output('baths-max-input', 'value')],
#    [Input('clear-button', 'n_clicks')],
#    prevent_initial_call=True
#)
#def reset_all_filters(n_clicks):
#    if n_clicks is None or n_clicks < 1:
#        raise PreventUpdate
#    return ('All', 'All',
#            [df['Living Space'].min(), df['Living Space'].max()],
#            [df['Price'].min(), df['Price'].max()],
#            [round(df['Price per SqFt'].min(), 3), df['Price per SqFt'].max()],
#            [df['Median Household Income'].min(), df['Median Household Income'].max()],
#            df['Beds'].min(), df['Beds'].max(),
#            df['Baths'].min(), df['Baths'].max())