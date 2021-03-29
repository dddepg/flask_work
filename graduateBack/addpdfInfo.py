from flask import Flask, request, Response, json
from flask import render_template
from graduateBack import app
import graduateBack.sql as sql
import re
import time


@app.route('/addpdfInfo', methods=["POST"])
def addpdfInfo():
    conn = sql.getConn()
    cur = sql.getCur(conn)
    res = {}
    title = request.form["title"]
    ownerID = request.form["ownerid"]
    url = request.form["url"]
    name = request.form["name"]
    data = time.strftime("%Y.%m.%d", time.localtime())
    power = request.form["power"]
    # 共享状态
    # 0：公开
    # 1：私人观看
    # 2：限制公开（未完成）
    paperType = request.form["paperType"]
    # 1-6:论文分类类型
    paperKeyWord = [request.form["key1"], request.form["key2"],
                    request.form["key3"], request.form["key4"], request.form["key5"]]
    try:
        # 将论文基本信息存入数据库
        sql_word = "INSINSERT INTO paper(title,author,url,update,power,paperType) VALUES (%s,%s,%s,%s,%s,%s) "
        cur.execute(sql_word, [title, name, url, data, power, paperType])
        # 获取新存入数据库的论文ID
        sql_word2 = "select id from paper WHERE title=%s,author=%s,url=%s,update=%s,power=%s,paperType=%s;"
        cur.execute(sql_word2, [title, name, url, data, power, paperType])
        results = cur.fetchone()
        # 将关键字存入数据库
        sql_word3 = "INSINSERT INTO paperkey(id,key1,key2,key3,key4,key5) VALUES (%s,%s,%s,%s,%s,%s)"
        cur.execute(sql_word3, [results[0], paperKeyWord[0], paperKeyWord[1],
                    paperKeyWord[2], paperKeyWord[3], paperKeyWord[4]])
        # 设置拥有关系
        sql_word4 = "INSINSERT INTO paperowner(userid,paperid) VALUES (%s,%s)"
        cur.execute(sql_word4, [results[0], ownerID])
    except:
        sql.closeCur(cur, conn)
        res['result'] = "2"
        res['msg'] = "啊哦，数据库出错了"
        response = Response(json.dumps(res))
        return response
    else:
        sql.closeCur(cur, conn)
        res['result'] = "1"
        res['msg'] = "上传成功"
        response = Response(json.dumps(res))
        return response
