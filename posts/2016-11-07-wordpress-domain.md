---
title: Wordpress auf einer Domain
image: wordpress-923188_960_720.jpg
description: Hier erkläre ich dir, wie Du Wordpress mit einer .tk-Domain einrichtet. Dafür verwenden wir freenom zur Domainregistrierung und Hostinger als Webhoster.
---

> Leider bin ich nicht mehr mit Hostinger zufrieden. Diese Webseite hoste ich mittlerweile bei [Uberspace](https://blog.lucas-hild.de/2017/03/uberspace/).

In dieser Anleitung erkläre ich dir, wie Du dir eine Domain erstellst und bei einem Hosting-Anbieter Wordpress installierst. Dafür verwende ich eine kostenlose .tk-Domain und den kostenlosen Hosting-Anbieter [Hostinger](http://hostinger.de). Für diese Anleitung brauchst Du keinerlei Vorkenntnisse.

# Domain registrieren

Als erstes gehst Du auf die Webseite [freenom.com](http://www.freenom.com/). Auf dieser Webseite kannst Du ersteinmal die Domain deiner Wahl auf ihre Verfügbarkeit überprüfen. Du kannst zwischen den Domainendungen .tk, .ml, .ga, .cf oder .gq entscheiden. Auf der nächsten Seite klickst Du auf "Use DNS" und als Unterpunkt wählst Du "Use your own DNS". Dabei trägst Du den Nameserver und die IP-Adresse ein, wie auf dem Screenshot. Wichtig ist es, dass du bei "Period" die Auswahlmöglichkeit "12 Months @ Free" auswählst. Nach 12 Monaten wird deine Domain nichts kosten, sondern Du musst die Domain einfach nur erneuern. Nach einem Klick auf Weiter musst Du dir noch einen Account erstellen. Alternativ kannst Du dich auch mit Google+ o. ä. anmelden.

![Nameserver](01.png)

*Zeile 1: Nameserver: ns1.hostinger.de IP address: 31.170.163.241, Zeile 2: Nameserver: ns2.hostinger.de IP address: 31.220.23.1*

# Hosting einrichten

[Hostinger](http://api.hostinger.de/redir/17957423) ist eine Webseite, die kostenloses Hosting anbietet. Hierbei erhaltet ihr 2GB Speicherplatz, PHP, MySQL und selbstverständlich auch eine Mail-Verwaltung kostenlos. Zudem kommt der Anbieter aus Deutschland. Nun erstellst Du dir einen Account auf der Webseite [hostinger.de](http://api.hostinger.de/redir/17957423), indem du bei "Kostenloses Hosting" auf "Jetzt bestellen!" klickst (Trotzdem ist das Angebot kostenlos). Jetzt musst Du dir hier einen Account anlegen. Nach einer erfolgreichen Registrierung, geht es weiter. Nun wählst Du als Domain Typ "Domain" aus. Im Feld "Domain" trägst Du deine Domain ein, die Du bei Freenom eingerichtet hast. Nun wählst Du noch ein Passwort, für deine Webseite aus. Dieses Passwort sollte ein anderes sein, als das für die Registrierung. Auf der nächsten Seite musst Du noch einen Grund angeben weshalb Du dir einen Account erstellt hast. Dies ist nötig, da Hostinger Spam-Versuche vermeiden möchte.

![Hosting einrichten](02.png)

Jetzt kommst Du auf das Dashboard (auch Cpanel genannt), deiner Domain. Dieses kannst Du mit [cpanel.hostinger.de](http://cpanel.hostinger.de) aufrufen. Nun gehst Du auf den Menüpunkt Dankenbanken > MySQL Datenbanken. Hier musst Du dir eine Datenbank erstellen, da ohne diese Wordpress nicht funktionieren wird. Der Dankenbankenname und der Benutzername sollten einige zufällige Buchstaben und Zahlen sein (z. B u\*\*\*\*\*\*\*\*\*\_ui45 und u\*\*\*\*\*\*\*\*\*\_er8). Schreibe dir diese Daten am besten auf. Du hast jetzt 4 verschiedene Passwörter: FreeNom-Account, Hostinger-Account, Hostinger-Webseite und das Passwort der MySQL-Datenbank.

# Wordpress hochladen

Nun gehst Du auf die deutsche [Wordpress Webseite](https://de.wordpress.org/). Hier kannst Du dir die aktuelle Wordpress-Version herunterladen. Diese entpackst Du. Jetzt brauchst Du das Programm FileZilla, welches Du dir unter Windows auf der offiziellen Webseite herunterlädst oder unter Linux / Debian aus den offiziellen Paketquellen installierst (sudo apt-get install filezilla). Unter Windows muss das Programm noch installiert werden. Mit FileZilla wirst Du später deine Webseite per FTP hochladen. Wenn Du FileZilla geöffnet hast, gehst Du oben links auf das Symbol für den SiteManager. Hier klickst Du auf "New Site". Die Daten entnimmst Du aus dem folgendem Bild. Das Passwort ist das Passwort deiner Webseite.

![FTP-Daten](03.png)

*Host: ftp.deinedomain.tk Port: 21 Login Type: Normal User: u... Password: p...*

Nun musst Du noch auch "Connect" klicken und die Sicherheitsmeldung bestätigen. Im linken Teil des Fensters hast Du deine lokalen Dateien auf deinem Computer. Rechts sind die Daten deiner Webseite. Nun navigierst du auf der linken Seite in den Downloadverzeichnis indem sich der entpackte Ordner mit dem Namen "wordpress" befindet. Diesen öffnest Du. In dem Ordner befinden sich weitere Ordner (z. B. wp-admin, wp-content ...) und einige Dateien (z. B. index.php, wp-active ...). Nun markierst Du all diese Dateien (und Ordner) und schiebst diese mit gedrückter Maustaste in das rechte Feld.

![Hochladen der Dateien](04.png)

Dies kann je nach Internetverbindung bis zu 10 Minuten dauern.

# Wordpress einrichten

Als nächstes beginnst Du mit der Einrichtung deiner Webseite. Diese rufst in deinem Webbrowser mit deinedomain.tk auf. Hier gehst du mit einem Klick auf "Los geht's" zum ersten Schritt deiner Einrichtung. Die Daten trägst Du so ein, wie Du sie bei der Einrichtung der MySQL-Datenbank angegeben hast. Als Datenbank-Host verwendest Du "mysql.hostinger.de" und als Tabellen-Präfix verwendest Du wieder eine Buchstaben, Zahlenfolge (z. B ae4_). Diese muss aber mit einem Unterstrich enden. Nun wählst Du den Titel deiner Webseite und ein Passwort. Jetzt kannst Du deine Seite installieren. Deine Webseite ist jetzt fertig eingerichtet. Du solltest sie unter deinedomain.tk aufrufen können. Wenn Du sie bearbeiten möchtest, gehst Du auf deinedomain.tk/wp-admin.

![Einrichtung von Wordpress](05.png)

Nun kannst Du mit der Gestaltung deiner Wordpress-Webseite beginnen. Wenn Du wissen möchtest, mit welchen Plugins Wordpress noch besser wird, kannst Du dir meinen [Artikel über meine Lieblings Wordpress-Plugins](/wordpress-plugins) anschauen.
