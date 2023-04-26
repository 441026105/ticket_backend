from common.utils import *
from . import admin
from .models import *
from flask import request, session


@admin.route("/items", methods=["GET"])
def get_items():
    return res_success(Items.query.all())


@admin.route("/items", methods=["POST"])
def add_items():
    items = request.json
    item = Items(items)
    item.save()
    return res_success("ok")


@admin.route("/items", methods=["PATCH"])
def update_items():
    items = request.json
    Items(items).update()
    return res_success("ok")


@admin.route("/items", methods=["DELETE"])
def delete_items():
    items = request.json
    Items(items).save()
    return res_success("ok")
