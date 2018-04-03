import os
from PIL import Image


post_folders = [
    os.path.dirname(os.path.realpath(__file__)) + "/static/posts/" + folder
    for folder
    in os.listdir(
        os.path.dirname(os.path.realpath(__file__)) + "/static/posts"
    )
]

for folder in post_folders:
    images_in_post_folder = [
        folder + "/" + image
        for image
        in os.listdir(folder)
        if image.lower().endswith((".jpg", ".png"))
    ]

    for image in images_in_post_folder:
        if os.stat(image).st_size > 2000000:
            print(image)
            img = Image.open(image)
            img.save(image, quality="web_low", optimize=True)
