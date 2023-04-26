import json

from flask import jsonify

from consts import *


def to_json(inst, cls):
    d = dict()
    '''
    获取表里面的列并存到字典里面
    '''
    for c in cls.__table__.columns:
        v = getattr(inst, c.name)
        d[c.name] = v
    return json.dumps(d)


def list_to_dict(data, key, value):
    obj = {}
    for item in data:
        obj[item[key]] = item[value]
    return obj


def res_error(result_code, error_msg):
    """错误回调"""
    return jsonify(result_code=result_code, msg=error_msg)


def res_success(res_data):
    """成功回调"""
    return jsonify(result_code=SUCCESS_CODE, data=res_data)


def res_message(res_msg):
    """新增和删除的回调"""
    res_msg = {
        "msg": res_msg
    }
    return jsonify(result_code=SUCCESS_CODE, data=res_msg)


# 获取字典的深度
from functools import singledispatch, wraps


@singledispatch
def depth(_, _level=1, _memo=None):
    return _level


def _protect(f):
    """Protect against circular references"""

    @wraps(f)
    def wrapper(o, _level=1, _memo=None, **kwargs):
        _memo, id_ = _memo or set(), id(o)
        if id_ in _memo:
            return _level
        _memo.add(id_)
        return f(o, _level=_level, _memo=_memo, **kwargs)

    return wrapper


def _protected_register(cls, func=None, _orig=depth.register):
    """Include the _protect decorator when registering"""
    if func is None and isinstance(cls, type):
        return lambda f: _orig(cls, _protect(f))
    return _orig(cls, _protect(func)) if func is not None else _orig(_protect(cls))


depth.register = _protected_register


@depth.register
def _dict_depth(d: dict, _level=1, **kw):
    return max(depth(v, _level=_level + 1, **kw) for v in d.values())
