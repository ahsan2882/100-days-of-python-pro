from flask import Flask, render_template
import requests


app = Flask(__name__)


@app.route('/')
def home():
    response = requests.get("https://api.npoint.io/c790b4d5cab58020d391")
    posts = response.json()
    return render_template("index.html", posts=posts)


@app.route('/post/<int:post_id>')
def get_post(post_id):
    response = requests.get("https://api.npoint.io/c790b4d5cab58020d391")
    posts = response.json()
    requested_post = None
    for blog_post in posts:
        if blog_post["id"] == post_id:
            requested_post = blog_post
    return render_template("post.html", post=requested_post)


@app.route('/about')
def go_to_about():
    return render_template("about.html")


@app.route('/contact')
def go_to_contact():
    return render_template("contact.html")


if __name__ == "__main__":
    app.run(debug=True)
