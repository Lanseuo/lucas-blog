import os
from flask import Flask, render_template, redirect, url_for
from livereload import Server

from converter import convert

app = Flask(__name__)


@app.route("/")
def index():
    current_path = os.path.dirname(os.path.realpath(__file__))
    all_files = os.listdir(current_path + "/posts")

    # Sort posts by date
    all_files.sort()

    posts = []

    for file_name in all_files:
        file_path = current_path + "/posts/" + file_name
        posts.append(convert(file_path))

    # Reverse order of posts, so that newest post is the first one
    posts = posts[::-1]

    return render_template("index.html",
                           site_title="Lucas Blog - Softwareentwicklung",
                           og={
                               "title": "Lucas Blog - Softwareentwicklung",
                               "description": "Auf dem Blog von Lucas Hild findest Du Artikel über Softwareentwicklung mit Python, JavaScript und dem Raspberry Pi",
                               "image": "https://images.pexels.com/photos/270373/pexels-photo-270373.jpeg",
                               "url": "https://blog.lucas-hild.de",
                               "type": "blog"
                           },
                           seo_description="Auf dem Blog von Lucas Hild findest Du Artikel über Softwareentwicklung mit Python, JavaScript und dem Raspberry Pi",
                           header_title="Lucas Blog",
                           header_image="https://images.pexels.com/photos/270373/pexels-photo-270373.jpeg",
                           posts=posts)


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
                                   site_title=post_details["title"] + "| Lucas Blog",
                                   og={
                                       "title": post_details["title"] + "| Lucas Blog",
                                       "description": post_details["description"],
                                       "image": "https://blog.lucas-hild.de" + post_details["image"],
                                       "url": "https://blog.lucas-hild.de" + "/" + permalink,
                                       "type": "article"
                                   },
                                   seo_description="Auf dem Blog von Lucas Hild findest Du Artikel über Softwareentwicklung mit Python, JavaScript und dem Raspberry Pi",
                                   header_title=post_details["title"],
                                   header_text=post_details["date"],
                                   header_image=post_details["image"],
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
