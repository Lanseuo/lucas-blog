import pytest
from datetime import datetime
from pathlib import Path

from blog.post_parser import PostParser


@pytest.fixture
def post_parser():
    return PostParser(
        Path("posts/2016-07-04-hallo-welt.md"),
        "hallo-welt"
    )


def test_extract_date(post_parser):
    date = post_parser.extract_date("2016-07-04-hallo-welt.md")
    assert date == datetime(2016, 7, 4)


def test_read_file(post_parser):
    file_content = post_parser.read_file()
    assert file_content.startswith("---\ntitle: ")
    assert file_content.endswith("free your data – host yourself\n")


def test_format_source_of_image(post_parser):
    source = post_parser.format_source_of_image("hallo-welt", "test.jpg")
    assert source == "/static/posts/hallo-welt/test.jpg"


def test_set_target_for_links(post_parser):
    html = "<a href=\"https://github.com\">GitHub</a>"
    result = post_parser.set_target_for_links(html)
    assert result == "<a href=\"https://github.com\" target=\"_blank\">GitHub</a>"

    html = "<a href=\"impressum\">Impressum</a>"
    result = post_parser.set_target_for_links(html)
    assert result == html

    html = "<p>Text</p>"
    result = post_parser.set_target_for_links(html)
    assert result == html


def test_decrease_heading(post_parser):
    result = post_parser.decrease_heading("<h1>Heading</h1>")
    assert result == "<h2>Heading</h2>"


def test_format_images(post_parser):
    html = "<p><img alt=\"Test\" src=\"https://via.placeholder.com/100\" /></p>"
    result = post_parser.format_images(html, "hallo-welt")
    assert "<figure class=\"img-wrapper\">" in result
    assert "<a href=\"https://via.placeholder.com/100\" target=\"_blank\">" in result
    assert "<img alt=\"Test\" src=\"https://via.placeholder.com/100\"/>" in result
