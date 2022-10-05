from flask import Flask, render_template

app = Flask(__name__)


@app.route("/<username>")
def hello_world(username=None):
    return render_template('./index.html', name=username)


@app.route("/blog")
def blog():
    return "<h1>Blog Chu!</h1>"
