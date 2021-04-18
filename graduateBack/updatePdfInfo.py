from flask import Flask, request, Response, json
from graduateBack import app
import graduateBack.sql as sql
import re
import time


@app.route('/updatestate', methods=["POST"])
def updatestate():
    conn = sql.getConn()
    cur = sql.getCur(conn)
    paperid = request.form["id"]
    paperstate = request.form["state"]
    res = {}
    try:
        sql_word = "UPDATE paper SET paperstate=%s WHERE idpaper=%s"
        cur.execute(sql_word, [paperstate, paperid])
    except:
        res['result'] = "1"
        res['msg'] = "啊哦，数据库出错了"
        response = Response(json.dumps(res))
        sql.closeCur(cur, conn)
        return response
    else:
        res['result'] = "0"
        res['msg'] = "修改成功"
        response = Response(json.dumps(res))
        sql.closeCur(cur, conn)
        return response


@app.route('/addNewsApi', methods=["POST"])
def addNewsApi():
    conn = sql.getConn()
    cur = sql.getCur(conn)
    title = request.form["title"]
    newsurl = request.form["newsurl"]
    state = int(request.form["state"])
    res = {}
    try:
        if(state==1):
            sql_word = "INSERT INTO newly ( title, URL ) VALUES ( %s,%s );"
            cur.execute(sql_word, [title, newsurl])
        else:
            sql_word = "INSERT INTO tread ( title, URL ) VALUES ( %s,%s );"
            cur.execute(sql_word, [title, newsurl])
    except:
        res['result'] = "0"
        res['msg'] = "啊哦，数据库出错了"
        response = Response(json.dumps(res))
        sql.closeCur(cur, conn)
        return response
    else:
        res['result'] = "1"
        response = Response(json.dumps(res))
        sql.closeCur(cur, conn)
        return response