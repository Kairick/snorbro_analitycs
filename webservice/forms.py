from wtforms import Form, SelectField

from services.main_service import get_all_stocks


class ChooseStockForm(Form):
    stock = SelectField(choices=get_all_stocks())
