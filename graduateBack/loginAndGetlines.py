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
    sql_word = "SELECT userPassword FROM user WHERE userName=%s"
    cur.execute(sql_word, username)
    results = cur.fetchone()
    if (password == results[0]):
        res = {}
        res['result'] = "1"
        response = Response(json.dumps(res))
        sql.closeCur(cur, conn)
        return response
    else:
        res = {}
        res['data'] = "2"
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
