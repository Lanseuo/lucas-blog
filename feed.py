import os
from werkzeug.contrib.atom import AtomFeed

from app import app
from converter import convert


@app.route("/feed")
def atom_feed():
    feed = AtomFeed("Lucas Blog",
                    feed_url="https://blog.lucas-hild.de/feed")

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

    for post in posts:
        feed.add(
            title=post["title"],
            title_type="text",
            subtitle="Softwareentwicklung",
            content=post["content"],
            content_type="html",
            summary=post["description"],
            summary_type="text",
            url="https://blog.lucas-hild.de/" + post["permalink"],
            author="Lucas Hild",
            published=post["date_time"],
            updated=post["date_time"]
        )

    return feed.get_response()
