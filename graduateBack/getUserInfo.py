from flask import Flask, request, Response, json
from flask import render_template
from graduateBack import app
import graduateBack.sql as sql


@app.route('/userInfo', methods=["POST"])
def userInfo():
    conn = sql.getConn()
    cur = sql.getCur(conn)
    id = request.form["id"]
    sql_word = "SELECT usertele,useremail FROM user WHERE id=%s"
    cur.execute(sql_word, id)
    results = cur.fetchone()
    res = {}
    res['tele'] = results[0]
    res['email'] = results[1]
    response = Response(json.dumps(res))
    sql.closeCur(cur, conn)
    return response


@app.route('/changeUserInfo', methods=["POST"])
def changeUserInfo():
    conn = sql.getConn()
    cur = sql.getCur(conn)
    res = {}
    try:   
        id = request.form["id"]
        tele = request.form["tele"]
        email = request.form["email"]
        sql_word = "UPDATE user SET usertele = %s ,useremail =%s WHERE id=%s"
        cur.execute(sql_word, [tele, email, id])
    except:
        sql.closeCur(cur, conn)
        res['result'] = "2"
        response = Response(json.dumps(res))
        return response
    else:
        sql.closeCur(cur, conn)
        res['result'] = "1"
        response = Response(json.dumps(res))
        return response

