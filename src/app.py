import dash
from dash import html, dcc
import dash_bootstrap_components as dbc
from dash.dependencies import Input, Output
import plotly.express as px
import pandas as pd

# Initialize the Dash application
app = dash.Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])
server = app.server

df = pd.read_csv('data/processed/processed_df.csv')  

title = dbc.Row([dbc.Col(html.H1('Dreamhouse Real Estate Dashboard'), width=12)])

state_dropdown = dcc.Dropdown(
    id='state-dropdown',
    options=[{'label': 'All', 'value': 'All'}] + [{'label': state, 'value': state} for state in df['State'].unique()],
    value='All',
    clearable=False
)

city_dropdown = dcc.Dropdown(
    id='city-dropdown',
    options=[{'label': 'All', 'value': 'All'}],
    value='All',
    clearable=False,
)

square_footage_slider = dcc.RangeSlider(
    id='square-footage-slider',
    min=df['Living Space'].min(),
    max=df['Living Space'].max(),
    value=[df['Living Space'].min(), df['Living Space'].max()],
    tooltip={'placement': 'bottom', 'always_visible': False}
)

price_range_slider = dcc.RangeSlider(
    id='price-range-slider',
    min=df['Price'].min(),
    max=df['Price'].max(),
    value=[df['Price'].min(), df['Price'].max()],
    tooltip={'placement': 'bottom', 'always_visible': False}
)

beds_slider = dcc.RangeSlider(
    id='beds-slider',
    min=df['Beds'].min(),
    max=df['Beds'].max(),
    value=[df['Beds'].min(), df['Beds'].max()],
    tooltip={'placement': 'bottom', 'always_visible': False}
)

baths_slider = dcc.RangeSlider(
    id='baths-slider',
    min=df['Baths'].min(),
    max=df['Baths'].max(),
    value=[df['Baths'].min(), df['Baths'].max()],
    tooltip={'placement': 'bottom', 'always_visible': False}
)

city_bar_graph = dcc.Graph(id='city-bar-graph')



app.layout = dbc.Container([
title,
    
    # Main Row
    dbc.Row([
        # first column --> filters
        dbc.Col([
            dbc.Label('State'),
            state_dropdown, 
            html.Br(),
            dbc.Label('City'),
            city_dropdown,  
            html.Br(),
            dbc.Label('Square Footage'),
            square_footage_slider, 
            html.Br(),
            dbc.Label('Price Range'),
            price_range_slider, 
            html.Br(),
            dbc.Label('Beds'),
            beds_slider, 
            html.Br(),
            dbc.Label('Baths'),
            baths_slider, 
        ], md=2),

        # Second column is for -->  Map, bar, and summary Stats
        dbc.Col([
            # Row for map and bar
            dbc.Row([
                dbc.Col([
                    dbc.Label('Map')  #Placeholder
                ], md=6),
                dbc.Col([
                    city_bar_graph 
                ], md=6),
            ]),
            
            # row for summary statistics -- this row could have two rows and 3 columns inside? --> this depends on how many summary stats we end up with
            dbc.Row([
                dbc.Col([
                    dbc.Label('Summary statistics'),  #placeholder
                    dbc.Row([ # J's Row
                        dbc.Col([
                            dbc.Label('Stat1')  #Placeholder
                         ], md=3),
                        dbc.Col([
                            dbc.Label('Stat2')  #Placeholder
                         ], md=3),
                        dbc.Col([
                            dbc.Label('Stat3')  #Placeholder
                         ], md=3),
                    ]),
                    dbc.Row([ # Jake's row (values)(will put the values in this row and the labels below)
                        dbc.Col([
                            dbc.Label(id='median-household-income-display'),
                            html.Br(),
                            dbc.Label('Median Household Income')
                         ], md=3),
                        dbc.Col([
                            dbc.Label(id='price-per-square-foot'),
                            html.Br(),
                            dbc.Label('Price per square foot')  #Placeholder
                         ], md=3),
                        dbc.Col([
                            dbc.Label(id='avg-num-baths'),
                            html.Br(),
                            dbc.Label('Average Number of Baths')  #Placeholder
                         ], md=3),
                    ]),
                ])
            ])
        ], md=10),
    ])
], fluid=True)


@app.callback(
    Output('city-dropdown', 'options'),
    Input('state-dropdown', 'value'))
def set_cities_options(selected_state):
    if selected_state == 'All':
        return [{'label': 'All', 'value': 'All'}] + [{'label': city, 'value': city} for city in df['City'].unique()]
    else:
        return [{'label': 'All', 'value': 'All'}] + [{'label': city, 'value': city} for city in df[df['State'] == selected_state]['City'].unique()]


@app.callback(
    Output('city-bar-graph', 'figure'),
    [Input('state-dropdown', 'value'),
     Input('city-dropdown', 'value'),
     Input('square-footage-slider', 'value'),
     Input('price-range-slider', 'value'),
     Input('beds-slider', 'value'),
     Input('baths-slider', 'value')])
