import psycopg2
import cgi

#値を受け取ってDBでやりとりする
#form_check = 0 #form_check を　0 としている
form = cgi.FieldStorage()
name = form.getvalue('name', '')
id = form.getvalue('id', '')

f = True

if name == '' or not str.isdecimal(id):
     f = False
else:
     id = int(id)

if f:
     #if "name" not in form or "id" not in form:
     #     form_check = 1 #　form_check は　１だお

     #データベース 接続
     conn = psycopg2.connect("dbname=chat user=postgres password=0415")
     print(conn.get_backend_pid())

     #カーソル取得
     cur = conn.cursor()

     #SELECT 文 の 実行
     cur.execute("select * from reg_user;")

     user = []
     for row in cur:
               user.append(row)

     for u in user:
          if name == u[1] or id == int(u[0]):
               f = False

if f:
     cur.execute("insert into reg_user (name, id) values ('{name}', {id});".format(name=name, id=id))
     conn.commit()

     print("Content-Type: text/html;")
     print("")
     print("""
<!DOCTYPE html>
<html lang="ja">
<head>
    <meta charset="UTF-8" />
    <title>ログイン画面</title>
</head>
<body>
<form action="/cgi-bin/login.py" method="post">
    お名前<input type="text" name="name" /><br />
    ID<input type="text" name="id" /><br />
    <input type="submit" value="ログイン" />
    <a href="/create.htm">作成</a>
</form>
</body>
</html>
""")

else:
     print("Content-Type: text/html;")
     print("")
     print("""
<!DOCTYPE html>
<html lang="ja">
    <head>
        <meta charset="UTF-8" />
        <title>作成画面</title>
    </head>
    <body>
        <form action="/cgi-bin/chat_system.py" method="post">
            お名前<input type="text" name="name" /><br />
            ID<input type="text" name="id" /><br />
            エラー
            <input type="submit" value="作成" />
            <input type="button" value="戻る" onclick="window.location='/login.htm'/>
        </form>
    </body>
     
</html>
""".format(name=name, id=id))

# cur.execute("delete from holiday where id = 11;")
# cur.execute("select * from holiday;")
# url = "http://localhost:8000/create.htm"



#結果 の 出力
# for row in cur:
#       print(row)

# print("Content-Type: text/html;")
# print("")
# print("""
# <!DOCTYPE html>
#      <html lang="ja">
#           <head>
#               <meta charset="UTF-8" />
#               <title>作成画面</title>
#           </head>
#                <body>
#                     <form action="/cgi-bin/chat_system.py" method="post">
#                         お名前<input type="text" name=""{name}"" /><br />
#                         ID<input type="text" name=""{id}"" /><br />
#
#                         <input type="submit" value="作成" />
#                         <input type="button" value="戻る" onclick="javascript:window.history.back(-1);return false;"/>
#                </form>
#           </body>
#      </html>
# """.format(name=name, id=id))
# print(name)
# print(id)