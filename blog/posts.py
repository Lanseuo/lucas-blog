import re

from . import top_level_path
from .post import Post


class Posts:
    @staticmethod
    def get_posts():
        posts_path = top_level_path / "posts"
        filenames = list(posts_path.iterdir())

        # Sort posts by date
        filenames.sort()

        posts = []

        for filename in filenames:
            permalink = re.sub(
                r"[-_\w/]*\d\d\d\d-\d\d-\d\d-([\w\d_-]*).md",
                lambda x: x.group(1),
                filename.name
            )

            post = Post(permalink)

            if post.is_published():
                posts.append(post)

        # Reverse order of posts, so that newest post is the first one
        posts = posts[::-1]

        return posts

    @staticmethod
    def get_posts_as_json():
        posts = Posts.get_posts()
        return [post.to_json() for post in posts]
