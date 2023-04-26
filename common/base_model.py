import dataclasses

from flask import current_app
from sqlalchemy.orm import class_mapper

from common.db_utils import db


class BaseModel(db.Model):
    __abstract__ = True
    query = db.session.query_property()

    def save(self):
        try:
            db.session.add(self)
            db.session.commit()

        except Exception as e:
            db.session.rollback()
            raise e

    def update(self):
        try:
            db.session.merge(self)
            db.session.commit()
        except Exception as e:
            db.session.rollback()
            raise e

    def delete(self):
        try:
            db.session.delete(self)
            db.session.commit()
        except Exception as e:
            db.session.rollback()
            raise e

    def batch_update(self, params: dict):
        for k, v in params.items():
            setattr(self, k, v)
        self.update()

    def as_dict(self):
        return dict((col.name, getattr(self, col.name)) for col in class_mapper(self.__class__).mapped_table.c)

    def to_json(self):
        return current_app.json.loads(current_app.json.dumps(self))
