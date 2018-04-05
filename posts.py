import os

from converter import convert


def get_posts():
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

    return posts


def get_post(permalink):
    for post in get_posts():
        if post["permalink"] == permalink:
            return post

    return None
