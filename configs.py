import multiprocessing
from urllib.parse import quote
import os

LOCAL_HOST = "127.0.0.1"

# LOCAL_HOST = "172.18.3.136"
# databases config
HOST = '127.0.0.1'
PORT = '5432'
DATABASE = 'ticket'
USERNAME = 'postgres'
PASSWORD = 'xiaohang1999'

# DB_URI = f"postgresql+psycopg2://{USERNAME}:{PASSWORD}@{HOST}:{PORT}/{DATABASE}"
DB_URI = f"mysql+pymysql://{USERNAME}:{PASSWORD}@{HOST}:{PORT}/{DATABASE}"
API_VERSION = "v1"
SQLALCHEMY_DATABASE_URI = DB_URI
SQLALCHEMY_TRACK_MODIFICATIONS = False
SQLALCHEMY_ECHO = False

SQLALCHEMY_ENGINE_OPTIONS = {'pool_pre_ping': True}
JSON_SORT_KEYS = False

FLASK_PORT = 5000
