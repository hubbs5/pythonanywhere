import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import plotly.express as px
import pandas as pd
import requests
import json

from app import app

base_url = 'https://api.pro.coinbase.com/products/{}/candles?granularity=86400'

def getBTCData(currency):
    sym = 'BTC' + '-' + currency
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
    html.H1('BTC-Fiat Price Charts'),
    dcc.Dropdown(
        id='fiat-dropdown-1',
        options=[
            {'label': i, 'value': i} for i in [
                'USD', 'EUR', 'JPY', 'GBP', 'CHF'
            ]
        ]
    ),
    html.Div(id='btc-fiat-chart'),
    dcc.Link('View ETH Pricing', href='/eth')
])

@app.callback(
    Output('btc-fiat-chart', 'children'),
    Input('fiat-dropdown-1', 'value'))
def display_value(value):
    if value is None:
        return html.Div()
    data = getBTCData(value)
    if data is None:
        return html.H3("No data found for BTC/{}".format(value))

    fig = px.line(data, x='Date', y='Close')
    return dcc.Graph(id='btc-fiat-chart-obj',
        figure=fig)