import logging

from sqlalchemy_utils import drop_database

from .config import DB_CONN_STRING
from .app import app
from .model import db


logging.getLogger().setLevel(logging.INFO)


def drop_db() -> None:
    drop_database(DB_CONN_STRING)
    logging.info(f'Services identity database deleted')


if __name__ == '__main__':
    drop_db()
