import sqlite3
from sqlite3 import Error


# def config():
#     db = {
#         'host': 'localhost',
#         'user': 'yfinance-admin',
#         'password': 'yfinance',
#         'database': 'yfinance'
#     }
#
#     return db


def create_connection(db_name):
    connection = None
    try:
        connection = sqlite3.connect(db_name)
        return connection
    except Error as e:
        print(e)


def create_table(connection, query):
    try:
        cursor = connection.cursor()
        cursor.execute(query)
    except Error as e:
        print(e)


def main():
    db_name = 'dictionary.db'
    query = """
    CREATE TABLE IF NOT EXISTS dictionary (
        id integer PRIMARY KEY,
        word text,
        meaning text
    );
    """
    connection = create_connection(db_name)

    if connection is not None:
        create_table(connection, query)
    else:
        print('Error')


if __name__ == '__main__':
    main()