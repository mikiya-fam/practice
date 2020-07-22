import mysql.connector

#DB接続情報
def conn_db():
      conn = mysql.connector.connect(
              host = 'localhost',      #localhostでもOK
              user = 'root',
              passwd = 'root',
              db = 'mikiya'
      )
      return conn
