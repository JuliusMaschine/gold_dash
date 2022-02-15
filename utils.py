from math import ceil
import pandas as pd

import html_content


def graph_data(date_value, currency):
    dff = html_content.df

    # Transform the years into a rounded integers
    start_year, end_year = date_value
    start_year, end_year = int(ceil(start_year)), int(ceil(end_year))

    dates = start_year, end_year

    # arranges the dataframe so it only includes the starting year
    # and ends with the end year
    lower_bound_year = dff[(dff["Date"] >= start_year)]
    upper_bound_year = dff[(dff["Date"] <= end_year)]

    dff = lower_bound_year.merge(upper_bound_year, how="inner")

    # Splits the dataframe into two dataframes, one for the starting year
    # and one for the end year
    starter_pie = dff[(dff["Date"] == start_year)][currency]
    end_pie = dff[(dff["Date"] == end_year)][currency]

    # fill the NA values with 0 for the final bar graph

    diff_bar_data = (
        (end_pie - starter_pie.squeeze().fillna(0))
        / starter_pie.squeeze()
        * 100
    )
    diff_bar_data = diff_bar_data.squeeze()
    diff_bar_data = pd.DataFrame(
        {
            "Countries": diff_bar_data.index,
            "Percentage Growth": diff_bar_data.values,
        }
    )

    # turn the graphs iinto series and then drop the empty rows
    starter_pie_series = starter_pie.squeeze().dropna()
    end_pie_series = end_pie.squeeze().dropna()

    graphs = dff, starter_pie_series, end_pie_series, diff_bar_data

    return graphs, dates
