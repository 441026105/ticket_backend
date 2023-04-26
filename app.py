import sys

sys.path.append(".")
from datetime import timedelta

from flask import Flask
from flask_cors import *

import configs
import cus_exceptions
from common.db_utils import db, migrate
from common.json_coder import MyJSONEncoder
from common.jwt import jwt
from consts import *
import logging


def create_app(config=None):
    # app init
    app = Flask(__name__)
    if config is not None:
        app.config.from_mapping(config)
    # app.config["APPLICATION_ROOT"] = "/api/"
    app.config.from_object(configs)
    jwt.init_app(app)
    db.init_app(app)
    migrate.init_app(app, db)

    # Set up the Flask-JWT-Extended extension
    app.config["JWT_COOKIE_SECURE"] = False
    app.config["JWT_TOKEN_LOCATION"] = ["headers"]
    app.config["JWT_ACCESS_TOKEN_EXPIRES"] = timedelta(hours=JWT_TOKEN_LIFE)
    # app.config["JWT_ACCESS_TOKEN_EXPIRES"] = timedelta(minutes=1)
    app.config["JWT_REFRESH_TOKEN_EXPIRES"] = timedelta(hours=JWT_REFRESH_TOKEN_LIFE)
    app.config["JWT_SECRET_KEY"] = JWT_KEY
    app.config["SECRET_KEY"] = "12345678"

    @app.errorhandler(Exception)
    def handler_err(err):
        print(type(err))
        print(err)
        logging.error(type(err))
        logging.error(err)
        if app.config.get("DEBUG"):
            err = cus_exceptions.ApiException(debug_info=err)
        else:
            err = cus_exceptions.ApiException()
        return err.to_result()

    # json encoder

    app.json_encoder = MyJSONEncoder

    # register route
    from apps.user import user
    from apps.main import main
    from apps.admin import admin
    from apps.home import home

    app.register_blueprint(admin, url_prefix=admin.url_prefix)
    app.register_blueprint(user, url_prefix=user.url_prefix)
    app.register_blueprint(main, url_prefix=main.url_prefix)
    app.register_blueprint(home, url_prefix=home.url_prefix)

    return app


app = create_app()
