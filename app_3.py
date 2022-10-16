# 在雲端建立 帳號密碼 test
import pymongo
client= pymongo.MongoClient("mongodb+srv://root:root123@mycluster.cu0otrh.mongodb.net/?retryWrites=true&w=majority")
db=client.week4_member

# 初始化 Flask 伺服器
from flask import *
app=Flask(
    __name__,
    static_folder="static",
    static_url_path="/"
)
app.secret_key="any string but secret"
# 處理路由
@app.route("/")
def index():
    return render_template("index.html")

@app.route("/member")
def member():
    if "name" in session:
        return render_template("member_3.html")
    else:
        return redirect("/")

@app.route("/error")
def error():
    message=request.args.get("message","發生錯誤,請聯繫客服")
    return render_template("error.html",message=message)

@app.route("/signin",methods=["POST"])    
def signin():
    name=request.form["name"]
    password=request.form["password"]
    # 和資料庫做互動
    collection=db.users
    # 檢查帳號密碼是否正確
    result=collection.find_one({
        "$and":[
            {"name":name},
            {"password":password}
        ]
    })
    if name=="":
        return redirect("/error?message=請輸入帳號、密碼")
    if password=="":
        return redirect("/error?message=請輸入帳號、密碼")
    # 找不到對應的資料 登入失敗 導向到錯誤頁面
    if result==None:
        return redirect("/error?message=帳號或密碼輸入錯誤")
    session["name"]=result["name"]
    return redirect("/member")

@app.route("/signout")
def signout():
    # 移除session 中的會員資訊
    del session["name"]
    return redirect("/")

app.run(port=3000)