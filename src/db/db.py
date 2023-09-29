import sqlite3
from flask import current_app, g


def get_conn():
    if 'conn' not in g:
        g.conn = sqlite3.connect(
            database=current_app.config['DB_NAME']
        )

    return g.conn


def db_extract(query, data):
    conn = get_conn()
    with conn.cursor() as cur:
        try:
            cur.execute(query, data)
        except Exception as e:
            print(e)
            return None
        return cur.fetchall()


def db_submit(query, data):
    conn = get_conn()
    with conn.cursor() as cur:
        try:
            cur.execute(query, data)
        except Exception as e:
            print(e)
    conn.commit()


def close_conn(e=None):
    conn = g.pop('conn', None)

    if conn is not None:
        conn.close()


def init_app(app):
    app.teardown_appcontext(close_conn)
