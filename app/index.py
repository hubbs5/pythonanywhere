import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import logging

from app import app
from pages import home, page1, page2

logger = logging.getLogger("PA-Test")

app.layout = html.Div([
    dcc.Location(id='url', refresh=False),
    html.Div(id='page-content')
])

@app.callback(Output('page-content', 'children'),
              Input('url', 'pathname'))
def display_page(pathname):
    if pathname == '/home' or pathname == '/':
        return home.layout
    elif pathname == '/btc':
        return page1.layout
    elif pathname == '/eth':
        return page2.layout
    else:
        app.logger.warning("404 Error")
        return "404", 
        # return home.layout

if __name__ == '__main__':
    app.run_server(debug=True)