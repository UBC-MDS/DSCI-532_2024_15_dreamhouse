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

price_per_square_footage_range_slider = dcc.RangeSlider(
    id='ppsf-range-slider',
    min=round(df['Price per SqFt'].min(),3),
    max=df['Price per SqFt'].max(),
    value=[round(df['Price per SqFt'].min(),3), df['Price per SqFt'].max()],
    tooltip={'placement': 'bottom', 'always_visible': False}
)

home_income_range_slider = dcc.RangeSlider(
    id='hi-range-slider',
    min=df['Median Household Income'].min(),
    max=df['Median Household Income'].max(),
    value=[df['Median Household Income'].min(), df['Median Household Income'].max()],
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
            dbc.Label('Price per Square Footage'),
            price_per_square_footage_range_slider, 
            html.Br(),
            dbc.Label('Median Household Income'),
            home_income_range_slider,
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
                    dbc.Row([ # the other J's Row --> whos is which tbd
                        dbc.Col([
                            dbc.Label('Stat4')  #Placeholder
                         ], md=3),
                        dbc.Col([
                            dbc.Label('Stat5')  #Placeholder
                         ], md=3),
                        dbc.Col([
                            dbc.Label('Stat6')  #Placeholder
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
     Input('ppsf-range-slider', 'value'),
     Input('hi-range-slider', 'value'),
     Input('beds-slider', 'value'),
     Input('baths-slider', 'value')])
def update_city_bar_graph(state, city, square_footage_range, price_range, ppsf_range, household_income_range, beds, baths):
    filtered_df = df.copy()
    
    if state != 'All':
        filtered_df = filtered_df[filtered_df['State'] == state]
    
    if city != 'All':
        filtered_df = filtered_df[filtered_df['City'] == city]
    
    min_sqft, max_sqft = square_footage_range
    filtered_df = filtered_df[(filtered_df['Living Space'] >= min_sqft) & (filtered_df['Living Space'] <= max_sqft)]
    
    min_price, max_price = price_range
    filtered_df = filtered_df[(filtered_df['Price'] >= min_price) & (filtered_df['Price'] <= max_price)]
    
    min_ppsf, max_ppsf = ppsf_range
    filtered_df = filtered_df[(filtered_df['Price per SqFt'] >= min_ppsf) & (filtered_df['Price per SqFt'] <= max_ppsf)]
    
    min_hi, max_hi = household_income_range
    filtered_df = filtered_df[(filtered_df['Median Household Income'] >= min_hi) & (filtered_df['Median Household Income'] <= max_hi)]
    
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

if __name__ == '__main__':
    app.run_server(debug=False)
