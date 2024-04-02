from dash import Dash, html

# Initialize the Dash app
app = Dash(__name__)
server = app.server

# Define the layout of the app
app.layout = html.Div([
    html.H1("American Housing Prices Dashboard"),
    html.H2("Project Overview"),
    html.P("This dashboard presents an interactive visualization of housing prices in top cities and states across top 50 cities in the United States of America. The data is sourced from a comprehensive dataset available on Kaggle, which includes demographics and house prices of the top cities in the United States. Our dashboard is built using the Dash package, enabling users to filter and explore the housing market data across various dimensions, such as state, city, house type, square footage, number of bedrooms and bathrooms, and more."),
    html.H3("This dashboard is for UBC MDS Program DSCI 532"),
    html.H4("Authors:"),
    html.Ul([
        html.Li("Ruocong Sun"),
        html.Li("Chun Li"),
        html.Li("Jake Barnabe"),
        html.Li("Zeily Garcia")
    ])
])

# Run the app
if __name__ == '__main__':
    app.run_server(debug=False)
