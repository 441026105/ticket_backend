import decimal
from datetime import datetime, timedelta

from flask.json import JSONEncoder


class MyJSONEncoder(JSONEncoder):
    def default(self, obj):
        if isinstance(obj, decimal.Decimal):
            return str(obj)
        elif type(obj) == timedelta:
            return str(obj)
        elif type(obj) == datetime:
            return obj.isoformat(sep=" ")
        else:
            return super(MyJSONEncoder, self).default(obj)
