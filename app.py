import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output, State, ALL, MATCH
import dash_bootstrap_components as dbc
import plotly.graph_objects as go
import pandas as pd

app = dash.Dash(
    __name__, suppress_callback_exceptions=True)

currencies = ["USD", "EUR", "GBP", "JPY"]

app.layout = html.Div([
    dbc.Row([
        html.H1("Hosting a Dash App on PythonAnywhere!")
    ]),
    dbc.Row([
        dbc.Col([
            html.H2("Bitcoin Price")
        ]),
        dbc.Col([
            html.H3("Select Curency:"),
            dcc.Dropdown(
                id="currency",
                options=[{"label": i, "value": i} for i in currencies],
                value="USD"
            )
        ])
    ]),
    dbc.Row([
        html.Div(id="btc-price-chart")
    ])
])

@app.callback(
    Output("btc-price-chart", "children"),
    Input("currency", "value")
)
def getBTCData(currency):
    base_url = f"https://data.bitcoinity.org/export_data.csv?currency={currency}&data_type=price_volume&t=lb&timespan=30d&vu=curr"
    btc_df = pd.read_csv(base_url)
    # Build plot
    fig = go.Figure()
    fig.add_trace(
        go.Scatter(
            x=btc_df["Time"],
            y=btc_df["price"],
            line=dict(
                color="blue",
                width=3
            )
        )
    )

    fig.update_layout(
        title=f"BTC/{currency}",
        xaxis_title="Date",
        yaxis_title=f"Price {currency}"
    )

    return dcc.Graph(figure=fig)

if __name__ == "__main__":
    app.run_server(port=8880, debug=True)