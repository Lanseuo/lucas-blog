from werkzeug.contrib.atom import AtomFeed

from app import app
# from posts import get_posts
import posts


@app.route("/feed")
def atom_feed():
    feed = AtomFeed("Lucas Blog",
                    feed_url="https://blog.lucas-hild.de/feed")

    for post in posts.get_posts():
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
