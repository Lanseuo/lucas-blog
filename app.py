import os
from flask import Flask, render_template, redirect, url_for
from livereload import Server

from converter import convert

app = Flask(__name__)


@app.route("/")
def index():
    current_path = os.path.dirname(os.path.realpath(__file__))
    all_files = os.listdir(current_path + "/posts")

    posts = []

    for file_name in all_files:
        file_path = current_path + "/posts/" + file_name
        posts.append(convert(file_path))

    # Order posts by date
    posts = posts[::-1]

    return render_template("index.html", posts=posts)


@app.route("/<string:permalink>")
def post(permalink):
    current_path = os.path.dirname(os.path.realpath(__file__))
    all_files = os.listdir(current_path + "/posts")

    # Find file
    for file_name in all_files:
        if file_name[11:-3] == permalink:
            file_path = current_path + "/posts/" + file_name
            post_details = convert(file_path)

            return render_template("post.html",
                                   title=post_details["title"],
                                   date=post_details["title"],
                                   image=post_details["image"],
                                   description=post_details["description"],
                                   content=post_details["content"])

    # No file was found
    return redirect(url_for("index"))


if __name__ == "__main__":
    app.debug = True
    server = Server(app.wsgi_app)
    server.serve()
