from flask import Flask, request, Response, json
from graduateBack import app
import graduateBack.sql as sql
import re

@app.route('/userInfo', methods=["POST"])
def userInfo():
    conn = sql.getConn()
    cur = sql.getCur(conn)
    res = {}
    id = request.form["id"]
    sql_word = "SELECT usertele,useremail FROM user WHERE id=%s"
    try:
        cur.execute(sql_word, id)
        results = cur.fetchone()
    except:
        res['result']="2"
        res['msg'] = "啊哦，数据库出错了"
        response = Response(json.dumps(res))
        sql.closeCur(cur, conn)
        return response
    else:
        res['result']="1"
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
    name = request.form["name"]
    # 0：中文名
    # 1：英文名
    # 2：格式错
    check=znORen(name)
    if check==2:
        res['result'] = "2"
        res['msg']="请输入正确的姓名"
        response = Response(json.dumps(res))
        return response
    check=checkInfoRight(tele,email)
    # 0：电话长度和邮箱都符合标准
    # 1：电话长度符合，但邮箱不是QQ或163
    # 2：电话长度符合，但邮箱格式不对
    # 3：电话长度不符，但邮箱符合标准
    # 4：电话长度不符，但邮箱不是QQ或163
    # 5：电话和邮箱都不符，
    if check==0:
        try: 
            sql_word = "UPDATE user SET usertele = %s ,useremail =%s ,userTrueName=%s WHERE id=%s"
            cur.execute(sql_word, [tele, email,name, id])
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

def znORen(string):
    # 检查整个字符串是否为中文或英文
    # :param string: 需要检查的字符串
    # :return: bool
    iszn=True
    isen=True
    for ch in string:
        if ch<u'\u4e00' or ch > u'\u9fff':
            iszn=False
    if not iszn:
        for en in string:
            if ord(en)<65 or 90<ord(en)<97 or ord(en)>122:
                isen=False
        if isen:
            return 1
        else:
            return 2
    else:
        return 0
    