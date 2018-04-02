---
title: Bitwarden - Passwort Manager
image: bitwarden-lucas-blog.jpg
description: Mit dem Passwort-Manager Bitwarden ist es einfach alle seine Passwörter sicher zu verwalten. Dafür gibt es Client für alle gängigen Platformen.
---

Bis vor einigen Wochen habe ich noch alle meine Passwörter per Hand aufgeschrieben. Da mir das aber zu umständlich und unübersichtlich geworden ist, habe ich mich auf die Suche nach einer digitalen Lösung begeben. Dabei bin ich auf viele kommerzielle Anbieter gestoßen, aber auch der Open Source PasswortManager bitwarden ist mir dabei über den Weg gelaufen. In diesem Artikel möchte ich euch diesen Passwort-Manager einmal genauer vorstellen.

# Das Projekt

Das Projekt bitwarden hat im November 2015 angefangen. Die erste Version wurde knapp ein Jahr später veröffentlicht. Im November 2016 wurde dann eine Kickstarter Kampagne für das Projekt gestartet. Ziel war es, $49.000 zu sammeln. Leider scheiterte das Projekt mit $7.016 von 285 Unterstützern. Trotzdem wurde das Projekt nicht aufgegeben. Mittlerweile wurden weitere Browser-Plugins, auto-fill für Android und Desktop Anwendungen für Linux, macOS und Windows entwickelt. Außerdem gibt es seit Januar 2018 auch Funktionen speziell für Unternehmen.

Besonders beeindruckend an dem Projekt finde ich, dass das ganze Projekt von nur einem einzigen Entwickler programmiert wird. Kyle Spearrin ist der Gründer und Entwickler von bitwarden. Er arbeite davor viele Jahre als Senior Software Architect im Bereich Finanzen.

![Weboberfläche](passwort-manager-bitwarden.png)

# Funktionen

Die Webseite von bitwarden lässt sich ziemlich leicht bedienen. Um Passwörter zu speichern, erstellt man für jede Webseite einen neuen Eintrag. Dieser kann in verschiedene Ordner einsortiert werden. In einem Eintrag können neben URL, Benutzername, Passwort und Authenticator Token, auch noch weitere Notizen und individuelle Felder gespeichert werden. Ein Passwort-Generator steht auch bereit. Was mir auch gut gefällt, ist das zu jeder Webseite automatisch ein Favicon (Logo) angezeigt wird.

![Eintrag bei bitwarden](eintrag-passwort-screenshot.png)

Bitwarden bietet verschiedene Clients an, um auf seine Passwörter zuzugreifen. Zum einem gibt es die Webseite, die unter [vault.bitwarden.com](https://vault.bitwarden.com) erreichbar ist. Außerdem gibt, es für die gängigsten Browser (Firefox, Chrome, Safari, Opera, Edge, Brave und Vivaldi) Erweiterungen. Diese unterstützen auch auto-fill-in. Mobile Apps gibt es für Android und iOS. Praktisch ist, dass wenn man mit dem Smartphone in Chrome auf einer Webseite ist, man über einen Tipp in den Benachrichtigungen auch automatisch das Passwort und den Benutzernamen einfüllen lassen kann.

![](devices-lucas-hild.png)

Wer Benutzeraccounts in einer Gruppe teilen und verwalten möchte, der kann Organisationen erstellen, mit denen Passwörter einfach ausgetauscht werden können.

# Sicherheit

Der wichtigste Punkt bei einem Passwort-Manager ist auf jeden Fall die Sicherheit. Alle Daten werden verschlüsselt bevor sie das Gerät verlassen. So hast nur Du Zugriff auf deine Passwörter. Die Daten werden mit AES-256 bit Verschlüsselung, Hashing mit Salts und PBKDF2 SHA-256 verschlüsselt. Die bitwarden Server werden in der Microsoft Azure Cloud gehostet und verwaltet.

Um deine Passwörter abzurufen, benötigst Du ein Master-Passwort. Dieses wählst Du am Anfang bei der Registrierung. Jedoch solltest Du es auf keinen Fall vergessen, da es nicht wiederherstellbar ist.

Bei der Vergabe des Passwortes, herrscht oft der Irrtum, dass dieses Groß- und Kleinbuchstaben, Zahlen und Sonderzeichen enthalten muss. Besser ist es jedoch ein „Passsatz“, statt ein Passwort zu verwenden. Zum Beispiel: *IchSchreibeGerneArtikelAufMeinemBlog*. Um solch ein „Passsatz“ zu knacken bräuchten Hacker eine Ewigkeit (genau genommen beim obigen Beispiel: 6.763254537723109e+44 Jahre). Der Vorteil davon ist auch noch, dass es viel leicht ist, sich einen Satz zu merken, als ein kryptisches Wort.

Wer bitwarden trotzdem nicht vertraut, kann sich den Passwort-Manager auch auf dem eigenen Server zuhause hosten. Eine Anleitung findest Du [hier](https://help.bitwarden.com/article/install-on-premise/).

![Sicherheit steht bei bitwarden an erster Stelle](bitwarden-deutsch.png)

Für mich hat sich der Umstieg von einem Zettel zu einem digitalen Passwort-Manager sehr gelohnt. Schaut euch gerne einmal bitwarden an.

> Welchen Passwort-Manager verwendest Du?
