from flask import Flask,request,Response,json
from flask import render_template
import sql
from flask_cors import CORS,cross_origin
app = Flask(__name__)
cors = CORS(app)

@app.route('/')
def graduate():
    return app.send_static_file('index.html')

@app.route('/login', methods='POST')
def login():
    cur=sql.getCur()
    username=request.form["username"]
    password=request.form["password"]
    sql_word="SELECT userPassword FROM user WHERE userName=%s"
    cur.execute(sql_word,username)
    results = cur.fetchone()
    if(password==results[0]):
        res={}
        res['result']="1"
        response =Response(json.dumps(res))
        return response
    else:
        res={}
        res['data']="2"
        response =Response(json.dumps(res))
        return response
    

if __name__ == '__main__':
    app.run()