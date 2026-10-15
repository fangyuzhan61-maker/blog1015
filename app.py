from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# 部落格初始文章資料
posts = [
    {
        "title": "我的第一篇文章",
        "author": "Fang",
        "content": "這是我的第一篇部落格文章，歡迎來到我的網站！"
    },
    {
        "title": "學習 Python 的心得",
        "author": "Amy",
        "content": "Python 是一種容易入門且功能強大的程式語言。"
    }
]

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        # 從表單取得使用者輸入的資料
        new_title = request.form.get("title")
        new_author = request.form.get("author")
        new_content = request.form.get("content")

        # 確認都有填寫後，加到文章清單的最上方
        if new_title and new_author and new_content:
            posts.insert(0, {
                "title": new_title,
                "author": new_author,
                "content": new_content
            })
        
        # 重新整理回到首頁，防止重新整理網頁時重複送出表單
        return redirect(url_for("index"))

    return render_template("index.html", posts=posts)

import os

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)