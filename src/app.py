import dash
from dash import html, dcc
from dash.dependencies import Input, Output
import plotly.express as px
import pandas as pd

# Initialize the Dash application
app = dash.Dash(__name__)

# Load and prepare the dataset
df = pd.read_csv('data/processed/processed_df.csv')

# Average Price (per sqft) by State
state_avg_prices = df.groupby('State')['Price per SqFt'].mean().reset_index()

# App layout
app.layout = html.Div(children=[
    html.H1(children='Dreamhouse Real Estate Dashboard'),
    
    dcc.Graph(
        id='us-map',
    ),
])

# Callback to update the heatmap
@app.callback(
    Output('us-map', 'figure'),
    Input('us-map', 'id'))
def update_map(dummy):
    fig = px.choropleth(
        state_avg_prices,
        locations='State',
        locationmode='USA-states',
        color='Price per SqFt',
        color_continuous_scale='Viridis',
        scope='usa',
        title='Average Price per SqFt by State'
    )

    # Set the size of the map
    fig.update_layout(height=750, width=900)

    # Adjust the legend position and orientation
    fig.update_layout(
        legend=dict(
            x=0.5,  # Adjust the x position as needed
            y=-0.1,  # Adjust the y position as needed
            orientation="h"
        )
    )

    return fig


# Run the Dash app
if __name__ == '__main__':
    app.run_server(debug=False)
