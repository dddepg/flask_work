from flask import Flask, request, Response, json
from flask import render_template
from graduateBack import app
import graduateBack.sql as sql


@app.route('/managePass', methods=["POST"])
def managePass():
    conn = sql.getConn()
    cur = sql.getCur(conn)
    res = {}
    tele = request.form["tele"]
    email = request.form["email"]
    id = request.form["id"]
    try:
        sql_word = "SELECT usertele, useremail FROM user WHERE userName=%s"
        cur.execute(sql_word, [id])
        results = cur.fetchone()
    except Exception as e:
        res['result'] = "1"
        res['msg'] = "啊哦，数据库出错了"
        res["info"] = str(e)
        response = Response(json.dumps(res))
        sql.closeCur(cur, conn)
        return response
    else:
        if (tele == results[0] and email == results[1]):
            res['result'] = "0"
            response = Response(json.dumps(res))
            sql.closeCur(cur, conn)
            return response
        else:
            res['result'] = "1"
            res['msg'] = "电话和邮箱不匹配"
            res['res'] = results
            res['form'] = request.form
            response = Response(json.dumps(res))
            sql.closeCur(cur, conn)
            return response


@app.route('/changePass', methods=["POST"])
def changePass():
    conn = sql.getConn()
    cur = sql.getCur(conn)
    res = {}
    id = request.form["id"]
    newPass = request.form["newPass"]
    try:
        sql_word = "SELECT userPassword FROM user WHERE userName=%s"
        cur.execute(sql_word, [id])
        results = cur.fetchone()
        if (newPass == results[0]):
            res['result'] = "1"
            res['msg'] = "新密码不能和原密码一样"
            response = Response(json.dumps(res))
            sql.closeCur(cur, conn)
            return response
        sql_word2 = "UPDATE user SET userPassword=%s WHERE userName=%s"
        cur.execute(sql_word2, [newPass, id])

    except Exception as e:
        res['result'] = "1"
        res['msg'] = "啊哦，数据库出错了"
        res["info"] = str(e)
        response = Response(json.dumps(res))
        sql.closeCur(cur, conn)
        return response
    else:
        res['result'] = "0"
        res['msg'] = "修改成功，请重新登录"
        response = Response(json.dumps(res))
        sql.closeCur(cur, conn)
        return response


@app.route('/getAllUser', methods=["GET"])
def getAllUser():
    conn = sql.getConn()
    cur = sql.getCur(conn)
    try:
        sql_word = "SELECT userName, userPassword,id FROM user WHERE userpower='1'"
        cur.execute(sql_word)
        results = cur.fetchall()
        res = {}
        reslist = list()
        for row in results:
            res2 = {}
            reslist2 = list()
            res["name"] = row[0]
            res["password"] = row[1]
            res["id"] = row[2]
            reslist.append(res.copy())
    except ():
        res2 = {}
        res2['result'] = "2"
        res2['msg'] = "啊哦，数据库出错了"
        response = Response(json.dumps(res2))
        sql.closeCur(cur, conn)
        return response
    else:
        res2 = {}
        res2['result'] = "1"
        res2['data'] = reslist
        response = Response(json.dumps(res2))
        sql.closeCur(cur, conn)
        return response


@app.route('/SupergetAllUser', methods=["GET"])
def SupergetAllUser():
    conn = sql.getConn()
    cur = sql.getCur(conn)
    try:
        sql_word = "SELECT userName, userpower,id FROM user WHERE userpower!='3' "
        cur.execute(sql_word)
        results = cur.fetchall()
        res = {}
        reslist = list()
        for row in results:
            res2 = {}
            reslist2 = list()
            res["name"] = row[0]
            res["power"] = row[1]
            res["id"] = row[2]
            reslist.append(res.copy())
    except ():
        res2 = {}
        res2['result'] = "2"
        res2['msg'] = "啊哦，数据库出错了"
        response = Response(json.dumps(res2))
        sql.closeCur(cur, conn)
        return response
    else:
        res2 = {}
        res2['result'] = "1"
        res2['data'] = reslist
        response = Response(json.dumps(res2))
        sql.closeCur(cur, conn)
        return response


@app.route('/changeUserPowerApi', methods=["POST"])
def changeUserPowerApi():
    conn = sql.getConn()
    cur = sql.getCur(conn)
    id = int(request.form["id"])
    power = request.form["power"]
    try:
        if power == 1:
            sql_word = "UPDATE user SET userpower=2 WHERE id=%s "
            cur.execute(sql_word, id)
        else:
            sql_word = "UPDATE user SET userpower=1 WHERE id=%s "
            cur.execute(sql_word, id)
    except ():
        res2 = {}
        res2['result'] = "2"
        res2['msg'] = "啊哦，数据库出错了"
        response = Response(json.dumps(res2))
        sql.closeCur(cur, conn)
        return response
    else:
        res2 = {}
        res2['result'] = "1"
        response = Response(json.dumps(res2))
        sql.closeCur(cur, conn)
        return response


@app.route('/deleUser', methods=["POST"])
def deleUser():
    conn = sql.getConn()
    cur = sql.getCur(conn)
    userid = request.form["userid"]
    try:
        sql1 = "DELETE FROM user WHERE id=%s"
        cur.execute(sql1, [userid])
    except:
        res2 = {}
        res2['result'] = "2"
        res2['msg'] = "啊哦，数据库出错了"
        response = Response(json.dumps(res2))
        sql.closeCur(cur, conn)
        return response
    else:
        res2 = {}
        res2['result'] = "1"
        res2['msg'] = "删除成功"
        response = Response(json.dumps(res2))
        sql.closeCur(cur, conn)
        return response


@app.route('/rebackUser', methods=["POST"])
def rebackUser():
    conn = sql.getConn()
    cur = sql.getCur(conn)
    id = request.form["id"]
    try:
        sql1 = "SELECT userName FROM user WHERE id=%s"
        cur.execute(sql1, [id])
        results = cur.fetchall()
        sql_word2 = "UPDATE user SET userPassword=%s WHERE id=%s"
        cur.execute(sql_word2, [results[0], id])
    except:
        res2 = {}
        res2['result'] = "2"
        res2['msg'] = "啊哦，数据库出错了"
        response = Response(json.dumps(res2))
        sql.closeCur(cur, conn)
        return response
    else:
        res2 = {}
        res2['result'] = "1"
        res2['msg'] = "修改成功"
        response = Response(json.dumps(res2))
        sql.closeCur(cur, conn)
        return response


@app.route('/creatUser', methods=["POST"])
def creatUser():
    conn = sql.getConn()
    cur = sql.getCur(conn)
    num = int(request.form["num"])
    try:
        if (num == 1):
            sql1 = "INSERT INTO user ( userName, userPassword) VALUES\
                   ( %s,%s );"

            cur.execute(sql1, [request.form["name"], request.form["name"]])
        else:
            i = int(request.form["beginname"])
            while i <= int(request.form["endname"]):
                sql1 = "INSERT INTO user ( userName, userPassword) VALUES (%s,%s );"
                cur.execute(sql1, [i, i])
                i = i + 1
    except Exception as e:
        res = {}
        res['result'] = "1"
        res['msg'] = "啊哦，数据库出错了"
        res["info"] = str(e)
        response = Response(json.dumps(res))
        sql.closeCur(cur, conn)
        return response
    else:
        res2 = {}
        res2['result'] = "1"
        res2['msg'] = "添加成功"
        response = Response(json.dumps(res2))
        sql.closeCur(cur, conn)
        return response
