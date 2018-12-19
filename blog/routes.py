from flask import render_template, url_for, redirect, jsonify
from werkzeug.contrib.atom import AtomFeed

from . import app
from .errors import PostNotFound
from .posts import Posts
from .post import Post


@app.route("/")
def index():
    return render_template(
        "index.html",
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
        posts=Posts.get_posts()
    )


@app.route("/<int:year>/<int:month>/<permalink>")
def wp_post_redirect(year, month, permalink):
    return redirect(url_for("post_view", permalink=permalink))


@app.route("/wp-content/uploads/<int:year>/<int:month>/<string:permalink>/<string:filename>")
def wp_media(year, month, permalink, filename):
    return app.send_static_file("posts/" + permalink + "/" + filename)


@app.route("/api/posts")
def api_posts():
    posts = [post.to_json() for post in Posts.get_posts()]
    return jsonify(posts)


@app.route("/api/posts/<string:permalink>")
def api_post(permalink):
    try:
        post = Post(permalink)
    except PostNotFound:
        return jsonify({"error": "post not found"}), 404

    return jsonify(post.to_json())


@app.route("/<string:permalink>")
def post_view(permalink):
    try:
        post = Post(permalink)
    except PostNotFound:
        return render_not_found()

    return render_template(
        "post.html",
        site_title=post.title + " | Lucas Blog",
        og={
            "title": post.title + "| Lucas Blog",
            "description": post.description,
            "image": "https://blog.lucas-hild.de" + post.image,
            "url": "https://blog.lucas-hild.de" + "/" + permalink,
            "type": "article"
        },
        seo_description="Auf dem Blog von Lucas Hild findest Du Artikel über Softwareentwicklung mit Python, JavaScript und dem Raspberry Pi",
        header_title=post.title,
        header_text=post.readable_date,
        header_image=post.image,
        title=post.title,
        date=post.title,
        image=post.image,
        description=post.description,
        content=post.content
    )


@app.route("/feed")
def atom_feed():
    feed = AtomFeed("Lucas Blog", feed_url="https://blog.lucas-hild.de/feed")

    for post in Posts.get_posts():
        feed.add(
            title=post.title,
            title_type="text",
            subtitle="Softwareentwicklung",
            content=post.content,
            content_type="html",
            summary=post.description,
            summary_type="text",
            url="https://blog.lucas-hild.de/" + post.permalink,
            author="Lucas Hild",
            published=post.date,
            updated=post.date
        )

    return feed.get_response()


@app.route("/impressum")
def imprint():
    return redirect("https://lucas-hild.de/imprint.html")


@app.route("/datenschutzerklaerung")
def privacy():
    return redirect("https://lucas-hild.de/privacy.html")


@app.route("/manifest.json")
def manifest_json():
    return app.send_static_file("manifest.json")


@app.route("/OneSignalSDKUpdaterWorker.js")
def one_signal_sdk_updater_worker_js():
    return app.send_static_file("js/OneSignalSDKUpdaterWorker.js")


@app.route("/OneSignalSDKWorker.js")
def one_signal_sdk_worker_js():
    return app.send_static_file("js/OneSignalSDKWorker.js")


def render_not_found():
    return render_template(
        "index.html",
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
        header_image=url_for(
            "static", filename="img/404.jpg"),
        posts=Posts.get_posts()
    ), 404
