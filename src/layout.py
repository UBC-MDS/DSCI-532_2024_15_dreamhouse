from dash import html, dcc
import dash_bootstrap_components as dbc
from components import title, state_dropdown, city_dropdown, square_footage_slider, price_range_slider, price_per_square_footage_range_slider, home_income_range_slider, beds_input, baths_input, clear_all_button, usa_main_map, city_bar_graph

def layout():
    return dbc.Container([
        title,
        # Main Row
        dbc.Row([
            # First column --> filters
            dbc.Col([
                dbc.Row([state_dropdown]),
                dbc.Row([city_dropdown]),
                dbc.Row([square_footage_slider]),
                dbc.Row([price_range_slider]),
                dbc.Row([price_per_square_footage_range_slider]),
                dbc.Row([home_income_range_slider]),
                dbc.Row([beds_input]),
                dbc.Row([baths_input]),
                dbc.Row([clear_all_button])
            ], md=2),
            # Second column is for --> Map, bar, and summary Stats
            dbc.Col([
                # Row for map and bar
                dbc.Row([
                    dbc.Col([
                        usa_main_map
                    ], md=6),
                    dbc.Col([
                        city_bar_graph 
                    ], md=6),
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
        ]),
        html.Div([
            html.P([
                "This dashboard was made by Group 15 of MDS DSCI 532",
                html.A(" Link to Github source", href="https://github.com/UBC-MDS/DSCI-532_2024_15_dreamhouse", target="_blank"),
                ". The data has been sourced from",
                html.A(" Link to data source", href="https://www.kaggle.com/datasets/jeremylarcher/american-house-prices-and-demographics-of-top-cities", target="_blank"),
                "."
            ], style={'textAlign': 'center', 'marginTop': '20px'})
        ])
    ], fluid=True)