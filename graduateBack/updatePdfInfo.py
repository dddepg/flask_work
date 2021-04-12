from flask import Flask, request, Response, json
from graduateBack import app
import graduateBack.sql as sql
import re
import time


@app.route('/updatestate', methods=["POST"])
def updatestate():
    conn = sql.getConn()
    cur = sql.getCur(conn)
    paperid= request.form["id"]
    paperstate=request.form["state"]
    res={}
    try:
        sql_word="UPDATE paper SET paperstate=%s WHERE idpaper=%s"
        cur.execute(sql_word,[paperstate,paperid])
    except:
        res['result']="1"
        res['msg']="啊哦，数据库出错了"
        response = Response(json.dumps(res))
        sql.closeCur(cur, conn)
        return response
    else:
        res['result']="0"
        res['msg']="修改成功"
        response = Response(json.dumps(res))
        sql.closeCur(cur, conn)
        return response

    

