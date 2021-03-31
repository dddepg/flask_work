from flask import Flask, request, Response, json
from graduateBack import app
import graduateBack.sql as sql
import re
import time


@app.route('/getallpaper', methods=["GET"])
def getallpaper():
    conn = sql.getConn()
    cur = sql.getCur(conn)
    try:
        sql_word = "SELECT paper.papertitle,paper.paperurl,paperkey.key1,paperkey.key2,\
                    paperkey.key3,paperkey.key4,paperkey.key5 FROM paper\
                    LEFT JOIN paperkey on paper.idpaper=paperkey.id where paper.paperstate=0"
        cur.execute(sql_word)
        results = cur.fetchall()
        res = {}
        reslist = list()
        for row in results:
            res["title"] = row[1]
            res["URL"] = row[2]
            reslist.append(res.copy())
    except:
        res2={}
        res2['result']="2"
        res2['msg']="啊哦，数据库出错了"
        response = Response(json.dumps(res2))
        sql.closeCur(cur, conn)
        return response
    else:
        res2={}
        res2['result']="1"
        res2['data']=reslist
        response = Response(json.dumps(res2))
        sql.closeCur(cur, conn)
        return response

@app.route('/getTypePaper', methods=["POST"])
def getTypePaper():
    paperType = request.form["type"]
    conn = sql.getConn()
    cur = sql.getCur(conn)
    try:
        sql_word = "SELECT paper.papertitle,paper.paperurl,paperkey.key1,paperkey.key2,\
                    paperkey.key3,paperkey.key4,paperkey.key5 FROM paper\
                    LEFT JOIN paperkey on paper.idpaper=paperkey.id where paper.paperstate=0 AND paper.paperType=%s"
        cur.execute(sql_word,paperType)
        results = cur.fetchall()
        res = {}
        reslist = list()
        for row in results:
            res["title"] = row[0]
            res["URL"] = row[1]
            res["key1"]
            res["key2"]
            res["key3"]
            res["key4"]
            res["key5"]
            reslist.append(res.copy())
    except:
        res2={}
        res2['result']="2"
        res2['msg']="啊哦，数据库出错了"
        response = Response(json.dumps(res2))
        sql.closeCur(cur, conn)
        return response
    else:
        res2={}
        res2['result']="1"
        res2['data']=reslist
        response = Response(json.dumps(res2))
        sql.closeCur(cur, conn)
        return response