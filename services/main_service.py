import os
from decouple import config


def get_all_stocks():
    stocks = os.listdir(config('PATH_TO_STOCKS_DATA'))
    return [(stock, stock.split('.')[0]) for stock in stocks]
