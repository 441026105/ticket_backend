import json

import requests
from flask import request
from flask_jwt_extended import create_access_token, create_refresh_token
from sqlalchemy import and_
from werkzeug import security

from common.jwt_auth import *
from common.utils import *
from . import user
from .models import *


# from common.redis_cache import redis_cache as r


@user.route("/", methods=["POST"], strict_slashes=False)
# @role_required(USER_ROLE['ADMIN'])
def create_user():
    req_user = request.get_json()
    hash_code = security.generate_password_hash(req_user["password"], "pbkdf2:sha256:5", 16)
    user_info = {
        "username": req_user["username"],
        "password": hash_code,
        "role": req_user["role"],
        "nickname": req_user.get("nickname"),
        "address": req_user.get("address"),
        "mobile_number": req_user.get("mobile_number")
    }
    user = User(user_info)
    user.update()
    return res_message("新增成功")


@user.route("/", methods=["PATCH"], strict_slashes=False)
@role_required(USER_ROLE['ADMIN'])
def update_user():
    req_user = request.get_json()
    if not req_user.get("id"):
        return res_error(10106, ERROR_CODE[10106])
    if req_user.get("password"):
        return res_error(10106, ERROR_CODE[10106])
    user = User(req_user)
    user.update()

    return res_message("修改成功")


@user.route("/", methods=["GET"], strict_slashes=False)
@role_required(USER_ROLE['ADMIN'])
def list_user():
    users = User.query.all()
    res_data = {
        "users": users
    }
    return res_success(res_data)


@user.route("/<userId>", methods=["DELETE"])
@role_required(USER_ROLE['ADMIN'])
def remove_user(userId):
    User.delete(User.query.filter(User.id == userId).first())
    return res_message("删除成功")


# @user.route("/", methods=["DELETE"], strict_slashes=False)
# @role_required(USER_ROLE['ADMIN'])
# def clear_user():
#     User.delete(User.query)
#     return res_message("删除成功")
