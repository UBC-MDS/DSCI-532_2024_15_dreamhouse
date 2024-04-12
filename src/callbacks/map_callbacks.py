import dash
from dash.dependencies import Input, Output
import plotly.express as px
from figures import generate_us_map
from data import df, state_mapping

def register_map_callbacks(app):
    @app.callback(
        Output('usa-map', 'figure'),
        [Input('state-dropdown', 'value'),
        Input('city-dropdown', 'value')])
    def update_map(selected_state, selected_city):
        if selected_state != 'All' and selected_state is not None:
            # Filter dataframe for selected state
            state_df = df[df['State'] == selected_state]
            # Generate choropleth map for selected state
            fig = px.choropleth(
                state_df,
                locations='code',
                locationmode="USA-states",
                color='Price per SqFt',
                scope='usa'
            )
            fig.update_geos(fitbounds="locations")
        else:
            # Display the entire US map
            fig = generate_us_map()
        return fig
    
    # Mouse clicking feature
    # Clicking a state on the main map will make a choice at the state-dropdown window
    @app.callback(
        Output('state-dropdown', 'value'),
        [Input('usa-map', 'clickData')]
    )
    def select_state_on_map_click(clickData):
        if clickData is not None:
            clicked_state_abbr = clickData['points'][0]['location']
            clicked_state_full = state_mapping.get(clicked_state_abbr, None)
            if clicked_state_full:
                return clicked_state_full
        raise dash.exceptions.PreventUpdate