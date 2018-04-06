---
title: Neuer Blog
image: zeitung-flask-blog.jpg
description: Ich habe mein eigenes Blogging-System in Flask entwickelt und stelle dir dieses in diesem Artikel vor.
---

Seit fast zwei Jahren existiert dieser Blog bereits. Über diese Zeit hinweg verwendete ich das CMS WordPress, um meine Artikel zu managen und zu schreiben. Besonders gut an WordPress gefällt mir, wie einfach es ist alles einzurichten und dass es so viele kostenlose Plugins und Themes gibt.

![Screenshot von der Startseite meines alten Blogs](alter-lucas-blog.png)

Über die letzten Jahre hat sich mein Blog jedoch verändert. Gestartet habe ich den Blog mit dem Thema "Fotografie und Technik". Jedoch schreibe ich mittlerweile lieber über Softwareentwicklung, die Fotografie und Technik (z. B. Smartphones etc.) sind da eher in den Hintergrund gerückt.

Was mich an WordPress gestört hat, war die für mich eingeschränkte Anpassbarkeit. Plugins müssen in PHP geschrieben werden, eine Programmiersprache, die mir persönlich nicht sonderlich gut gefällt. Damit wurde die Integration meines Newsletters ziemlich kompliziert. Auch das Theme meines Blogs fand ich nicht mehr optimal und es passte nicht zu meinem [Portfolio](https://lucas-hild.de). Selbstverständlich hätte ich auch mein eigenes WordPress-Theme schreiben können. Im Endeffekt habe ich mich jedoch dann anders entschieden.

![Screenshot von einem Artikel meines alten Blogs](artikel-hild.png)

Deswegen war es Zeit für eine Umstrukturierung. Dafür entwickelte ich eine [Flask App](/flask-uberspace), die jetzt für diesen Blog verwendet wird. Das Design orientiert sich an meinem Portfolio und die Artikelübersicht orientiert sich an dem alten Design.

# Artikel in Markdown

Die Artikel sind im Markdown-Format geschrieben und werden dann in HTML umgewandelt, damit sie auf der Webseite angezeigt werden können. Für die Umwandlung verwende ich die Library [Python Markdown](https://python-markdown.github.io/) und einige selbst geschriebene Regex (Reguläre Ausdrücke).

Dies erspart mir einiges an Zeit beim Schreiben der Artikel. Somit kann ich meine Artikel wie folgt schreiben:

	:::md
	# 2018-04-04-neuer-blog.md

	---
	title: Mein neuer Blog
	image: ...
	description: ...
	---
	
	normaler Text mit *kursiven* und **fett gedruckten** Wörter.
	
	# Überschrift 1
	## Überschrift 2
	### Überschrift 3
	
	[Link](https://blog.lucas-hild.de)
	
	![Bild](DSC_001.JPG)
	
		:::python
		print("Codebeispiel")
		
Die Bilder komprimiere ich mit der Library Pillow, damit die Ladezeit nicht allzu lang ist.

Wer sich für mein Blogging-System interessiert, findet hier den [Sourcecode](https://github.com/Lanseuo/lucas-blog).