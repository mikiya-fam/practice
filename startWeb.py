# coding: utf-8
from flask import Flask, render_template,request

# Webサーバインスタンスの生成
app = Flask(__name__) 

# http://localhost:5000/にリクエストが来たときの処理
@app.route("/")
def index():
    return render_template('login.html')

@app.route("/test/", methods = ['POST','GET'])
def test():
    if request.method == 'GET':
        userId = request.args.get('userId', '')
        userPassword = request.args.get('userPassword', '')

    return render_template('schedule/scheduleTop.html',userId=userId,userPassword=userPassword)

@app.route("/edit/")
def edit():
    return render_template('schedule/scheduleEdit.html')

@app.route("/editComplete/", methods = ['POST','GET'])
def editComplete():
    if request.method == 'GET':
        time = request.args.get('time', '')
        eventName = request.args.get('eventName', '')
        place = request.args.get('place', '')
        comment = request.args.get('comment', '')
        participant = request.args.get('participant', '')

    return render_template('schedule/scheduleeditComplete.html',time=time,eventName=eventName,place=place,comment=comment,participant=participant)


if __name__ == "__main__":
    # webサーバーの立ち上げ
    app.run()