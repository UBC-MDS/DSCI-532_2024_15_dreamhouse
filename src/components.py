from dash import html, dcc
import dash_bootstrap_components as dbc
from src.data import df

# Graph components
graphs = html.Div([
    dcc.Graph(id='city-bar-graph', style={'height': '560px'}),
    dcc.Graph(id='usa-map')
])



title = dbc.Row(
    [dbc.Col(
        [
            html.Div(  # Create a div that wraps both H1 and H2 with the desired background
                [
                    html.H1('🏡 Dreamhouse 🏡', 
                            className='text-center', 
                            style={'fontSize': '60px', 'font-family': "'Arial Black', Gadget, sans-serif"}
                           ),
                    html.H2('A Real Estate Dashboard of the 50 Largest Cities in the United States', 
                            className='text-center', 
                            style={'fontSize': '24px', 'marginTop': '20px', 'color': 'grey'}
                           )
                ],
                style={'display': 'flex', 'flex-direction': 'column', 'justify-content': 'center', 'align-items': 'center', 'background-color': '#ADD8E6', 'border-radius': '5px', 'margin': '5px 0 5px 0', 'padding': '5px', 'width': '100%'}
            )
        ],
        width=12
    )],
    justify="center"
)

dropdown_box = html.Div(
    [   # Enclosing both dropdown labels in a single div
        html.Label(
            ["State", 
             dcc.Dropdown(
                 id='state-dropdown',
                 options=[{'label': 'All', 'value': 'All'}] + [{'label': state, 'value': state} for state in df['State'].unique()],
                 value='All',
                 clearable=False,
                 style={'width': '100%', 'min-width': '200px'}
             ),
             html.Br()
            ]
        ),
        html.Label(
            ["City", 
             dcc.Dropdown(
                 id='city-dropdown',
                 options=[{'label': 'All', 'value': 'All'}],
                 value='All',
                 clearable=False,
                 style={'width': '100%', 'min-width': '200px'}
             ),
             html.Br()
            ]
        )
    ],
    style={
        'background-color': '#ADD8E6',  # Light blue background fills the box
        'padding': '10px',  # Provides padding inside the box
        'margin': '5px 0 5px 11px',  # Centers the box with some space around
        'display': 'flex',
        'flex-direction': 'column',  # Stack the dropdowns vertically
        'align-items': 'center',  # Center align the dropdown contents
        'width': '300px',  # Fixed width for the container
        'box-shadow': '0 4px 8px rgba(0, 0, 0, 0.05)',  # Optional: adds a subtle shadow for depth
        'border-radius': '5px'
    }
)

slider_wrapper_style = {'width': '100%', 'margin': '20px auto'}

controls_box = html.Div(
    [
        html.Div(
            [
                html.Label("Square Footage"),
                dcc.RangeSlider(
                    id='square-footage-slider',
                    min=df['Living Space'].min(),
                    max=df['Living Space'].max(),
                    value=[df['Living Space'].min(), df['Living Space'].max()],
                    tooltip={'placement': 'bottom', 'always_visible': False}
                ),
            ],
            style=slider_wrapper_style
        ),
        html.Div(
            [
                html.Label("Price Range"),
                dcc.RangeSlider(
                    id='price-range-slider',
                    min=df['Price'].min(),
                    max=df['Price'].max(),
                    value=[df['Price'].min(), df['Price'].max()],
                    tooltip={'placement': 'bottom', 'always_visible': False}
                ),
            ],
            style=slider_wrapper_style
        ),
        html.Div(
            [
                html.Label("Price per Square Footage"),
                dcc.RangeSlider(
                    id='ppsf-range-slider',
                    min=round(df['Price per SqFt'].min(), 3),
                    max=df['Price per SqFt'].max(),
                    value=[round(df['Price per SqFt'].min(), 3), df['Price per SqFt'].max()],
                    tooltip={'placement': 'bottom', 'always_visible': False}
                ),
            ],
            style=slider_wrapper_style
        ),
        html.Div(
            [
                html.Label("Median Household Income"),
                dcc.RangeSlider(
                    id='hi-range-slider',
                    min=df['Median Household Income'].min(),
                    max=df['Median Household Income'].max(),
                    value=[df['Median Household Income'].min(), df['Median Household Income'].max()],
                    step=90000,
                    tooltip={'placement': 'bottom', 'always_visible': False}
                ),
            ],
            style=slider_wrapper_style
        ),
        html.Div(
            [
                html.Label(
                    [
                        "Beds",
                        html.Div(
                            [
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
                            ],
                            style={'padding': '10px 0'}
                        )
                    ]
                ),
                html.Br()
            ],
            style=slider_wrapper_style
        ),
        html.Div(
            [
                html.Label(
                    [
                        "Baths",
                        html.Div(
                            [
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
                            ],
                            style={'padding': '10px 0'}
                        )
                    ]
                ),
                html.Br()
            ],
            style=slider_wrapper_style
        ),
        dbc.Button("Reset Custom Filters", id="clear-button", color="secondary", size="lg", className="me-1", style={'width': '90%', 'margin': '10px auto'}),
        dbc.Button('Apply Inputs', id='filter-button', n_clicks=0, size="sm", color="info", className="me-1", style={"width": "90%", "margin": "10px auto", "color": "white"}),
        html.Div(id='beds-last-update', style={'display': 'none'}),
        html.Div(id='baths-last-update', style={'display': 'none'}),
    ],
    style={
        'background-color': '#ADD8E6',  # Light blue background
        'border-radius': '5px',  # Rounded corners
        'padding': '10px',  # Padding inside the box
        'margin': '5px 0 5px 11px',  # Margin around the box
        'display': 'flex',
        'flex-direction': 'column',
        'align-items': 'center',
        'width': '100%',  # Width set to 100% of the parent container
        'box-sizing': 'border-box',  # Include padding and border in the width and height totals
    }
)

city_bar_graph = dcc.Graph(id='city-bar-graph', style={'height': '560px'})
usa_main_map = dcc.Graph(id='usa-map', style={'height': '560px'})
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
