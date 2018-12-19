from datetime import datetime

from . import top_level_path
from .errors import PostNotFound
from .post_parser import PostParser


class Post:
    def __init__(self, permalink):
        self.permalink = permalink

        markdown_file_path = self.get_markdown_file_path()

        post_parser = PostParser(markdown_file_path, permalink)

        self.title = post_parser.title
        self.date = post_parser.date
        self.readable_date = self.get_readable_date()
        self.image = post_parser.image
        self.description = post_parser.description
        self.content = post_parser.content

    def get_markdown_file_path(self):
        posts_folder = top_level_path / "posts"

        for markdown_file in posts_folder.iterdir():
            permalink_of_file = markdown_file.name[11:-3]

            if permalink_of_file == self.permalink:
                return markdown_file

        raise PostNotFound

    def to_json(self):
        return {
            "title": self.title,
            "permalink": self.permalink,
            "date": self.date,
            "image": self.image,
            "description": self.description,
            "content": self.content
        }

    def is_published(self):
        return datetime.now() > self.date

    def get_readable_date(self):
        months = ["Januar", "Februar", "März", "April", "Mai", "Juni",
                  "Juli", "August", "September", "Oktober", "November", "Dezember"]

        day = self.date.day
        month = months[self.date.month - 1]
        year = self.date.year

        return "{}. {} {}".format(day, month, year)

    def __lt__(self, other):
        return self.date > other.date
