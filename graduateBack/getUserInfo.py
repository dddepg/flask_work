from flask import Flask, request, Response, json
from flask import render_template
from graduateBack import app
import graduateBack.sql as sql
import re

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
    id = request.form["id"]
    tele = request.form["tele"]
    email = request.form["email"]
    check=checkInfoRight(tele,email)
    # 0：电话长度和邮箱都符合标准
    # 1：电话长度符合，但邮箱不是QQ或163
    # 2：电话长度符合，但邮箱格式不对
    # 3：电话长度不符，但邮箱符合标准
    # 4：电话长度不符，但邮箱不是QQ或163
    # 5：电话和邮箱都不符，
    if check==0:
        try: 
            sql_word = "UPDATE user SET usertele = %s ,useremail =%s WHERE id=%s"
            cur.execute(sql_word, [tele, email, id])
        except:
            sql.closeCur(cur, conn)
            res['result'] = "2"
            res['msg']="啊哦，数据库出错了"
            response = Response(json.dumps(res))
            return response
        else:
            sql.closeCur(cur, conn)
            res['result'] = "1"
            response = Response(json.dumps(res))
            return response
    elif check==1:
        res['result'] = "2"
        res['msg']="请输入QQ或163邮箱"
        response = Response(json.dumps(res))
        return response
    elif check==2:
        res['result'] = "2"
        res['msg']="请入正确的邮箱"
        response = Response(json.dumps(res))
        return response
    elif check==3:
        res['result'] = "2"
        res['msg']="请入正确的中国大陆电话（11位数字）"
        response = Response(json.dumps(res))
        return response
    elif check==4:
        res['result'] = "2"
        res['msg']="请入正确的中国大陆电话（11位数字），邮箱请输入QQ或163邮箱"
        response = Response(json.dumps(res))
        return response
    elif check==5:
        res['result'] = "2"
        res['msg']="请入正确的中国大陆电话（11位数字）和邮箱"
        response = Response(json.dumps(res))
        return response
    else:
        res['result'] = "2"
        res['msg']="未知错误，请联系管理员"
        response = Response(json.dumps(res))
        return response


def checkInfoRight(tele,email):
    if tele.isdigit() and len(tele)==11:
        rest=re.split(r'(\w*)\@(.*)\.(com)',email)
        if rest[0]=="" and rest[4]=="" and rest[3]=="com":
            if rest[2]=="qq" or rest[2]=="163":
                return 0
            else:
                return 1
        else:
            return 2
    else:
        rest=re.split(r'(\w*)\@(.*)\.(com)',email)
        if rest[0]=="" and rest[4]=="" and rest[3]=="com":
            if rest[2]=="qq" or rest[2]=="163":
                return 3
            else:
                return 4
        else:
            return 5 