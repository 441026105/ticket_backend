from common.utils import *
from . import home
from .models import *
from flask import request, session
from apps.admin.models import Items


@home.route("/items", methods=["GET"])
def get_items():
    sort = request.args.get("sort")

    if not sort:
        items = Items.query.all()
        res_data = items
    else:
        res_data = [{"title": sort, "boxR": []}]
        items = Items.query.filter(Items.sort == sort).all()
        for item in items:
            item_info = {
                "title": item.name,
                "bgImg": item.bgImg,
                "venue": item.address,
                "time": item.time,
                "price": item.price,
            }
            if item.hot:
                res_data[0].update({"boxL": item_info})
            else:
                res_data[0]["boxR"].append(item_info)

    return res_success(res_data)
