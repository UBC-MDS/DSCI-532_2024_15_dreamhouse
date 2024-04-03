import dash
from dash import html, dcc
from dash.dependencies import Input, Output
import plotly.express as px
import pandas as pd

# Initialize the Dash application
app = dash.Dash(__name__)
server = app.server

# Load and prepare the dataset
df = pd.read_csv('../data/processed/processed_df.csv')

# App layout
app.layout = html.Div(children=[
    html.H1(children='Dreamhouse Real Estate Dashboard'),
    
    # filterss
    html.Div([
        # selection state & city 
        html.Label('State'),
        dcc.Dropdown(
            id='state-dropdown',
            options=[{'label': 'All', 'value': 'All'}] +
                    [{'label': state, 'value': state} for state in df['State'].unique()],
            value='All',
            clearable=False,
        ),
        html.Label('City'),
        dcc.Dropdown(
            id='city-dropdown',
            multi=False, #This could be an improvement? -- maybe we can Add multiple cities at once -- complicates bars
            options=[{'label': 'All', 'value': 'All'}],
            value='All',
            clearable=False,
        ),

        # living space RangeSlider
        html.Label('Square Footage'),
        dcc.RangeSlider(
            id='square-footage-slider',
            min= df['Living Space'].min(),
            max=df['Living Space'].max(),
            value=[df['Living Space'].min(), df['Living Space'].max()],
            updatemode='drag',
            tooltip={'always_visible': False, 'placement': 'top'}, 
        ),
        # price RangeSlider
        html.Label('Price Range'),
        dcc.RangeSlider(
            id='price-range-slider',
            min= df['Price'].min(),
            max=df['Price'].max(),
            value=[df['Price'].min(), df['Price'].max()],
            updatemode='drag',
            tooltip={'always_visible': False, 'placement': 'top'}, 
        ),
        # Beds & baths
        html.Label('Beds'),
        dcc.RangeSlider(
            id='beds-slider',
            min= df['Beds'].min(),
            max=df['Beds'].max(),
            value=[df['Beds'].min(), df['Beds'].max()],
            updatemode='drag',
            tooltip={'always_visible': False, 'placement': 'top'} ,
        ),
        html.Label('Baths'),
        dcc.RangeSlider(
            id='baths-slider',
            min= df['Baths'].min(),
            max=df['Baths'].max(),
            value=[df['Baths'].min(), df['Baths'].max()],
            updatemode='drag',
            tooltip={'always_visible': False, 'placement': 'top'},
        ),
    ], style={'columnCount': 2}),
    
    # graph to be colored by state
    dcc.Graph(
        id='city-bar-graph',
    ),
    
])

# state-dropdown --> updates the city-dropdown options
@app.callback(
    Output('city-dropdown', 'options'),
    Input('state-dropdown', 'value'))

def set_cities_options(selected_state):
    if selected_state == 'All':
        return [{'label': 'All', 'value': 'All'}] + [
            {'label': city, 'value': city} for city in df['City'].unique()
        ]
    else:
        return [{'label': 'All', 'value': 'All'}] + [
            {'label': city, 'value': city} for city in df[df['State'] == selected_state]['City'].unique()
        ]

# update the city bar graph
@app.callback(
    Output('city-bar-graph', 'figure'),
    Input('state-dropdown', 'value'),
    Input('city-dropdown', 'value'),
    Input('square-footage-slider', 'value'),
    Input('price-range-slider', 'value'),
    Input('beds-slider', 'value'),
    Input('baths-slider', 'value'))


def update_city_bar_graph(state, city, square_footage_range, price_range, beds, baths):
    filtered_df = df.copy()

    # State filter
    if state != 'All':
        filtered_df = filtered_df[filtered_df['State'] == state]

    # City filter
    if city != 'All':
        filtered_df = filtered_df[filtered_df['City'] == city]

    # living space
    min_sqft, max_sqft = square_footage_range
    filtered_df = filtered_df[(filtered_df['Living Space'] >= min_sqft) & (filtered_df['Living Space'] <= max_sqft)]

    # price 
    min_price, max_price = price_range
    filtered_df = filtered_df[(filtered_df['Price'] >= min_price) & (filtered_df['Price'] <= max_price)]

    # Beds & baths
    min_beds, max_beds = beds
    filtered_df = filtered_df[(filtered_df['Beds'] >= min_beds) & (filtered_df['Beds'] <= max_beds)]
    
    min_baths, max_baths = baths
    filtered_df = filtered_df[(filtered_df['Baths'] >= min_baths) & (filtered_df['Baths'] <= max_baths)]

    # when data is empty, display no data tp plot
    if not filtered_df.empty:
        city_avg_prices = filtered_df.groupby(['City', 'State'], as_index=False)['Price'].mean()

        fig = px.bar(
            city_avg_prices,
            y='City',
            x='Price',        #Missing count! Unsure if this is the only way to hover?
            color='State',
            title='Average House Pricing by City'
        )

        fig.update_layout(
            yaxis={'categoryorder': 'total descending'},
            xaxis_title='Average Price',
            yaxis_title='City',
            legend_title='State'
        )
    else:
        fig = px.bar()
        fig.update_layout(
            title='No Data Available for Selected Filters',
            xaxis={'visible': False},
            yaxis={'visible': False}
        )

    return fig

if __name__ == '__main__':
    app.run_server(debug=False)
