# DB connection & DB select
import pymysql


class DBUser:
    def __init__(self, user, passwd, host, db, port, charset):
        self.user = user
        self.passwd = passwd
        self.host = host
        self.db = db
        self.port = port
        self.charset = charset


def db_connection(db_info):
    conn = pymysql.connect(user=db_info.user,
                           passwd=db_info.passwd,
                           host=db_info.host,
                           db=db_info.db,
                           port=db_info.port,
                           charset=db_info.charset)
    return conn


def db_select(query):
    conn = db_connection()
    try:
        with conn.cursor() as curs:
            curs.execute(query)
            rs = curs.fetchall()
    finally:
        conn.close()
        return rs
