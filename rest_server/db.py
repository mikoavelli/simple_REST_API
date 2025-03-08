import psycopg2

from sqlalchemy import text
from psycopg2.extras import RealDictCursor

from config import Config
from rest_server import db



def execute_query(query, params=None):
    connection = psycopg2.connect(
        host=Config.DB_HOST,
        database=Config.DB_DATABASE,
        user=Config.DB_USER,
        password=Config.DB_PASSWORD
    )
    try:
        with connection.cursor(cursor_factory=RealDictCursor) as cursor:
            cursor.execute(query, params or ())
            return cursor.fetchall()
    finally:
        connection.close()


def call_procedure(name, params=None):
    param_str = ', '.join(f":{key}" for key in params) if params else ''
    sql = text(f"CALL {name}({param_str})")
    db.session.execute(sql, params or {})
    db.session.commit()


def execute_function(name, params=None):
    param_str = ', '.join(f":{key}" for key in params) if params else ''
    sql = text(f"SELECT {name}({param_str})")
    result = db.session.execute(sql, params or {}).scalar()
    return result
