import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import plotly.express as px
import pandas as pd
import requests
import json

from app import app

base_url = 'https://api.pro.coinbase.com/products/{}/candles?granularity=86400'

def getETHData(currency):
    sym = 'ETH' + '-' + currency
    url = base_url.format(sym)
    response = requests.get(url)
    if response.status_code == 200:
        data = pd.DataFrame(json.loads(response.text),
            columns=['Time', 'Low', 'High', 'Open', 'Close', 'Volume'])
        data['Date'] = pd.to_datetime(data['Time'], unit='s')
        return data
    else:
        return None
        
layout = html.Div([
    dcc.Link('Home', href='/home'),
    html.H1('ETH-Fiat Price Charts'),
    dcc.Dropdown(
        id='fiat-dropdown-2',
        options=[
            {'label': i, 'value': i} for i in [
                'USD', 'EUR', 'JPY', 'GBP', 'CHF'
            ]
        ]
    ),
    html.Div(id='eth-fiat-chart'),
    dcc.Link('View BTC Pricing', href='/btc')
])


@app.callback(
    Output('eth-fiat-chart', 'children'),
    Input('fiat-dropdown-2', 'value'))
def display_value(value):
    if value is None:
        return html.Div()
    data = getETHData(value)
    if data is None:
        return html.H3("No data found for ETH/{}".format(value))

    fig = px.line(data, x='Date', y='Close')
    return dcc.Graph(id='eth-fiat-chart-obj',
        figure=fig)