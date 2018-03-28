import markdown
import re


def convert_date(date):
    print(date)
    day = date.split("-")[2]

    if date.split("-")[1] == "01":
        month = "Januar"
    elif date.split("-")[1] == "02":
        month = "Februar"
    elif date.split("-")[1] == "03":
        month = "März"
    elif date.split("-")[1] == "04":
        month = "April"
    elif date.split("-")[1] == "05":
        month = "Mai"
    elif date.split("-")[1] == "06":
        month = "Juni"
    elif date.split("-")[1] == "07":
        month = "Juli"
    elif date.split("-")[1] == "08":
        month = "August"
    elif date.split("-")[1] == "09":
        month = "September"
    elif date.split("-")[1] == "10":
        month = "Oktober"
    elif date.split("-")[1] == "11":
        month = "November"
    elif date.split("-")[1] == "12":
        month = "Dezember"

    year = date.split("-")[0]

    return "{}. {} {}".format(day, month, year)


def replace_images(html, permalink):
    """Find all images and pass them to replace_images_sub"""
    return re.sub(r"<p><img alt=\"([\s\w]*)\" src=\"([\s\w:/\.-]*)\" /></p>",
                  lambda x: replace_images_sub(x.group(1), x.group(2), permalink),
                  html)
    return html


def replace_images_sub(alt, src, permalink):
    """Fix src of image and add caption"""
    # External src
    if "http" in src:
        return """<figure class="img-wrapper">
    <a href="{src}" target="_blank">
        <img alt="{alt}" src="{src}" />
    </a>
    <figcaption>{alt}</figcaption>
</figure>""".format(alt=alt, src=src)
    # Internal src
    else:
        return """<figure class="img-wrapper">
    <a href="/static/posts/{permalink}/{src}" target="_blank">
        <img alt="{alt}" src="/static/posts/{permalink}/{src}" />
    </a>
    <figcaption>{alt}</figcaption>
</figure>""".format(alt=alt, src=src, permalink=permalink)


def convert(filename):
    """Convert markdown to html"""
    with open(filename, "r") as f:
        markdown_file = f.read()

    # Convert markdown to html
    md = markdown.Markdown(extensions=["markdown.extensions.meta"])
    html = md.convert(markdown_file)

    # Get permalink from filename (e. g. 2018-03-28-bitwarden-passwort-manager.md)
    #                                               ^                        ^
    permalink = re.sub(r"[-_\w/]*\d\d\d\d-\d\d-\d\d-([\w\d_-]*).md",
                       lambda x: x.group(1), filename)

    result = {
        "title": md.Meta["title"][0],
        "date": convert_date(md.Meta["date"][0]),
        "content": replace_images(html, permalink=permalink),
        "image": md.Meta["image"][0],
        "description": md.Meta["description"][0]
    }

    return result
