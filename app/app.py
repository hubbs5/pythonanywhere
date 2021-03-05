import dash
import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html

external_stylesheets = [dbc.themes.UNITED]

app = dash.Dash(
    __name__,
    external_stylesheets=external_stylesheets, 
    prevent_initial_callbacks=True
)

server = app.server

if __name__ == "__main__":
    app.run_server(port=8880, debug=True)