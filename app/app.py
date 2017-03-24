from flask import Flask, Blueprint
from flask_restplus import Resource, Api

def create_app(config_filename):
    app = Flask(__name__)
    app.config.from_pyfile(config_filename)

    from views.api_v1.api_v1 import v1
    app.register_blueprint(v1)

    return app
