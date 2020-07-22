# coding: utf-8
from flask import Flask, render_template,request
import mysql.connector

# Webサーバインスタンスの生成
app = Flask(__name__) 

#DB接続情報
def conn_db():
      conn = mysql.connector.connect(
              host = 'localhost',      #localhostでもOK
              user = 'root',
              passwd = 'root',
              db = 'mikiya'
      )
      return conn

# http://localhost:5000/にリクエストが来たときの処理
@app.route("/")
def index():
    return render_template('login.html')

@app.route("/test/", methods = ['POST'])
def test():
        userId = request.form["userId"]
        userPassword = request.form["userPassword"]
        print(userId)
        print(userPassword)
        # #DB接続インスタンス
        conn = conn_db()
        # # カーソルを取得
        cursor = conn.cursor()
        # ログイン処理（入力されたユーザIDとパスワードの組み合わせのデータが存在するか）
        # cursor.execute("SELECT * FROM T_MEMBER where user_Id='uycep2ed' and Password='tsuka0807'")
        cursor.execute("SELECT * FROM T_MEMBER WHERE USER_ID = %(user_id)s AND PASSWORD = %(password)s", {'user_id': userId, 'password': userPassword})

        # # データが0件の場合、ログイン画面へ
        print(cursor.fetchall())
        print(cursor.rowcount)
        if cursor.rowcount == 0:
           return render_template('login.html')
        # ログイン結果がOKの場合、スケジュールトップへ
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

# 新規登録画面初期表示処理
@app.route('/userRegistCommit/', methods=['POST'])
def userRegistCommitAction():
    # 入力値を取得する
    # 姓
    lastName = request.form["lastName"]
    # 名
    firstName = request.form["firstName"]
    # 名
    sex = request.form["sex"]
    # ユーザID
    userId = request.form["userId"]
    # パスワード
    password = request.form["password"]
    # 登録日時
    createdDate = datetime.datetime.now()
    # 更新日時
    updatedDate = datetime.datetime.now()
    # 削除フラグ
    deleteFlag = "0"

    #DB接続インスタンス
    conn = conn_db()
    # カーソルを取得
    cursor = conn.cursor()
    # 登録処理
    cursor.execute("INSERT INTO T_MEMBER (LAST_NAME, FIRST_NAME, SEX, USER_ID, PASSWORD, CREATED_DATE, UPDATED_DATE, DELETE_FLAG ) VALUES (%(lastName)s, %(firstName)s, %(sex)s, %(userId)s, %(password)s, %(createdDate)s, %(updatedDate)s, %(deleteFlag)s)"
    , {'lastName': lastName, 'firstName': firstName, 'sex': sex, 'userId': userId, 'password': password, 'createdDate': createdDate, 'updatedDate': updatedDate, 'deleteFlag': deleteFlag})
    conn.commit()
    # 登録完了画面を表示する
    return render_template('user/userRegistComplete.html')
#############ユーザ関連#############


if __name__ == "__main__":
    # webサーバーの立ち上げ
    app.run()