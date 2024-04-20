import plotly.express as px
from src.data import state_avg_prices


def generate_us_map(data, geojson, location_field, color_scale_max, scope='usa', hover_info=None):
    """
    Generate a US choropleth map based on the provided data.
    
    Args:
        data (DataFrame): Data to display on the map, with necessary columns for locations and values.
        geojson (dict): GeoJSON data for the map outlines.
        location_field (str): The DataFrame column to be used as the identifier in the geojson mapping.
        color_scale_max (float): Maximum value for the color scale.
        scope (str, optional): The geographic scope of the map, defaults to 'usa'.
        hover_info (list, optional): Additional info to show on hover.
        
    Returns:
        Figure: A Plotly figure object for the choropleth map.
    """
    fig = px.choropleth(
        data,
        geojson=geojson,
        locations=location_field,
        color='Price',
        color_continuous_scale="Viridis",
        range_color=(data['Price'].min(), color_scale_max),  # Set the color scale range
        scope=scope,
        hover_data=hover_info
    )
    fig.update_geos(fitbounds="locations", visible=True)
    fig.update_layout(title_text='County Level Price Heatmap', geo_scope=scope, coloraxis=dict(colorbar=dict(orientation='h', y=-0.5)))
    fig.update_coloraxes(showscale=True)  # Make sure the color scale is visible

    return fig

def generate_default_map():
    fig = px.choropleth(
        state_avg_prices,
        locations='code',
        locationmode="USA-states",
        color='Price',
        color_continuous_scale="Plasma",
        scope='usa'
    )
    fig.update_layout(
    title_text='National Median Property Prices Heatmap', geo_scope='usa', coloraxis=dict(colorbar=dict(orientation='h', y=-0.5))
    )
    #fig.update_coloraxes(showscale=False)

    return fig