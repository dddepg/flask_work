from flask import Flask, request, Response, json
from graduateBack import app
import graduateBack.sql as sql
import re
import time


@app.route('/getallpaper', methods=["POST"])
def getallpaper():
    conn = sql.getConn()
    cur = sql.getCur(conn)
    try:
        sql_word = "select title from paper order by updata desc where power=0"
        cur.execute(sql_word)
        results = cur.fetchall()
        res = {}
        reslist = list()
        for row in results:
            res["title"] = row[1]
            res["URL"] = row[2]
            reslist.append(res.copy())
        response = Response(json.dumps(reslist))
    except:
        sql.closeCur(cur, conn)
    else:
        sql.closeCur(cur, conn)
        return response

        
    