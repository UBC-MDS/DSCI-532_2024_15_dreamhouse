from dash import html
import dash_bootstrap_components as dbc
from src.components import (
    title, dropdown_box, usa_main_map, city_bar_graph,
    summary_stats_first_row, summary_stats_second_row, controls_box
)


def layout():
    return dbc.Container([
        title,  # Dashboard title
        dbc.Row([  # Main content row
            dbc.Col([  # First column for filters
                dbc.Row([dropdown_box]),
                dbc.Row([controls_box])
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


