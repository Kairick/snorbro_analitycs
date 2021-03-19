from flask import Blueprint, render_template, request

from services.main_service import get_stock_chart
from webservice.forms import ChooseStockForm

main_blueprint = Blueprint('main_blueprint', __name__, static_folder='webservice/static',
                           template_folder='webservice/templates')


@main_blueprint.route('/')
def main():
    form = ChooseStockForm()
    return render_template('index.html', form=form, chart=None, stock=None)


@main_blueprint.route('/stock_chart', methods=['POST'])
def stock_chart():
    stock = request.form.get('stock')
    chart = get_stock_chart(stock)
    form = ChooseStockForm()
    return render_template('index.html', form=form, chart=chart, stock=stock.split('.')[0])

