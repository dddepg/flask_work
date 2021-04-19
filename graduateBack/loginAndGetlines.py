#coding=UTF-8
from flask import Flask, request, Response, json
from flask import render_template
from graduateBack import app
import graduateBack.sql as sql


@app.route('/login', methods=["POST"])
def login():
    conn = sql.getConn()
    cur = sql.getCur(conn)
    username = request.form["username"]
    password = request.form["password"]
    sql_word = "SELECT * FROM user WHERE userName=%s"
    cur.execute(sql_word, username)
    results = cur.fetchone()
    if (password == results[2]):
        res = {}
        res['result'] = "1"
        res['userID'] = results[0]
        res['userPower'] = results[3]
        res['userTrueName'] = results[4]
        response = Response(json.dumps(res))
        sql.closeCur(cur, conn)
        return response
    else:
        res = {}
        res['result'] = "2"
        response = Response(json.dumps(res))
        sql.closeCur(cur, conn)
        return response


@app.route('/newly')
def newly():
    conn = sql.getConn()
    cur = sql.getCur(conn)
    sql_word = "select * from newly order by id desc LIMIT 4"
    cur.execute(sql_word)
    results = cur.fetchall()
    res = {}
    reslist = list()
    for row in results:
        res["title"] = row[1]
        res["URL"] = row[2]
        res["id"] = row[0]
        reslist.append(res.copy())
    response = Response(json.dumps(reslist))
    sql.closeCur(cur, conn)
    return response


@app.route('/allnewly')
def allnewly():
    conn = sql.getConn()
    cur = sql.getCur(conn)
    sql_word = "select * from newly order by id desc"
    cur.execute(sql_word)
    results = cur.fetchall()
    res = {}
    reslist = list()
    for row in results:
        res["title"] = row[1]
        res["URL"] = row[2]
        res["id"] = row[0]
        reslist.append(res.copy())
    response = Response(json.dumps(reslist))
    sql.closeCur(cur, conn)
    return response


@app.route('/tread')
def tread():
    conn = sql.getConn()
    cur = sql.getCur(conn)
    sql_word = "select * from tread order by id desc LIMIT 4"
    cur.execute(sql_word)
    results = cur.fetchall()
    res = {}
    reslist = list()
    for row in results:
        res["title"] = row[1]
        res["URL"] = row[2]
        reslist.append(res.copy())
    response = Response(json.dumps(reslist))
    sql.closeCur(cur, conn)
    return response


@app.route('/alltread')
def alltread():
    conn = sql.getConn()
    cur = sql.getCur(conn)
    sql_word = "select * from tread order by id desc"
    cur.execute(sql_word)
    results = cur.fetchall()
    res = {}
    reslist = list()
    for row in results:
        res["title"] = row[1]
        res["URL"] = row[2]
        res["id"] = row[0]
        reslist.append(res.copy())
    response = Response(json.dumps(reslist))
    sql.closeCur(cur, conn)
    return response


@app.route('/deleNewsApi', methods=["POST"])
def deleNewsApi():
    conn = sql.getConn()
    cur = sql.getCur(conn)
    res = {}
    tehtype = int(request.form["type"])
    try:
        if (tehtype == 1):
            sql_word = "DELETE FROM newly WHERE id=%s "
            cur.execute(sql_word, [request.form["id"]])
        else:
            sql_word = "DELETE FROM tread WHERE id=%s "
            cur.execute(sql_word, [request.form["id"]])
    except:
        res['result'] = "1"
        res['msg'] = "啊哦，数据库出错了"
        response = Response(json.dumps(res))
        sql.closeCur(cur, conn)
        return response
    else:
        res['result'] = "0"
        res['msg'] = "删除成功"
        response = Response(json.dumps(res))
        sql.closeCur(cur, conn)
        return response