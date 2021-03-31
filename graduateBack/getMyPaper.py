from flask import Flask, request, Response, json
from graduateBack import app
import graduateBack.sql as sql
import re
import time


@app.route('/getMyPaper', methods=["POST"])
def getMyPaper():
    conn = sql.getConn()
    cur = sql.getCur(conn)
    id= request.form["id"]
    try:
        sql_word = "SELECT paper.papertitle,paper.paperurl,\
            paper.uploaddate,paper.idpaper FROM paper \
                join paperowner on paper.idpaper=paperowne.paperid\
                     where paperowner.ownerid=%s"
        cur.execute(sql_word,id)
        results = cur.fetchall()
        res = {}
        reslist = list()
        for row in results:
            res["title"] = row[0]
            res["URL"] = row[1]
            res["date"] = row[2]
            res["id"] = row[3]
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