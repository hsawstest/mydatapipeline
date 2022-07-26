from util import get_mysql_connection
from config import DB_DETAILS


def read_table(db_details, table_name, limit=0):
    source = db_details['SOURCE_DB']
    connection = get_mysql_connection(db_host=source['DB_HOST'],
                                      db_name=source['DB_NAME'],
                                      db_user=source['DB_USER'],
                                      db_pass=source['DB_PASS']
                                      )
    cursor = connection.cursor()
    if limit == 0:
        query = f'SELECT * FROM TESTDB.{table_name}'
    else:
        query = f'SELECT * FROM TESTDB.{table_name} LIMIT {limit}'
    cursor.execute(query)
    data = cursor.fetchall()
    column_names = cursor.column_names

    connection.close()
    return data, column_names
