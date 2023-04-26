# encoding:GBK
import datetime
from dataclasses import dataclass

from common.base_model import BaseModel
from common.db_utils import db


@dataclass
class User(BaseModel, db.Model):
    __tablename__ = "user"
    # __table_args__ = {'extend_existing': True}
    id: int = db.Column(db.Integer, primary_key=True)
    username: str = db.Column(db.String(80), unique=True)
    nickname: str = db.Column(db.String(80))
    password = db.Column(db.String(200))
    address: str = db.Column(db.String(200))
    role: int = db.Column(db.Integer)
    mobile_number: str = db.Column(db.String(200))

    create_time = db.Column(db.DateTime, default=datetime.datetime.now)
    update_time = db.Column(db.DateTime, default=datetime.datetime.now, onupdate=datetime.datetime.now)

    def __init__(self, params: dict):
        for k, v in params.items():
            setattr(self, k, v)

    def login_res_serial(self):
        return {
            "id": self.id,
            "role": self.role,
            "username": self.username,
            "nickname": self.nickname
        }
