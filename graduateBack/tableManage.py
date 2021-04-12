from flask import Flask, request, Response, json
from flask import render_template
from werkzeug.utils import secure_filename
from graduateBack import app
from pypinyin import lazy_pinyin
import graduateBack.sql as sql
import graduateBack.docxManage as docx
import re, random
import time
import traceback

WORD_FOLDER = '.\graduateBack\static\word'
ALPHABET = '1234567890'
app.config['WORD_FOLDER'] = WORD_FOLDER


@app.route('/creatTable', methods=["POST"])
def creatTable():
    conn = sql.getConn()
    cur = sql.getCur(conn)
    res = {}
    thetabletitle = request.form["thetabletitle"]
    ownerid = request.form["ownerid"]
    id = time.strftime("%m%d%S", time.localtime()) + "" + ownerid
    date = time.strftime("%Y-%m-%d", time.localtime())
    if no_chinese(thetabletitle):
        filename = secure_filename(thetabletitle)
        while testexist(app.config['WORD_FOLDER'] + "\\" + filename):
            filename = changeFileName(filename)
    else:
        filename = secure_filename(''.join(lazy_pinyin(thetabletitle)))
        while testexist(app.config['WORD_FOLDER'] + "\\" + filename):
            filename = changeFileName(filename)
    url = "https://www.dddepg.top/graduate_back/static/word/" + filename
    try:
        sql_word = "INSERT INTO thetable(idthetable,thetabletitle,\
            thetablcreatdate,thetableurl,ownerid)\
             VALUES (%s,%s,%s,%s,%s)"

        cur.execute(sql_word,
                    [int(id), thetabletitle, date, url,
                     int(ownerid)])
    except Exception as e:
        res['result'] = "1"
        res['msg'] = "啊哦，数据库出错了"
        res["info"] = str(e)
        response = Response(json.dumps(res))
        sql.closeCur(cur, conn)
        return response
    else:
        res['result'] = "0"
        res['id'] = id
        res['filename'] = filename
        response = Response(json.dumps(res))
        sql.closeCur(cur, conn)
        return response


def no_chinese(string):
    # 检查整个字符串是否包含中文
    # :param string: 需要检查的字符串
    # :return: bool
    for ch in string:
        if u'\u4e00' <= ch <= u'\u9fff':
            return False
    return True


def testexist(filepath):
    # 检查文件是否存在，以防止重名
    try:
        f = open(filepath)
        f.close()
    except IOError:
        return False
    else:
        return True


def changeFileName(filenaem):
    rest = re.split(r'(.*)\.(.*)', filenaem)
    newname = rest[1] + random.choice(ALPHABET) + "." + rest[2]
    return newname


@app.route('/TablefirstDate', methods=["POST"])
def TablefirstDate():
    conn = sql.getConn()
    cur = sql.getCur(conn)
    res = {}
    xueke = request.form["xueke"]
    id = request.form["id"]
    xiangmu = request.form["xiangmu"]
    ketiming = request.form["ketiming"]
    shenqingname = request.form["shenqingname"]
    rest = re.split(r'(.*)-(.*)-(.*)T', request.form["tianbaodate"])
    tianbaodate = rest[1] + "年" + rest[2] + "月" + rest[3] + "日"
    try:
        sql_word = "INSERT  INTO type1table(thetableid,xueke,\
            xiangmu,ketiming,shenqingname,tianbaodate)\
             VALUES (%s,%s,%s,%s,%s,%s) "

        cur.execute(sql_word,
                    [id, xueke, xiangmu, ketiming, shenqingname, tianbaodate])
    except Exception as e:
        res['result'] = "1"
        res['msg'] = "啊哦，数据库出错了"
        res["info"] = str(e)
        response = Response(json.dumps(res))
        sql.closeCur(cur, conn)
        return response
    else:
        res['result'] = "0"
        res['msg'] = "success"
        response = Response(json.dumps(res))
        sql.closeCur(cur, conn)
        return response


