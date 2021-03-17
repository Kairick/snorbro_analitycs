from flask import Blueprint, redirect, url_for, render_template

main_blueprint = Blueprint('main_blueprint', __name__, static_folder='webservice/static',
                           template_folder='webservice/templates')


@main_blueprint.route('/')
def main():
    return render_template('index.html')


