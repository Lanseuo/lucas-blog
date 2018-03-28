import os
from flask import Flask, render_template, redirect, url_for
from livereload import Server

from converter import convert

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/<string:permalink>")
def post(permalink):
    current_path = os.path.dirname(os.path.realpath(__file__))
    all_files = os.listdir(current_path + "/posts")

    # If post doesn't exist
    if not list(filter(lambda x: permalink in x, all_files)):
        return redirect(url_for("index"))

    file_name = list(filter(lambda x: permalink in x, all_files))[0]
    file = current_path + "/posts/" + file_name
    post_details = convert(file)

    print(post_details)

    return render_template("post.html",
                           title=post_details["title"],
                           content=post_details["content"])


if __name__ == "__main__":
    app.debug = True
    server = Server(app.wsgi_app)
    server.serve()
