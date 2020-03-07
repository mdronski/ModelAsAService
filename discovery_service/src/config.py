import os

DB_ENGINE = 'postgres'
DB_USER = os.environ['DB_USER']
DB_SECRET = os.environ['DB_SECRET']
DB_HOST = os.environ['DB_HOST']
DB_NAME = os.environ['DISCOVERY_SERVICE_DB_NAME']
SERVER_IDENTITY_SERVICE_HOST = os.environ['SERVER_IDENTITY_SERVICE_HOST']
SERVER_IDENTITY_SERVICE_PORT = os.environ['SERVER_IDENTITY_SERVICE_PORT']
SERVER_IDENTITY_SERVICE_PATH = os.environ['SERVER_IDENTITY_SERVICE_PATH']
SERVER_IDENTITY_URL = \
    f'{SERVER_IDENTITY_SERVICE_HOST}:{SERVER_IDENTITY_SERVICE_PORT}/' \
    f'{SERVER_IDENTITY_SERVICE_PATH}'
API_VERSION = 'v1'
SERVICE_NAME = os.environ['DISCOVERY_SERVICE_NAME']
SERVICE_SECRET = os.environ['DISCOVERY_SERVICE_SECRET']
DB_CONN_STRING = f'{DB_ENGINE}://{DB_USER}:{DB_SECRET}@{DB_HOST}/{DB_NAME}'
