import sys
from config import DB_DETAILS
from util import get_tables
from read import read_table


def main():
    env = sys.argv[1]
    db = DB_DETAILS[env]
    tables = get_tables('table_list')
    for table in tables['table_name']:
        data, column_name = read_table(db, table)
        for records in data:
            print(records)


if __name__ == '__main__':
    main()
