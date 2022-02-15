from dash import html
from dash import dcc
import pandas as pd


# Header content
header_description = (
    "Analysis of the gold rate from January 1978 to January 2021."
)

header_content = html.Div(
    children=[
        html.P(children="🪙", className="header-emoji"),
        html.H1(children="Gold Rate", className="header-title"),
        html.P(
            children=header_description,
            className="header-description",
        ),
    ],
    className="header",
)

# Body content
df = pd.read_csv("annual_gold_rate.csv")
currency = df.loc[:, df.columns != "Date"]

# Graph ids
line_graph = dcc.Graph(id="gold-rate-line-graph")
pie_chart_old = dcc.Graph(id="gold-rate-pie-chart-old")
pie_chart_new = dcc.Graph(id="gold-rate-pie-chart-new")
bar_chart = dcc.Graph(id="gold-rate-bar-chart")

# Create a RangeSlider component
date_slider = dcc.RangeSlider(
    id="date-slider",
    min=df["Date"].min(),
    max=df["Date"].max(),
    value=[df["Date"].min(), df["Date"].max()],
    marks={
        1980: "1980",
        1985: "1985",
        1990: "1990",
        1995: "1995",
        2000: "2000",
        2005: "2005",
        2010: "2010",
        2015: "2015",
        2020: "2020",
    },
)

curr_dropdown = dcc.Dropdown(
    id="curr-dropdown",
    options=[
        {"label": currency, "value": currency} for currency in currency.columns
    ],
    value=currency.columns,
    multi=True,
)

line_graph = html.Div(children=[line_graph], className="card")
date_slider = html.Div(children=[date_slider], className="card")
curr_dropdown = html.Div(children=[curr_dropdown], className="card")
pie_chart_old = html.Div(children=[pie_chart_old], className="six columns")
pie_chart_new = html.Div(children=[pie_chart_new], className="six columns")
pie_chart = html.Div(children=[pie_chart_old, pie_chart_new], className="rows")
pie_chart = html.Div(children=[pie_chart], className="card")
bar_chart = html.Div(children=[bar_chart], className="twelve columns")
bar_chart = html.Div(children=[bar_chart], className="card")

body_content = html.Div(
    children=[
        line_graph,
        date_slider,
        curr_dropdown,
        pie_chart,
        bar_chart,
    ],
    className="wrapper",
)

# footer_content = html.Div(children=[])

html_layout = html.Div(children=[header_content, body_content])
