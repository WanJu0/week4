# 在雲端建立 帳號密碼 test
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

app.run(port=3000)