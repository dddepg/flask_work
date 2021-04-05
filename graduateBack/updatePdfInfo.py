from flask import Flask, request, Response, json
from graduateBack import app
import graduateBack.sql as sql
import re
import time


@app.route('/getpdfInfo', methods=["POST"])
def getpdfInfo():
    conn = sql.getConn()
    cur = sql.getCur(conn)
    paperid= request.form["paperid"]
    res={}
    try:
        sql_word="SELECT paper.*,paperkey.* from paper join paperkey on paper.idpaper=paperkey.id where idpaper=%s"
        cur.execute(sql_word,paperid)
        results = cur.fetchall()
        res["result"]=1
        res["title"]=results[1]
        res["author"]=results[2]
        res["url"]=results[3]
        res["type"]=results[5]
        res["state"]=results[6]
        res["key1"]=results[8]
        res["key2"]=results[9]
        res["key3"]=results[10]
        res["key4"]=results[11]
        res["key5"]=results[12]
    except:
        res['result']="2"
        res['msg']="啊哦，数据库出错了"
        response = Response(json.dumps(res))
        sql.closeCur(cur, conn)
        return response
    else:
        response = Response(json.dumps(res))
        sql.closeCur(cur, conn)
        return response

    

