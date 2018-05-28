import markdown
import re
from datetime import datetime

import app


def convert_date(date):
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
    return re.sub(r"<p><img alt=\"([^\"]*)\" src=\"([^\"]*)\" /></p>",
                  lambda x: replace_images_sub(
                      x.group(1), x.group(2), permalink),
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


def decrease_heading(html):
    return html.replace("<h5>", "<h6>").replace("</h5>", "</h6>") \
        .replace("<h4>", "<h5>").replace("</h4>", "</h5>") \
        .replace("<h3>", "<h4>").replace("</h3>", "</h4>") \
        .replace("<h2>", "<h3>").replace("</h2>", "</h3>") \
        .replace("<h1>", "<h2>").replace("</h1>", "</h2>") \



def fix_src_of_img(src, permalink):
    return "/static/posts/{}/{}".format(permalink, src)


def target_blank_for_external_links(html):
    """Find all links and pass them to target_blank_for_external_links_sub"""
    return re.sub(r"<a href=\"([^\"]*)\">",
                  lambda x: target_blank_for_external_links_sub(x.group(0)),
                  html)
    return html


def target_blank_for_external_links_sub(a):
    if "http" in a and "https://blog.lucas-hild.de" not in a:
        href = re.match(r"<a href=\"([^\"]*)\">", a).group(1)
        return "<a href=\"{}\" target=\"_blank\">".format(href)
    else:
        return a


def convert(filename):
    """Convert markdown to html"""
    with open(filename, "r", encoding="utf-8") as f:
        markdown_file = f.read()

    # Convert markdown to html
    md = markdown.Markdown(extensions=["markdown.extensions.meta",
                                       "markdown.extensions.codehilite",
                                       "markdown.extensions.attr_list"])
    html = md.convert(markdown_file)

    # Parse permalink out of filename
    # (e. g. 2018-03-28-bitwarden-passwort-manager.md)
    #                   ^                        ^
    permalink = re.sub(r"[-_\w/]*\d\d\d\d-\d\d-\d\d-([\w\d_-]*).md",
                       lambda x: x.group(1), filename)

    # Parse date out of filename
    date = re.findall("\d\d\d\d-\d\d-\d\d", filename)[0]

    html = target_blank_for_external_links(html)
    html = decrease_heading(html)
    html = replace_images(html, permalink=permalink)

    result = {
        "title": md.Meta["title"][0],
        "permalink": permalink,
        "date": convert_date(date),
        "date_time": datetime.strptime(date, "%Y-%m-%d"),
        "image": fix_src_of_img(md.Meta["image"][0], permalink),
        "description": md.Meta["description"][0],
        "content": html
    }

    is_date_in_future = datetime.now().timestamp() - \
        result["date_time"].timestamp() < 0
    if not is_date_in_future or (is_date_in_future and app.app.debug):
        return result
    else:
        return None
