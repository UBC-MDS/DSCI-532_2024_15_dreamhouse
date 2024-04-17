import plotly.express as px
from src.data import state_avg_prices

def generate_us_map(data, geojson, location_field, scope='usa', hover_info=None):
    """
    Generate a US choropleth map based on the provided data.

    Args:
    data (DataFrame): Data to display on the map, with necessary columns for locations and values.
    geojson (dict): GeoJSON data for the map outlines.
    location_field (str): The DataFrame column to be used as the identifier in the geojson mapping.
    scope (str, optional): The geographic scope of the map, defaults to 'usa'.

    Returns:
    Figure: A Plotly figure object for the choropleth map.
    """
    fig = px.choropleth(
        data,
        geojson=geojson,
        locations=location_field,
        color='Price per SqFt',
        color_continuous_scale="Viridis",
        scope=scope,
        hover_data=hover_info
    )
    fig.update_geos(fitbounds="locations", visible=True)
    fig.update_layout(title_text='US Property Prices Overview', geo_scope=scope)
    fig.update_coloraxes(showscale=False)

    return fig

def generate_default_map():
    fig = px.choropleth(
        state_avg_prices,
        locations='code',
        locationmode="USA-states",
        color='Price per SqFt',
        scope='usa'
    )
    fig.update_layout(title_text='National Property Prices Overview', geo_scope='usa')

    return fig