from flask import Flask, request, Response, json, request, redirect, url_for
from graduateBack import app
import graduateBack.sql as sql
import os
from werkzeug.utils import secure_filename
from pypinyin import lazy_pinyin
import random, re

UPLOAD_FOLDER = '.\graduateBack\static\pdf'
ALLOWED_EXTENSIONS = {'txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'}
ALPHABET = 'abcdefghijklmnopqrstuvwxyz1234567890'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER


@app.route('/updataPDF', methods=["POST"])
def updataPDF():
    # check if the post request has the file part
    if 'file' not in request.files:
        res = {}
        res['result'] = 1
        res['msg'] = "表单中不存在文件部分"
        response = Response(json.dumps(res))
        return response
    file = request.files['file']
    # if user does not select file, browser also
    # submit an empty part without filename
    if file.filename == '':
        res = {}
        res['result'] = 1
        res['msg'] = "请上传文件"
        response = Response(json.dumps(res))
        return response
    if file and allowed_file(file.filename):
        if no_chinese(file.filename):
            filename = secure_filename(file.filename)
            if testexist(app.config['UPLOAD_FOLDER']+"\\"+filename):
                filename=changeFileName(filename)
        else:
            filename = secure_filename(''.join(lazy_pinyin(file.filename)))
            if testexist(app.config['UPLOAD_FOLDER']+"\\"+filename):
                filename=changeFileName(filename)
        file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
        url = "https://www.dddepg.top/graduate_back/static/pdf/" + filename
        res = {}
        res['result'] = 0
        res['url'] = url
        response = Response(json.dumps(res))
        return response
    res = {}
    res['result'] = 1
    res['msg'] = "你在干什么？？？？？？"
    response = Response(json.dumps(res))
    return response


def allowed_file(filename):
    return '.' in filename and filename.rsplit(
        '.', 1)[1].lower() in ALLOWED_EXTENSIONS


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



@app.route('/updataPDFtest', methods=["POST"])
def allowed_file_test():
    username = request.form["username"]
    name = '.' in username and username.rsplit(
        '.', 1)[1].lower() in ALLOWED_EXTENSIONS
    if no_chinese(username):
        filename = secure_filename(username)
    else:
        filename = secure_filename(''.join(lazy_pinyin(username)))
    # fn=secure_filename(username)
    res = {}
    res['result'] = name
    res['name'] = filename
    response = Response(json.dumps(res))
    return response