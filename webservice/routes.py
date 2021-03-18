from flask import Blueprint, render_template, request

from webservice.forms import ChooseStockForm

main_blueprint = Blueprint('main_blueprint', __name__, static_folder='webservice/static',
                           template_folder='webservice/templates')


@main_blueprint.route('/')
def main():
    form = ChooseStockForm()
    return render_template('index.html', form=form, chart=None)


@main_blueprint.route('/get_stock_chart', methods=['POST'])
def get_stock_chart():
    stock = request.form.get('stock')

    form = ChooseStockForm()
    return render_template('index.html', form=form, chart=None)