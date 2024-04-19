import dash
import dash_bootstrap_components as dbc
from src.layout import layout
from src.callbacks.map_callbacks import register_map_callbacks
from src.callbacks.bar_callbacks import register_bar_callbacks
from src.callbacks.summary_callbacks import register_summary_callbacks
from src.callbacks.filters_callbacks import register_filter_callbacks

app = dash.Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])
server = app.server
app.layout = layout

app.title = 'Dreamhouse'

app._favicon = "favicon.ico"

register_filter_callbacks(app)
register_map_callbacks(app)
register_bar_callbacks(app)
register_summary_callbacks(app)

if __name__ == '__main__':
    app.run_server(debug=True)




