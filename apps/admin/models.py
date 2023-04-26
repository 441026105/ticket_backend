from dataclasses import dataclass
from datetime import datetime

from common.base_model import BaseModel
from common.db_utils import db


@dataclass
class Items(BaseModel, db.Model):
    __tablename__ = "items"

    id: int = db.Column(db.Integer, primary_key=True)
    name: str = db.Column(db.String(200))
    bgImg: str = db.Column(db.String(200))
    sort: str = db.Column(db.String(200))
    address: str = db.Column(db.String(200))
    time: datetime = db.Column(db.DateTime)
    price: float = db.Column(db.Numeric)
    hot: bool = db.Column(db.Boolean)

    def __init__(self, params: dict):
        for k, v in params.items():
            setattr(self, k, v)