def update_city_bar_graph(state, city, square_footage_range, price_range, beds, baths):
    filtered_df = df.copy()
    
    if state != 'All':
        filtered_df = filtered_df[filtered_df['State'] == state]
    
    if city != 'All':
        filtered_df = filtered_df[filtered_df['City'] == city]
    
    min_sqft, max_sqft = square_footage_range
    filtered_df = filtered_df[(filtered_df['Living Space'] >= min_sqft) & (filtered_df['Living Space'] <= max_sqft)]
    
    min_price, max_price = price_range
    filtered_df = filtered_df[(filtered_df['Price'] >= min_price) & (filtered_df['Price'] <= max_price)]
    
    min_beds, max_beds = beds
    filtered_df = filtered_df[(filtered_df['Beds'] >= min_beds) & (filtered_df['Beds'] <= max_beds)]
    
    min_baths, max_baths = baths
    filtered_df = filtered_df[(filtered_df['Baths'] >= min_baths) & (filtered_df['Baths'] <= max_baths)]
    
    if not filtered_df.empty:
        city_avg_prices = filtered_df.groupby(['City', 'State'], as_index=False)['Price'].mean()
        fig = px.bar(
            city_avg_prices,
            y='City',
            x='Price',
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


@app.callback(
    Output('median-household-income-display', 'children'),
    [Input('state-dropdown', 'value'),
     Input('city-dropdown', 'value'),
     Input('square-footage-slider', 'value'),
     Input('price-range-slider', 'value'),
     Input('beds-slider', 'value'),
     Input('baths-slider', 'value')]
)
def update_median_income_display(state, city, square_footage_range, price_range, beds, baths):
    # Filter the DataFrame based on the inputs (similar to the bar graph update function)
    filtered_df = df.copy()
    
    if state != 'All':
        filtered_df = filtered_df[filtered_df['State'] == state]
    
    if city != 'All':
        filtered_df = filtered_df[filtered_df['City'] == city]
    
    min_sqft, max_sqft = square_footage_range
    filtered_df = filtered_df[(filtered_df['Living Space'] >= min_sqft) & (filtered_df['Living Space'] <= max_sqft)]
    
    min_price, max_price = price_range
    filtered_df = filtered_df[(filtered_df['Price'] >= min_price) & (filtered_df['Price'] <= max_price)]
    
    min_beds, max_beds = beds
    filtered_df = filtered_df[(filtered_df['Beds'] >= min_beds) & (filtered_df['Beds'] <= max_beds)]
    
    min_baths, max_baths = baths
    filtered_df = filtered_df[(filtered_df['Baths'] >= min_baths) & (filtered_df['Baths'] <= max_baths)]
    
    # Compute the median of the "Median Household Income" column for the filtered DataFrame
    median_income = filtered_df['Median Household Income'].median()
    
    # Return the formatted median value for display
    return f"{median_income:.2f}"


@app.callback(
    Output('price-per-square-foot', 'children'),
    [Input('state-dropdown', 'value'),
     Input('city-dropdown', 'value'),
     Input('square-footage-slider', 'value'),
     Input('price-range-slider', 'value'),
     Input('beds-slider', 'value'),
     Input('baths-slider', 'value')]
)
def update_price_per_square_foot(state, city, square_footage_range, price_range, beds, baths):
    # Filter the DataFrame based on the inputs (similar to the bar graph update function)
    filtered_df = df.copy()
    
    if state != 'All':
        filtered_df = filtered_df[filtered_df['State'] == state]
    
    if city != 'All':
        filtered_df = filtered_df[filtered_df['City'] == city]
    
    min_sqft, max_sqft = square_footage_range
    filtered_df = filtered_df[(filtered_df['Living Space'] >= min_sqft) & (filtered_df['Living Space'] <= max_sqft)]
    
    min_price, max_price = price_range
    filtered_df = filtered_df[(filtered_df['Price'] >= min_price) & (filtered_df['Price'] <= max_price)]
    
    min_beds, max_beds = beds
    filtered_df = filtered_df[(filtered_df['Beds'] >= min_beds) & (filtered_df['Beds'] <= max_beds)]
    
    min_baths, max_baths = baths
    filtered_df = filtered_df[(filtered_df['Baths'] >= min_baths) & (filtered_df['Baths'] <= max_baths)]
    
    # Compute the median of the "Median Household Income" column for the filtered DataFrame
    price_per_square_foot = filtered_df['Price per SqFt'].mean()
    
    # Return the formatted median value for display
    return f"{price_per_square_foot:.2f}"


@app.callback(
    Output('avg-num-baths', 'children'),
    [Input('state-dropdown', 'value'),
     Input('city-dropdown', 'value'),
     Input('square-footage-slider', 'value'),
     Input('price-range-slider', 'value'),
     Input('beds-slider', 'value'),
     Input('baths-slider', 'value')]
)
def update_avg_num_baths(state, city, square_footage_range, price_range, beds, baths):
    # Filter the DataFrame based on the inputs (similar to the bar graph update function)
    filtered_df = df.copy()
    
    if state != 'All':
        filtered_df = filtered_df[filtered_df['State'] == state]
    
    if city != 'All':
        filtered_df = filtered_df[filtered_df['City'] == city]
    
    min_sqft, max_sqft = square_footage_range
    filtered_df = filtered_df[(filtered_df['Living Space'] >= min_sqft) & (filtered_df['Living Space'] <= max_sqft)]
    
    min_price, max_price = price_range
    filtered_df = filtered_df[(filtered_df['Price'] >= min_price) & (filtered_df['Price'] <= max_price)]
    
    min_beds, max_beds = beds
    filtered_df = filtered_df[(filtered_df['Beds'] >= min_beds) & (filtered_df['Beds'] <= max_beds)]
    
    min_baths, max_baths = baths
    filtered_df = filtered_df[(filtered_df['Baths'] >= min_baths) & (filtered_df['Baths'] <= max_baths)]
    
    # Compute the median of the "Median Household Income" column for the filtered DataFrame
    avg_num_baths = filtered_df['Baths'].mean()
    
    # Return the formatted median value for display
    return f"{avg_num_baths:.2f}"

if __name__ == '__main__':
    app.run_server(debug=False)
