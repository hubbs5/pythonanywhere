import dash
import dash_core_components as dcc
import dash_html_components as html
import dash_bootstrap_components as dbc
from dash.dependencies import Input, Output
from flask import Response, redirect

from app import server
from app import app

from pages import home, page1, page2

PAGES = ['/home', '/page1', '/page2']

SIDEBAR_STYLE = {
    "position": "fixed",
    "top": 0,
    "left": 0,
    "bottom": 0,
    "width": "18rem",
    "padding": "2rem 1rem",
    "background-color": "#f8f9fa",
}

sidebar = html.Div([
    html.H1('Python Anywhere Multi-Page Dash App'),
    html.Hr(),
    dbc.Nav([
        dbc.NavItem(
            dbc.NavLink('Home', href='/home', id='home-link')
        ),
        dbc.NavItem(
            dbc.NavLink('Page 1', href='/page1', id='page1-link')
        ),
        dbc.NavItem(
            dbc.NavLink('Page 2', href='/page2', id='page2-link')
        )
    ],
        vertical=True
    )
    ],
    style=SIDEBAR_STYLE
)

layout = html.Div([
    sidebar,
    dcc.Location(id='base-url', refresh=True),

    html.Div([
        dbc.Container(home.layout)
    ],
        id='home-display',
        style={'display': 'none'}
    ),

    html.Div([
        dbc.Container(page1.layout)
    ],
        id='page1-display',
        style={'display': 'none'}
    ),

    html.Div([
        dbc.Container(page2.layout)
    ],
        id='page2-display',
        style={'display': 'none'}
    )
])

@app.callback(
    [Output('home-display', 'style'),
     Output('page1-display', 'style'),
     Output('page2-display', 'style')],
    Input('base-url', 'pathname')
)
def router(pathname):
    '''
    Routes to correct page based on pathname.
    '''
    output = []
    for p in PAGES:
        if pathname in p and pathname != '/':
            output.append(
                {'display': 'block'}
            )
        elif pathname == '/' and 'home' in 'p':
            output.append(
                {'display': 'block'}
            )
        else:
            output.append(
                {'display': 'none'}
            )
    return output