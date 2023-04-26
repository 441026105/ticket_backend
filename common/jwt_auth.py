import sys
from functools import wraps

import flask_jwt_extended.exceptions
from flask import abort, jsonify, current_app
from flask_jwt_extended import verify_jwt_in_request, current_user
from consts import *
from common.utils import res_error


def role_required(role):
    def wrapper(fn):
        @wraps(fn)
        def decorator(*args, **kwargs):
            try:
                verify_jwt_in_request()
            except flask_jwt_extended.exceptions.NoAuthorizationError as no_auth_error:
                return res_error(10106, no_auth_error.args)
            except Exception as e:
                print(e)
                return res_error(10105, ERROR_CODE[10105])
            if not current_user or current_user.role > role:
                return res_error(10106, ERROR_CODE[10106])
            else:
                return fn(*args, **kwargs)

        return decorator

    return wrapper
