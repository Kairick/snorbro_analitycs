import datetime
import json
import os
import pandas as pd
import plotly
from decouple import config
import plotly.graph_objs as go


def get_all_stocks():
    stocks = os.listdir(config('PATH_TO_STOCKS_DATA'))
    return [(stock, stock.split('.')[0]) for stock in stocks]


def get_stock_chart(stock):
    stocks_path = config('PATH_TO_STOCKS_DATA')
    full_path = os.path.join(stocks_path, stock)
    stock_file = pd.read_csv(full_path)
    return get_chart(stock_file)


def get_chart(csv_data):
    json_datasets = []
    csv_2019 = csv_data[(csv_data['DATE'] > 20190201) & (csv_data['DATE'] < 20200201)]
    csv_2020 = csv_data[(csv_data['DATE'] > 20200201) & (csv_data['DATE'] < 20220201)]
    for dataset in [csv_data, csv_2019, csv_2020]:
        trace = go.Scatter(x=dataset["Unnamed: 0"], y=dataset["PRICE"])
        layout = go.Layout(xaxis=dict(title=""),
                           yaxis=dict(title="Цена"), )
        data = [trace]
        fig = go.Figure(data=data, layout=layout)
        fig_json = json.dumps(fig, cls=plotly.utils.PlotlyJSONEncoder)
        json_datasets.append(fig_json)
    return json_datasets

