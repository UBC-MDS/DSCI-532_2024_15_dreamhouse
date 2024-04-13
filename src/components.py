from dash import html, dcc
import dash_bootstrap_components as dbc
from data import df

# Graph components
graphs = html.Div([
    dcc.Graph(id='city-bar-graph', style={'height': '560px'}),
    dcc.Graph(id='usa-map')
])


title = dbc.Row([dbc.Col(html.H1('Dreamhouse Real Estate Dashboard'), width=12, style={'fontSize': '20px', 'width': '30%', 'height': '100px', 'display': 'flex', 'justify-content': 'center', 'align-items': 'center'})])

state_dropdown = html.Label([
    "State",
    dcc.Dropdown(
    id='state-dropdown',
    options=[{'label': 'All', 'value': 'All'}] + [{'label': state, 'value': state} for state in df['State'].unique()],
    value='All',
    clearable=False
    ),
    html.Br()
])

city_dropdown = html.Label([
    "City",
    dcc.Dropdown(
    id='city-dropdown',
    options=[{'label': 'All', 'value': 'All'}],
    value='All',
    clearable=False,
    ),
    html.Br()
])

square_footage_slider =  html.Label([
    "Square Footage",
    dcc.RangeSlider(
    id='square-footage-slider',
    min=df['Living Space'].min(),
    max=df['Living Space'].max(),
    value=[df['Living Space'].min(), df['Living Space'].max()],
    tooltip={'placement': 'bottom', 'always_visible': False}),
    html.Br()
])

price_range_slider =  html.Label([
    "Price Range",
    dcc.RangeSlider(
    id='price-range-slider',
    min=df['Price'].min(),
    max=df['Price'].max(),
    value=[df['Price'].min(), df['Price'].max()],
    tooltip={'placement': 'bottom', 'always_visible': False}),
    html.Br()
])

price_per_square_footage_range_slider =  html.Label([
    "Price per Square Footage",
    dcc.RangeSlider(
    id='ppsf-range-slider',
    min=round(df['Price per SqFt'].min(),3),
    max=df['Price per SqFt'].max(),
    value=[round(df['Price per SqFt'].min(),3), df['Price per SqFt'].max()],
    tooltip={'placement': 'bottom', 'always_visible': False}),
    html.Br()
])

home_income_range_slider =  html.Label([
    "Median Household Income",
    dcc.RangeSlider(
    id='hi-range-slider',
    min=df['Median Household Income'].min(),
    max=df['Median Household Income'].max(),
    value=[df['Median Household Income'].min(), df['Median Household Income'].max()],
    step=90000,
    tooltip={'placement': 'bottom', 'always_visible': False}),
    html.Br()
])

beds_input =  html.Label([
    "Beds",
    html.Div([
        dcc.Input(
            type='number',
            id='beds-min-input',
            value=df['Beds'].min(),
            min=df['Beds'].min(),
            max=df['Beds'].max(),
            placeholder='Min',
            style={'width': '49%', 'display': 'inline-block'}
        ),
        dcc.Input(
            type='number',
            id='beds-max-input',
            value=df['Beds'].max(),
            min=df['Beds'].min(),
            max=df['Beds'].max(),
            placeholder='Max',
            style={'width': '49%', 'display': 'inline-block', 'float': 'right'}
        )
    ], style={'padding': '10px 0'}), 
    html.Br()
])


baths_input=  html.Label([
    "Baths",
    html.Div([
        dcc.Input(
            type='number',
            id='baths-min-input',
            value=df['Baths'].min(),
            min=df['Baths'].min(),
            max=df['Baths'].max(),
            placeholder='Min',
            style={'width': '49%', 'display': 'inline-block'}
        ),
        dcc.Input(
            type='number',
            id='baths-max-input',
            value=df['Baths'].max(),
            min=df['Baths'].min(),
            max=df['Baths'].max(),
            placeholder='Max',
            style={'width': '49%', 'display': 'inline-block', 'float': 'right'}
        )
    ], style={'padding': '10px 0'}),
    html.Br()
])

clear_all_button = dbc.Button("Reset", id="clear-button", className="mb-3", color="secondary")

city_bar_graph = dcc.Graph(id='city-bar-graph', style={'height': '560px'})
usa_main_map = dcc.Graph(id='usa-map')
state_avg_prices = df.groupby('code')['Price per SqFt'].mean().reset_index()

# summary statistics
##
summary_stats_first_row = dbc.Row([
    html.Div(style={'display': 'flex', 'justify-content': 'space-between', 'width': '100%', 'padding': '20px'}, children=[
        html.Div(id='median-price-display', style={'fontSize': '20px', 'width': '30%', 'height': '100px', 'display': 'flex', 'justify-content': 'center', 'align-items': 'center', 'background-color': '#F0F0F0', 'border-radius': '5px', 'margin': '10px', 'padding': '20px'}),
        html.Div(id='median-price-per-sqft-display', style={'fontSize': '20px', 'width': '30%', 'height': '100px', 'display': 'flex', 'justify-content': 'center', 'align-items': 'center', 'background-color': '#F0F0F0', 'border-radius': '5px', 'margin': '10px', 'padding': '20px'}),
        html.Div(id='average-beds-display', style={'fontSize': '20px', 'width': '30%', 'height': '100px', 'display': 'flex', 'justify-content': 'center', 'align-items': 'center', 'background-color': '#F0F0F0', 'border-radius': '5px', 'margin': '10px', 'padding': '20px'}),
    ])
])

summary_stats_second_row = dbc.Row([
    html.Div(style={'display': 'flex', 'justify-content': 'space-between', 'width': '100%', 'padding': '20px'}, children=[
        html.Div(id='median-household-income-display', style={'fontSize': '20px', 'width': '30%', 'height': '100px', 'display': 'flex', 'justify-content': 'center', 'align-items': 'center', 'background-color': '#F0F0F0', 'border-radius': '5px', 'margin': '10px', 'padding': '20px'}),
        html.Div(id='median-living-space', style={'fontSize': '20px', 'width': '30%', 'height': '100px', 'display': 'flex', 'justify-content': 'center', 'align-items': 'center', 'background-color': '#F0F0F0', 'border-radius': '5px', 'margin': '10px', 'padding': '20px'}),
        html.Div(id='avg-num-baths', style={'fontSize': '20px', 'width': '30%', 'height': '100px', 'display': 'flex', 'justify-content': 'center', 'align-items': 'center', 'background-color': '#F0F0F0', 'border-radius': '5px', 'margin': '10px', 'padding': '20px'}),
    ])
])