@app.route('/TableSecondDate', methods=["POST"])
def TableSecondDate():
    conn = sql.getConn()
    cur = sql.getCur(conn)
    res = {}
    rest = re.split(r'(.*)-(.*)-(.*)T', request.form["jihuawanchengshijian"])
    jihuawanchengshijian = rest[1] + "年" + rest[2] + "月" + rest[3] + "日"
    if (request.form["sfgat"] == "1"):
        gst = "是"
    else:
        gst = "否"
    try:
        sql_word = "UPDATE type1table SET ketiming2=%s,guanjianci=%s,xiangmuleibie=%s,xuekefenlei=%s,yanjiuleixing=%s,\
                    ketifuzeren=%s,xingbie=%s,mingzu=%s,chushengri=%s,xingzhengzhiwu=%s,zhuanyezhicheng=%s,yanjiuzhuanchang=%s,\
                    zuihouxueli=%s,zuihouxuewei=%s,danrendaoshi=%s,suozaisheng1=%s,suozaisheng2=%s,suoshuxitong1=%s,suoshuxitong2=%s,\
                    gongzuodanwei=%s,lianxidianhua=%s,shengfenzheng1=%s,sfzhm=%s,sfgat=%s,yuqicg=%s,yuqizs=%s,sqjfei=%s,\
                    jihuawanchengshijian=%s WHERE thetableid=%s"

        cur.execute(sql_word, [
            request.form["ketiming2"], request.form["guanjianci"],
            request.form["xiangmuleibie"], request.form["xuekefenlei"],
            request.form["yanjiuleixing"], request.form["ketifuzeren"],
            request.form["xingbie"], request.form["mingzu"],
            request.form["chushengri"], request.form["xingzhengzhiwu"],
            request.form["zhuanyezhicheng"], request.form["yanjiuzhuanchang"],
            request.form["zuihouxueli"], request.form["zuihouxuewei"],
            request.form["danrendaoshi"], request.form["suozaisheng1"],
            request.form["suozaisheng2"], request.form["suoshuxitong1"],
            request.form["suoshuxitong2"], request.form["gongzuodanwei"],
            request.form["lianxidianhua"], request.form["shengfenzheng1"],
            request.form["sfzhm"], gst, request.form["yuqicg"],
            request.form["yuqizs"], request.form["sqjfei"],
            jihuawanchengshijian, request.form["id"]
        ])
    except Exception as e:
        res['result'] = "1"
        res['msg'] = "啊哦，数据库出错了"
        res["info"] = str(e)
        res["where"] = traceback.format_exc()
        response = Response(json.dumps(res))
        sql.closeCur(cur, conn)
        return response
    else:
        res['result'] = "0"
        res['msg'] = "success"
        response = Response(json.dumps(res))
        sql.closeCur(cur, conn)
        return response


@app.route('/TableLastDate', methods=["POST"])
def TableLastDate():
    conn = sql.getConn()
    cur = sql.getCur(conn)
    res = {}
    try:
        sql_word = "UPDATE type1table SET ketishejilunzheng=%s,yanjiujichu=%s WHERE thetableid=%s "
        cur.execute(sql_word, [
            request.form["ketishejilunzheng"], request.form["yanjiujichu"],
            request.form["id"]
        ])
    except:
        res['result'] = "1"
        res['msg'] = "啊哦，数据库出错了"
        response = Response(json.dumps(res))
        sql.closeCur(cur, conn)
        return response
    else:
        res['result'] = "0"
        res['msg'] = "success"
        response = Response(json.dumps(res))
        sql.closeCur(cur, conn)
        docx.creatTable(request.form["id"], request.form["name"])
        return response


@app.route('/DropRow', methods=["POST"])
def DropRow():
    conn = sql.getConn()
    cur = sql.getCur(conn)
    res = {}
    try:
        sql_word = "DELETE FROM thetable WHERE idthetable=%s "
        cur.execute(sql_word, [request.form["id"]])
        sql_word2 = "DELETE FROM type1table WHERE thetableid=%s "
        cur.execute(sql_word2, [request.form["id"]])
    except:
        res['result'] = "1"
        res['msg'] = "啊哦，数据库出错了"
        response = Response(json.dumps(res))
        sql.closeCur(cur, conn)
        return response
    else:
        res['result'] = "0"
        res['msg'] = "success"
        response = Response(json.dumps(res))
        sql.closeCur(cur, conn)
        return response



@app.route('/getMyTable', methods=["POST"])
def getMyTable():
    conn = sql.getConn()
    cur = sql.getCur(conn)
    id= request.form["id"]
    try:
        sql_word = "SELECT * FROM thetable where ownerid=%s"
        cur.execute(sql_word,id)
        results = cur.fetchall()
        res = {}
        reslist = list()
        for row in results:
            res["id"] = row[0]
            res["title"] = row[1]
            res["date"] = row[2]
            res["url"] = row[3]
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