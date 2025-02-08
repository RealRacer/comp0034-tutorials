# Imports for Dash and Dash.html
from dash import Dash, html
import dash_bootstrap_components as dbc

meta_tags = [{"name": "viewport", "content": "width=device-width, initial-scale=1"}]
external_stylesheets = [dbc.themes.JOURNAL]

# Create an instance of the Dash app
app = Dash(__name__,
           external_stylesheets=external_stylesheets,
           meta_tags=meta_tags)


row_one = dbc.Row([
    dbc.Col(['App name and text']),
])

row_two = dbc.Row([
    dbc.Col(children=['drop down'], width=4),
    dbc.Col(children=['check boxes'], width={"size": 4, "offset": 2})
    # 2 'empty' columns between this and the previous column
])

row_three = dbc.Row([
    dbc.Col(['Im ticc'], width=6),
    dbc.Col(['Bomba'], width=6),
])

row_four = dbc.Row([
    dbc.Col(['stinky'], width=8),
    dbc.Col(['bludc'], width=4)
])
# Add an HTML layout to the Dash app
app.layout = dbc.Container([
    row_one,
    row_two,
    row_three,
    row_four
])





# Run the app
if __name__ == '__main__':
    app.run(debug=True, port=5050)
