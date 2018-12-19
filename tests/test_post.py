import pytest
from pathlib import Path

from blog.post import Post


@pytest.fixture
def post():
    return Post("hallo-welt")


def test_get_markdown_file_path(post):
    file_path = post.get_markdown_file_path()
    assert isinstance(file_path, Path)
    assert file_path.name == "2016-07-04-hallo-welt.md"


def test_to_json(post):
    json = post.to_json()

    assert "title" in json.keys()
    assert "permalink" in json.keys()
    assert "date" in json.keys()
    assert "image" in json.keys()
    assert "description" in json.keys()
    assert "content" in json.keys()
