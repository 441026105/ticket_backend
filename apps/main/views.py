from flask import request, session
from flask_jwt_extended import create_access_token, create_refresh_token
from werkzeug import security

from common.utils import *
from . import main
from .models import *


@main.route("/login", methods=["POST"])
def login():
    username = request.json.get("username", None)
    password = request.json.get("password", None)
    user = User.query.filter(User.username == username).first()

    if not user:
        return res_error(10101, ERROR_CODE[10101].format(str(username)))
    pwd_hash = user.password

    error_login = ErrorLogin.query.filter(ErrorLogin.user_id == user.id).first()
    error_msg_10103 = ERROR_CODE[10103].format(str(username), LOGIN_ERROR_LOCKED_TIME)
    if error_login and error_login.locked_state and (
            datetime.datetime.now() - error_login.locked_time).total_seconds() < LOGIN_ERROR_LOCKED_TIME * 60:
        return res_error(10103, error_msg_10103)

    if not security.check_password_hash(pwd_hash, password):
        if not error_login:
            add_error_login = ErrorLogin(user_id=user.id, error_times=1, locked_state=False, )
            ErrorLogin.save(add_error_login)
            res_error_msg = ERROR_CODE[10102].format(str(username),
                                                     LOGIN_ERROR_LIMITED_TIMES - add_error_login.error_times,
                                                     LOGIN_ERROR_LOCKED_TIME)
            return res_error(10102, res_error_msg)
        else:
            error_msg_10102 = ERROR_CODE[10102].format(str(username),
                                                       LOGIN_ERROR_LIMITED_TIMES - error_login.error_times - 1,
                                                       LOGIN_ERROR_LOCKED_TIME)

            if not error_login.locked_state:
                if not error_login.error_times == LOGIN_ERROR_LIMITED_TIMES - 1:
                    error_login.error_times += 1
                    ErrorLogin.save(error_login)
                    return res_error(10102, error_msg_10102)
                else:
                    error_login.error_times += 1
                    error_login.locked_state = True
                    error_login.locked_time = datetime.datetime.now()
                    ErrorLogin.save(error_login)
                    return res_error(10103, error_msg_10103)
            else:
                if (
                        datetime.datetime.now() - error_login.locked_time).total_seconds() > LOGIN_ERROR_LOCKED_TIME * 60:
                    error_login.locked_state = False
                    error_login.error_times = 1
                    error_login.locked_time = None
                    ErrorLogin.save(error_login)
                    return res_error(10102, error_msg_10102)
                else:
                    return res_error(10103, error_msg_10103)

    else:

        if error_login:
            ErrorLogin.delete(error_login)
        user_serialize = user.login_res_serial()

        token = create_access_token(
            identity=user
        )
        refresh_token = create_refresh_token(
            identity=user
        )
        res_data = {
            "user": user_serialize,
            "access_token": token,
            "refresh_token": refresh_token
        }
        return res_success(res_data)





@main.route("/logout", methods=["GET"])
def logout():
    session.pop('user_id', None)
    return res_success({})
