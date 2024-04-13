
import plotly.express as px
from data import state_avg_prices

def generate_us_map():
    fig = px.choropleth(
        state_avg_prices,
        locations='code',
        locationmode="USA-states",
        color='Price per SqFt',
        scope='usa'
    )
    fig.update_layout(title_text='US Choropleth Map', geo_scope='usa')
    return fig