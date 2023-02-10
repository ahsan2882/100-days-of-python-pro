from flask import Flask, render_template
import requests


app = Flask(__name__)
all_posts = requests.get("https://api.npoint.io/c790b4d5cab58020d391").json()


@app.route('/')
def home():
    return render_template("index.html", posts=all_posts)


@app.route('/post/<int:post_id>')
def get_post(post_id):
    requested_post = None
    for blog_post in all_posts:
        if blog_post["id"] == post_id:
            requested_post = blog_post
    return render_template("post.html", post=requested_post)


if __name__ == "__main__":
    app.run(debug=True)
