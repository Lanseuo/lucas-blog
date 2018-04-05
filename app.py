from flask import Flask, jsonify, render_template, redirect, url_for
from livereload import Server

from posts import get_posts, get_post

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html",
                           site_title="Lucas Blog - Softwareentwicklung",
                           og={
                               "title": "Lucas Blog - Softwareentwicklung",
                               "description": "Auf dem Blog von Lucas Hild findest Du Artikel über Softwareentwicklung mit Python, JavaScript und dem Raspberry Pi",
                               "image": url_for("static", filename="img/header.jpg"),
                               "url": "https://blog.lucas-hild.de",
                               "type": "blog"
                           },
                           seo_description="Auf dem Blog von Lucas Hild findest Du Artikel über Softwareentwicklung mit Python, JavaScript und dem Raspberry Pi",
                           header_title="Lucas Blog",
                           header_image=url_for("static", filename="img/header.jpg"),
                           posts=get_posts())


@app.route("/<int:year>/<int:month>/<permalink>")
def wp_post(year, month, permalink):
    return redirect(url_for("post", permalink=permalink))


@app.route("/wp-content/uploads/<int:year>/<int:month>/<string:permalink>/<string:filename>")
def wp_media(year, month, permalink, filename):
    return app.send_static_file("posts/" + permalink + "/" + filename)


@app.route("/api/posts")
def api_posts():
    return jsonify(get_posts())


@app.route("/api/posts/<string:permalink>")
def api_post(permalink):
    post_details = get_post(permalink)
    if post_details:
        return jsonify(post_details)
    else:
        return jsonify({}), 404


@app.route("/<string:permalink>")
def post(permalink):
    post_details = get_post(permalink)

    if post_details:
        return render_template("post.html",
                               site_title=post_details["title"] + " | Lucas Blog",
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
    else:
        return render_template("index.html",
                               site_title="404 | Lucas Blog",
                               og={
                                   "title": "Lucas Blog - Softwareentwicklung",
                                   "description": "Auf dem Blog von Lucas Hild findest Du Artikel über Softwareentwicklung mit Python, JavaScript und dem Raspberry Pi",
                                   "image": url_for("static", filename="img/404.jpg"),
                                   "url": "https://blog.lucas-hild.de",
                                   "type": "blog"
                               },
                               seo_description="Auf dem Blog von Lucas Hild findest Du Artikel über Softwareentwicklung mit Python, JavaScript und dem Raspberry Pi",
                               header_title="Seite nicht gefunden",
                               header_image=url_for("static", filename="img/404.jpg"),
                               posts=get_posts()), 404


from feed import *

if __name__ == "__main__":
    app.debug = True
    server = Server(app.wsgi_app)
    server.serve(host="0.0.0.0")
