#coding=UTF-8
import pymysql


# 1. 连接数据库，
def getConn():
    conn = pymysql.connect(
        host='172.17.0.2',
        port=3306,
        user='root',
        password='MYdb20210208',
        db='my_graduate_design',
        charset='utf8',
        autocommit=True,  # 如果插入数据，， 是否自动提交? 和conn.commit()功能一致。
    )
    return conn


def closeConn(conn):
    # 5. 关闭连接
    conn.close()


def getCur(conn):
    cur = conn.cursor()
    return cur


def closeCur(cur, conn):
    cur.close()
    closeConn(conn)
