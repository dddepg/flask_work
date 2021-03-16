import sql as sql

conn = sql.getConn()
cur = sql.getCur(conn)
sql_word = "SELECT * FROM user WHERE id=%s"
cur.execute(sql_word, 3)
results = cur.fetchone()
print(results)
sql.closeCur(cur, conn)