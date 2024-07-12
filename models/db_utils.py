import os

import psycopg2

user = os.getenv("PG_DATABASE_USER")
password = os.getenv("PG_DATABASE_PASSWORD")
database = os.getenv("PG_DATABASE_NAME")


def execute_query(query, params=None, return_result=False):
    with psycopg2.connect(f"dbname={database} user={user} password={password}") as conn:
        with conn.cursor() as cursor:
            sql_data = None
            if params:
                cursor.execute(query, params)
            else:
                cursor.execute(query)
            if return_result:
                sql_data = cursor.fetchall()
    conn.close()
    if return_result:
        return sql_data
