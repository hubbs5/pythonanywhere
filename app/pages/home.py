import dash_core_components as dcc
import dash_html_components as html

from app import app

layout = html.Div([
    html.H1('Crypto Pricing App'),
    html.P('This is a simple example app to show you how to deploy apps on PythonAnywhere.'),
    html.P('The code and tutorial can be found in the links below:'),
    html.A('Code', href='https://github.com/hubbs5/pythonanywhere', target='_blank'),
    html.Br(),
    html.A('Tutorial', href='/tutorial'),
    html.P('Other pages in the app:'),
    dcc.Link('BTC Pricing', href='/btc'),
    html.Br(),
    dcc.Link('ETH Pricing', href='/eth')
])