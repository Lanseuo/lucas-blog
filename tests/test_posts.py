import random

from blog.post import Post
from blog.posts import Posts


def test_get_posts():
    posts = Posts.get_posts()

    for post in posts:
        assert isinstance(post, Post)


def test_get_posts_as_json():
    posts = Posts.get_posts_as_json()

    for post in posts:
        assert "title" in post.keys()
        assert "permalink" in post.keys()
        assert "date" in post.keys()
        assert "image" in post.keys()
        assert "description" in post.keys()
        assert "content" in post.keys()


def test_correct_order():
    posts = Posts.get_posts()

    copied_list = posts.copy()
    random.shuffle(copied_list)
    manually_sorted_posts = sorted(
        copied_list,
        key=lambda post: post.date
    )[::-1]

    assert posts == manually_sorted_posts
