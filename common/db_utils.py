from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
import sqlalchemy

migrate = Migrate()


# db = SQLAlchemy()
class MySqlAlchemy(SQLAlchemy):
    def __init__(self):
        self.Column = sqlalchemy.Column
        self.Integer = sqlalchemy.Integer
        self.ForeignKey = sqlalchemy.ForeignKey
        self.Boolean = sqlalchemy.Boolean
        self.DateTime = sqlalchemy.DateTime
        self.VARCHAR = sqlalchemy.VARCHAR
        self.String = sqlalchemy.String
        self.Numeric = sqlalchemy.Numeric
        self.BigInteger = sqlalchemy.BigInteger
        self.FetchedValue = sqlalchemy.FetchedValue
        super().__init__()

    pass


db = MySqlAlchemy()
