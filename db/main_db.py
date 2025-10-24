import sqlite3
from db import queries
from config import path_db


def init_db():
    conn = sqlite3.connect(path_db)
    cursor = conn.cursor()
    cursor.execute(queries.CREATE_TABLE_LIST)
    conn.commit()
    conn.close()


def add_prod(name):
    conn = sqlite3.connect(path_db)
    cursor = conn.cursor()
    cursor.execute(queries.INSERT_PROD, (name, ))
    conn.commit()
    prod_id = cursor.lastrowid
    conn.close()
    return prod_id


def get_prod():
    conn = sqlite3.connect(path_db)
    cursor = conn.cursor()
    cursor.execute(queries.SELECT_PROD)
    list = cursor.fetchall()
    conn.close()
    return list


def delete_prod(prod_id):
    conn = sqlite3.connect(path_db)
    cursor = conn.cursor()
    cursor.execute(queries.DELETE_PROD, (prod_id, ))
    conn.commit()
    conn.close()

def bought(prod_id, bought):
    conn = sqlite3.connect(path_db)
    cursor = conn.cursor()
    cursor.execute(queries.UPDATE_PROD, (bought, prod_id))
    conn.commit()
    conn.close()
