from flask import Flask
from decouple import config
from webservice.routes import main_blueprint


app = Flask(__name__)

app.config.update(
    SECRET_KEY=config('SECRET_KEY'),
    CSRF_ENABLED=config("CSRF_ENABLED"),
    DEBUG=True
)


app.register_blueprint(main_blueprint)
