---
title: Flask auf dem Uberspace
image: article-image.png
description: Hier erfährst Du, wie Du mit Flask deine eigenen Webapplications erstellst und diese bei dem Hostinganbieter Uberspace veröffentlichst.
---

Flask ist ein, in Python geschriebenes, Webframework. Durch die einfache Erweiterbarkeit lassen sich mit ihm interaktive Webseite schnell erstellen. Aber auch APIs können mit dem Flask Framework erstellt werden. Bei meinem Lieblingshoster Uberspace gibt es die Möglichkeit Python laufen zu lassen. Außerdem habe ich es geschafft Webseiten mit Flask zu erstellen. Die Performance ist nicht die beste, aber die Kombination aus Flask und Uberspace kann für eine einfache Webapplication verwendet werden.

# Flask-Application

Als erstes loggen wir uns per SSH auf unserem Uberspace-Server ein. Als nächstes erstellen wir einen neuen Ordner mit dem Namen unserer Application im Homeverzeichnis und wechseln in den Ordner.

    mkdir flaskapplication
    cd flaskapplication

In diesem Ordner erstellen wir jetzt unserer Python Script:


    nano app.py

&zwj;
{: .break-code }

    :::python
    #!/usr/bin/env python3.6
    from flask import Flask

    app = Flask(__name__)

    @app.route("/")
    def index():
        return "Hello World from Uberspace and Flask!"

    if __name__ == "__main__":
        app.run()

# FCGI

Flask lassen wir auf unserem Uberspace mit FCGI (Fast Common Gateway Interface) laufen. Dafür müssen wir auch ein Script schreiben. Dieses liegt im Ordner *fcgi-bin* unter dem Homeverzeichnis.

    nano ~/fcgi-bin/flaskapplication.fcgi

&zwj;
{: .break-code }

    :::python
    #!/usr/bin/env python3.6

    import sys
    sys.path.insert(0, "/home/USERNAME/flaskapplication")
    from app import app

    from flup.server.fcgi_fork import WSGIServer
    WSGIServer(app).run()

Hierbei ersetzst Du *USERNAME* mit dem Username auf deinem Uberspace-Server und *flaskapplication* mit dem Ordner, indem Du *app.py* gespeichert hast.

# Module installieren

Damit die Webapplikation funktioniert, brauchst Du zwei Module: Flask und Flup6. Flup6 wird benötigt, um zwischen Flask und FCGI zu übersetzen.

    pip3 install flask --user
    pip3 install flup6 --user

# Überprüfen

Nun sollte deine Webseite unter *deinedomain.de/fcgi-bin/flaskapplication.fcgi* erreichbar sein. Falls Du Änderungen an deinen Dateien vornimmst, musst Du das Script neustarten. Dafür gibst Du folgenden Befehl ein:

    killall flaskapplication.fcgi

# Pfad verschönern

Wenn Du deine Flask-Webseite teilen möchtest, sieht der Domainpfad /fgci-bin/flaskkapplication.fcgi nicht wirklich schön aus. Deswegen kannst Du deinen Pfad mit der *.htaccess* Datei verschönern:

    nano ~/html/.htaccess

Hier definieren wir eine RewriteRule, die alle Anfragen auf deinen verschönerten Pfad auf /fcgi-bin/flaskapplication.fcgi umleiten:

    :::apache
    # Flask
    RewriteRule ^flaskapplication /fcgi-bin/flaskapplication.fcgi/ \[QSA,L\]
    RewriteRule ^flaskapplication/(.*)$ /fcgi-bin/flaskapplication.fcgi/$1 \[QSA,L\]

Nun sollte Flask unter *deinedomain.de/flaskapplication* abrufbar sein. Flask läuft zwar auf dem Uberspace nicht besonders schnell, zum Ausprobieren und für kleinere Projekte ist es aber geeignet. Wenn Du mehr über Flask lernen möchtest, kannst Du mit folgenden Tutorials lernen, wie man Webapplications mit Flask erstellt.

*   [Offizielles Tutorial](http://flask.pocoo.org/docs/0.12/tutorial/)
*   [Practical Flask Web Development Tutorials by Sentdex](https://www.youtube.com/playlist?list=PLQVvvaa0QuDc_owjTbIY4rbgXOFkUYOUB)
*   [The Flask Mega-Tutorial by Miguel Grinberg](https://blog.miguelgrinberg.com/post/the-flask-mega-tutorial-part-i-hello-world)

Viel Spaß beim Ausprobieren!
