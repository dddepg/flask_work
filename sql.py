import pymysql
# 1. 连接数据库，
conn = pymysql.connect(
    host='sh-cynosdbmysql-grp-b6j6byfw.sql.tencentcdb.com',
    port=21143,
    user='root',
    password='MYdb20210208',
    db='my_graduate_design',
    charset='utf8',
    autocommit=True,    # 如果插入数据，， 是否自动提交? 和conn.commit()功能一致。
)
cur = conn.cursor()
def getCur():
    return cur
    
def closeCur():
    # 4. 关闭游标
    cur.close()
    # 5. 关闭连接
    conn.close()


