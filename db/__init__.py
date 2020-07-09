import pymysql
import os


def connect():
    return pymysql.connect(
        host=os.environ.get('MARIADB_HOST', None),
        port=int(os.environ.get('MARIADB_PORT', 0)),
        user=os.environ.get('MARIADB_USER', None),
        passwd=os.environ.get('MARIADB_PASSWD', None),
        db=os.environ.get('MARIADB_DB', None),
        charset='utf8'
    )
