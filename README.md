# Lucas Blog

My markdown blogging system.

![](https://img.shields.io/badge/license-MIT-blue.svg?style=flat-square)

## Add new post

Create file *posts/yyyy-mm-dd-permalink.md*.

```markdown
---
title: TITLE
image: IMAGE
description: DESCRIPTION
---

normaler Text mit *kursiven* und **fett gedruckten** Wörter.

# Überschrift 1
## Überschrift 2
### Überschrift 3

[Link](https://blog.lucas-hild.de)

![Bild](DSC_001.JPG)

  :::python
  print("Codebeispiel")
```

Add images to *static/posts/permalink*.

Compress images before uploading them.

```
python3 compress_images.py
```

## Made with

- [Flask](http://flask.pocoo.org) - web framework
- [Python Markdown](https://python-markdown.github.io/) - convert markdown posts to HTML

## Meta

Lucas Hild - [https://lucas-hild.de](https://lucas-hild.de)  
This project is licensed under the MIT License - see the LICENSE file for details
