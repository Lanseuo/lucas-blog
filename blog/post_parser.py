import markdown
import re

from . import meta
from datetime import datetime


class PostParser:
    def __init__(self, markdown_file_path, permalink):
        self.markdown_file_path = markdown_file_path
        self.permalink = permalink

        self.parse_markdown()
        self.set_attributes()

    def extract_date(self, filename):
        raw_date = re.findall(r"\d\d\d\d-\d\d-\d\d", filename)[0]
        return datetime.strptime(raw_date, "%Y-%m-%d")

    def parse_markdown(self):
        markdown_data = markdown.Markdown(extensions=[
            "markdown.extensions.meta",
            "markdown.extensions.codehilite",
            "markdown.extensions.attr_list"
        ])

        file_content = self.read_file()

        self.html = markdown_data.convert(file_content)
        self.markdown_meta = markdown_data.Meta

    def read_file(self):
        with open(self.markdown_file_path, "r", encoding="utf-8") as f:
            return f.read()

    def set_attributes(self):
        self.title = self.markdown_meta["title"][0]
        self.date = self.extract_date(self.markdown_file_path.name)
        self.image = self.format_source_of_image(self.permalink, self.markdown_meta["image"][0])
        self.description = self.markdown_meta["description"][0]
        self.content = self.format_content(self.html)

    def format_source_of_image(self, permalink, source):
        return "/static/posts/{}/{}".format(permalink, source)

    def format_content(self, html):
        html = self.set_target_for_links(html)
        html = self.decrease_heading(html)
        html = self.format_images(html, self.permalink)
        return html

    def set_target_for_links(self, html):
        def replace(a):
            if "http" in a and meta.site_url not in a:
                href = re.match(r"<a href=\"([^\"]*)\">", a).group(1)
                return f'<a href="{href}" target="_blank">'

            else:
                return a

        return re.sub(r"<a href=\"([^\"]*)\">", lambda x: replace(x.group(0)), html)

    def decrease_heading(self, html):
        return html \
            .replace("<h5>", "<h6>").replace("</h5>", "</h6>") \
            .replace("<h4>", "<h5>").replace("</h4>", "</h5>") \
            .replace("<h3>", "<h4>").replace("</h3>", "</h4>") \
            .replace("<h2>", "<h3>").replace("</h2>", "</h3>") \
            .replace("<h1>", "<h2>").replace("</h1>", "</h2>")

    def format_images(self, html, permalink):
        """Fix source of image and add caption"""
        def replace(alt, source, permalink):
            is_external_source = "http" in source

            if is_external_source:
                link = source
            else:
                link = f"/static/posts/{permalink}/{source}"

            return f"""
                <figure class="img-wrapper">
                    <a href="{link}" target="_blank">
                        <img alt="{alt}" src="{link}"/>
                    </a>
                    <figcaption>{alt}</figcaption>
                </figure>
            """

        return re.sub(
            r"<p><img alt=\"([^\"]*)\" src=\"([^\"]*)\" /></p>",
            lambda x: replace(x.group(1), x.group(2), permalink),
            html
        )
