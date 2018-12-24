import os
from PIL import Image

from blog import top_level_path

post_folders = [
    folder for folder in (top_level_path / "blog/static/posts").iterdir()
]

for folder in post_folders:
    images_in_post_folder = [
        image for image in folder.iterdir()
        if image.name.lower().endswith((".jpg", ".png"))
    ]

    for image in images_in_post_folder:
        if os.stat(image).st_size > 2000000:
            print(image)
            img = Image.open(image)
            img.save(image, quality="web_low", optimize=True)
