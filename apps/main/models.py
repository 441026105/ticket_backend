import datetime
from dataclasses import dataclass

from apps.user import User
from common.base_model import BaseModel
from common.db_utils import db


@dataclass
class ErrorLogin(BaseModel, db.Model):
    __tablename__ = "error_login"
    # __table_args__ = {'extend_existing': True}
    id: int = db.Column(db.Integer, primary_key=True)
    user_id: int = db.Column(
        db.Integer, db.ForeignKey('user.id'), unique=True
    )
    user = db.relationship(
        'User',
        backref=db.backref('error_login', lazy='dynamic')
    )
    error_times: int = db.Column(db.Integer)
    locked_state: bool = db.Column(db.Boolean, default=False)
    locked_time: datetime.datetime = db.Column(db.DateTime)




