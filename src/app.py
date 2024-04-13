import dash
import dash_bootstrap_components as dbc
from src.layout import layout
from callbacks.map_callbacks import register_map_callbacks
from callbacks.bar_callbacks import register_bar_callbacks
from callbacks.summary_callbacks import register_summary_callbacks
from callbacks.filters_callbacks import register_filter_callbacks

app = dash.Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])
server = app.server
app.layout = layout

register_filter_callbacks(app)
register_map_callbacks(app)
register_bar_callbacks(app)
register_summary_callbacks(app)

if __name__ == '__main__':
    app.run_server(debug=False)


