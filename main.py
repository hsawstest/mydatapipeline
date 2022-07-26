import sys
from config import DB_DETAILS


def main():
    env = sys.argv[1]
    db = DB_DETAILS[env]
    print(db)


if __name__ == '__main__':
    main()
