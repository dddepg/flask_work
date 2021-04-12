from flask import Flask, request, Response, json
from graduateBack import app
import graduateBack.sql as sql
import re
from flask import render_template, send_file, send_from_directory, jsonify, make_response

@app.route('/downloadPDF/<file_name>', methods=["GET"])
def downloadPDF(file_name):
    try:
        directory = "C:\\Users\\Administrator\\Downloads\\flask_work\\graduateBack\\static\\pdf"
        response = make_response(
            send_from_directory(directory, file_name, as_attachment=True))
        return response
    except:
        response = make_response("<h1>该文件不存在或无法下载</h1>")
        return response

@app.route('/downloadword/<file_name>', methods=["GET"])
def downloadword(file_name):
    try:
        directory = "C:\\Users\\Administrator\\Downloads\\flask_work\\graduateBack\\static\\word"
        response = make_response(
            send_from_directory(directory, file_name, as_attachment=True))
        return response
    except:
        response = make_response("<h1>该文件不存在或无法下载</h1>")
        return response
