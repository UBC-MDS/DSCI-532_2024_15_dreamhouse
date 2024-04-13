
import plotly.express as px
from src.data import state_avg_prices
from src.data import df
from urllib.request import urlopen
import json
with urlopen('https://raw.githubusercontent.com/plotly/datasets/master/geojson-counties-fips.json') as response:
    counties = json.load(response)


def generate_us_map(selected_state=None):
    if selected_state:
        # Filter data for the selected state and generate a county-level choropleth
        filtered_df = df[df['code'] == selected_state]
        fig = px.choropleth(
            filtered_df, 
            geojson=counties, 
            locations='fips', 
            color='Price per SqFt',
            color_continuous_scale="Viridis",
            scope="usa"
        )
    else:
        # Generate the default US map showing state averages
        fig = px.choropleth(
            state_avg_prices,
            locations='code',
            locationmode="USA-states",
            color='Price per SqFt',
            scope='usa'
        )
    fig.update_layout(title_text='US Choropleth Map', geo_scope='usa')
    return fig

def generate_city_map(state_df):
    fig = px.scatter_geo(
        state_df,
        locations='fips',
        locationmode="USA-states",
        lat='Latitude',
        lon='Longitude',
        color='Price per SqFt',
        hover_name='City',
        scope='usa',
        color_continuous_scale="Viridis"
    )
    fig.update_geos(fitbounds="locations")
    fig.update_layout(
        title_text='City Details',
        geo_scope='usa'
    )
    return fig