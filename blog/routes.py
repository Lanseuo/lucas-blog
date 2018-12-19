from flask import render_template, url_for, redirect, jsonify
from werkzeug.contrib.atom import AtomFeed

from . import app, meta
from .errors import PostNotFound
from .posts import Posts
from .post import Post


@app.route("/")
def index():
    return render_template(
        "index.html",
        site_title=meta.site_full_title,
        og={
            "title": meta.site_full_title,
            "description": meta.site_description,
            "image": url_for("static", filename="img/header.jpg"),
            "url": meta.site_url,
            "type": "blog"
        },
        seo_description=meta.site_description,
        header_title=meta.site_title,
        header_image=url_for("static", filename="img/header.jpg"),
        posts=Posts.get_posts()
    )


@app.route("/<string:permalink>")
def post(permalink):
    try:
        post = Post(permalink)
    except PostNotFound:
        return render_not_found()

    return render_template(
        "post.html",
        site_title=post.title + " | " + meta.site_title,
        og={
            "title": post.title + " | " + meta.site_title,
            "description": post.description,
            "image": meta.site_url + "/" + post.image,
            "url": meta.site_url + "/" + permalink,
            "type": "article"
        },
        seo_description=meta.site_description,
        header_title=post.title,
        header_text=post.readable_date,
        header_image=post.image,
        title=post.title,
        date=post.title,
        image=post.image,
        description=post.description,
        content=post.content
    )


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


@app.route("/feed")
def atom_feed():
    feed = AtomFeed(meta.site_title, feed_url=meta.site_url + "/feed")

    for post in Posts.get_posts():
        feed.add(
            title=post.title,
            title_type="text",
            subtitle=meta.site_subtitle,
            content=post.content,
            content_type="html",
            summary=post.description,
            summary_type="text",
            url=meta.site_url + "/" + post.permalink,
            author=meta.site_author,
            published=post.date,
            updated=post.date
        )

    return feed.get_response()


@app.route("/manifest.json")
def manifest_json():
    return app.send_static_file("manifest.json")


@app.route("/OneSignalSDKUpdaterWorker.js")
def one_signal_sdk_updater_worker_js():
    return app.send_static_file("js/OneSignalSDKUpdaterWorker.js")


@app.route("/OneSignalSDKWorker.js")
def one_signal_sdk_worker_js():
    return app.send_static_file("js/OneSignalSDKWorker.js")


@app.route("/<int:year>/<int:month>/<permalink>")
def wp_post_redirect(year, month, permalink):
    return redirect(url_for("post", permalink=permalink))


@app.route("/wp-content/uploads/<int:year>/<int:month>/<string:permalink>/<string:filename>")
def wp_media(year, month, permalink, filename):
    return app.send_static_file("posts/" + permalink + "/" + filename)


def render_not_found():
    return render_template(
        "index.html",
        site_title="404 | " + meta.site_title,
        og={
            "title": meta.site_full_title,
            "description": meta.site_description,
            "image": url_for("static", filename="img/404.jpg"),
            "url": meta.site_url,
            "type": "blog"
        },
        seo_description=meta.site_description,
        header_title="Seite nicht gefunden",
        header_image=url_for(
            "static", filename="img/404.jpg"),
        posts=Posts.get_posts()
    ), 404
