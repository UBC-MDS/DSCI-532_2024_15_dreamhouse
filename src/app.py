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
        # First column --> filters
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
        # Second column is for --> Map, bar, and summary Stats
        dbc.Col([
            # Row for map and bar
            dbc.Row([
                dbc.Col([dbc.Label('Map')], md=6),  # Placeholder
                dbc.Col([city_bar_graph], md=6),
            ]),
            # First Row for summary statistics
            dbc.Row([
                html.Div(style={'display': 'flex', 'justify-content': 'space-between', 'width': '100%', 'padding': '20px'}, children=[
                    html.Div(id='median-price-display', style={'fontSize': '20px', 'width': '30%', 'height': '100px', 'display': 'flex', 'justify-content': 'center', 'align-items': 'center', 'background-color': '#F0F0F0', 'border-radius': '5px', 'margin': '10px', 'padding': '20px'}),
                    html.Div(id='median-price-per-sqft-display', style={'fontSize': '20px', 'width': '30%', 'height': '100px', 'display': 'flex', 'justify-content': 'center', 'align-items': 'center', 'background-color': '#F0F0F0', 'border-radius': '5px', 'margin': '10px', 'padding': '20px'}),
                    html.Div(id='average-beds-display', style={'fontSize': '20px', 'width': '30%', 'height': '100px', 'display': 'flex', 'justify-content': 'center', 'align-items': 'center', 'background-color': '#F0F0F0', 'border-radius': '5px', 'margin': '10px', 'padding': '20px'}),
                ])
            ], justify="center"),
            # Second Row for additional summary statistics
            dbc.Row([
                html.Div(style={'display': 'flex', 'justify-content': 'space-between', 'width': '100%', 'padding': '20px'}, children=[
                    # New summary boxes to be added here
                    html.Div(id='median-household-income-display', style={'fontSize': '20px', 'width': '30%', 'height': '100px', 'display': 'flex', 'justify-content': 'center', 'align-items': 'center', 'background-color': '#F0F0F0', 'border-radius': '5px', 'margin': '10px', 'padding': '20px'}),
                    html.Div(id='median-living-space', style={'fontSize': '20px', 'width': '30%', 'height': '100px', 'display': 'flex', 'justify-content': 'center', 'align-items': 'center', 'background-color': '#F0F0F0', 'border-radius': '5px', 'margin': '10px', 'padding': '20px'}),
                    html.Div(id='avg-num-baths', style={'fontSize': '20px', 'width': '30%', 'height': '100px', 'display': 'flex', 'justify-content': 'center', 'align-items': 'center', 'background-color': '#F0F0F0', 'border-radius': '5px', 'margin': '10px', 'padding': '20px'}),
                ])
            ], justify="center"),
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
        city_avg_prices = filtered_df.groupby(['City', 'State'], as_index=False)['Price'].agg(['mean', 'count'])
        fig = px.bar(
            city_avg_prices,
            y='City',
            x='mean',
            color='State',
            title='Average House Pricing by City',
            hover_data={'mean': True, 'count': True}, 
            labels={'mean': 'Average Price', 'City': 'City', 'State': 'State', 'count': 'Count'}
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
    return f"Median Household Income: ${median_income:.2f}"


@app.callback(
    Output('median-living-space', 'children'),
    [Input('state-dropdown', 'value'),
     Input('city-dropdown', 'value'),
     Input('square-footage-slider', 'value'),
     Input('price-range-slider', 'value'),
     Input('beds-slider', 'value'),
     Input('baths-slider', 'value')]
)
def update_median_square_footage(state, city, square_footage_range, price_range, beds, baths):
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
    median_square_footage = filtered_df['Living Space'].median()
    
    # Return the formatted median value for display
    return f"Median Living Space: {median_square_footage:.2f} SqFt"


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
    return f"Average Number of Baths: {avg_num_baths:.2f}"

if __name__ == '__main__':
    app.run_server(debug=False)
