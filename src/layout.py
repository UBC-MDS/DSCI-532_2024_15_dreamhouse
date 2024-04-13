from dash import html, dcc
import dash_bootstrap_components as dbc
from src.components import (
    title, state_dropdown, city_dropdown, square_footage_slider, price_range_slider,
    price_per_square_footage_range_slider, home_income_range_slider, beds_input,
    baths_input, clear_all_button, usa_main_map, city_bar_graph,
    summary_stats_first_row, summary_stats_second_row
)


def layout():
    return dbc.Container([
        title,  # Dashboard title
        dbc.Row([  # Main content row
            dbc.Col([  # First column for filters
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
            dbc.Col([  # Second column for maps, graphs, and stats
                dbc.Row([  # Maps and graphs
                    dbc.Col([usa_main_map], md=6),
                    dbc.Col([city_bar_graph], md=6),
                ]),
                summary_stats_first_row,  # Summary statistics
                summary_stats_second_row,
            ], md=10),
        ]),
        html.Div([  # Footer
            html.P([
                "This dashboard was made by Group 15 of MDS DSCI 532",
                html.A(" Link to Github source", href="https://github.com/UBC-MDS/DSCI-532_2024_15_dreamhouse", target="_blank"),
                ". The data has been sourced from",
                html.A(" Link to data source", href="https://www.kaggle.com/datasets/jeremylarcher/american-house-prices-and-demographics-of-top-cities", target="_blank"),
                "."
            ], style={'textAlign': 'center', 'marginTop': '20px'})
        ])
    ], fluid=True)


