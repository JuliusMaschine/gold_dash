import dash
from dash import Input, Output
import plotly.express as px

import utils
import html_content

app = dash.Dash(__name__)

app.layout = html_content.html_layout
app.css.append_css(
    {"external_url": "https://codepen.io/chriddyp/pen/bWLwgP.css"}
)
server = app.server


@app.callback(
    [
        Output("gold-rate-line-graph", "figure"),
        Output("gold-rate-pie-chart-old", "figure"),
        Output("gold-rate-pie-chart-new", "figure"),
        Output("gold-rate-bar-chart", "figure"),
    ],
    [Input("date-slider", "value"), Input("curr-dropdown", "value")],
)
def update_graph(date_value, currency):

    graphs, dates = utils.graph_data(date_value, currency)

    start_year, end_year = dates

    dff, start_pie_data, end_pie_data, diff_bar = graphs

    line_graph = px.line(
        dff,
        x="Date",
        y=[currencies for currencies in currency],
        title=f"Gold Rate in top 6 currencies from {start_year} to {end_year}",
        template="plotly_dark",
    )

    old_pie_chart = px.pie(
        values=start_pie_data,
        names=[currencies for currencies in start_pie_data.index],
        title=f"Gold Rate in top 6 currencies in {start_year}",
        template="plotly_dark",
    )

    new_pie_chart = px.pie(
        values=end_pie_data,
        names=[currencies for currencies in end_pie_data.index],
        title=f"Gold Rate in top 6 currencies in {end_year}",
        template="plotly_dark",
    )

    bar_chart = px.bar(
        diff_bar,
        x="Countries",
        y="Percentage Growth",
        title=f"Gold Rate in currencies from {start_year} to {end_year}",
        template="plotly_dark",
    )

    return line_graph, old_pie_chart, new_pie_chart, bar_chart


if __name__ == "__main__":
    app.run_server(debug=True)
