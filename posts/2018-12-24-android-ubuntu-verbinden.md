---
title: Android Smartphone mit Ubuntu verbinden
image: android-ubuntu.JPG
description: Du möchtest Android mit Ubuntu verbinden, um Dateien zu übertragen, Android Benachrichtigungen zu sehen und Deine Zwischenablage synchronisieren zu lassen? So geht's!
---

Eine Sache, die mir am Apple's Ecosystem sehr gut gefällt, ist die "Continuity". Apple verbindet verschiedene Geräte (Mac und iPhone) und lässt einen die Arbeit auf einem Gerät beginnen und auf einem anderen fortführen. Wen nervt es nicht, sich dauernd Nachrichten zwischen Geräten hin und herzuschicken, um beispielsweise ein Passwort nicht abtippen zu müssen oder Dateien auf beiden Geräten zu haben?

Vor einigen Wochen habe ich die GNOME Shell Erweiterung **GSConnect** entdeckt. Mit dieser kann man von seinen Linux Computer, beispielsweise mit Ubuntu 18.04, mit seinem Android Smartphone verbinden. GSConnect macht es sehr einfach und komfortabel, Dateien zu übertragen, Notifications auf beiden Geräten zu bekommen oder den Computer mit dem Smartphone zu steuern. Und das beste ist, das ganze funktioniert ohne USB-Kabel. Die einzige Voraussetzung ist, dass die beiden Geräte sich im selben Netzwerk befinden.

# GSConnect unter Ubuntu installieren

Als erstes erkläre ich Dir, wie Du dieses Feature überhaupt nutzen kannst.

## KDE Connect auf dem Android Smartphone installieren

Als erstes musst Du Dir dafür die *KDE Connect* App auf deinem Smartphone installieren. Diese App findest Du im [Google Play Store](https://play.google.com/store/apps/details?id=org.kde.kdeconnect_tp) oder auch bei [F-Droid](https://f-droid.org/packages/org.kde.kdeconnect_tp).

![Die KDE Connect App gibt es im Play Store](play-store-kde-connect.JPG)

## GSConnect installieren

Die GSConnect Erweiterung findest Du im [Store von GNOME](https://extensions.gnome.org/extension/1319/gsconnect). Von dort kannst Du die Erweiterung direkt über den Browser installieren.

![GSConnect in GNOME Extension Shop](gsconnect-gnome-extension.png)

## Geräte verbinden

Wenn die Erweiterung und die App installiert sind, kannst Du die beiden Geräte verbinden.

Dafür öffnest Du die *KDE Connect* App auf deinem Smartphone. Dort findest Du eine Liste mit verfügbaren Geräten. Wähle hier deinen Computer aus und klicke auf den "Request Pairing" Button.

Auf dem Computer musst Du diese Anfrage nur noch akzeptieren. Schon hast Du deine beiden Geräte miteinander verbunden.

Du solltest nun Dein Smartphone im Statusmenü auf deinem Computer finden. Dort kannst Du den Akkustand deines Smartphones überprüfen, das Geräte klingeln lassen oder es stumm schalten.

![](status-menu.png)

# Funktionen

GSConnect hat viele Funktionen. Einige davon möchte ich Dir hier kurz vorstellen. 

## Smartphone als Maus verwenden

In der *KDE Connect* App findest Du den Punkt **Remote Input**. Damit kannst Du den Mauszeiger auf deinem Computer komfortabel bewegen. Zusätzlich kann man auch die Tastatur des Smartphones verwenden, um Eingaben auf dem Computer zu machen.

![](remote-input-mouse.gif)

Außerdem kann man über den Menüpunkt **Remote control** die Medienwiedergabe und über den Punkt **Presentation remote** eine Präsentation vom Smartphone aus steuern.

## Dateien übertragen

GSConnect macht es auch einfach, Dateien zu übertragen. Das funktioniert sowohl vom Computer aufs Smartphone als auch andersherum. Dafür kann man im Dateiexplorer, in meinem Fall *Nautilus*, mit einem Rechtsklick auf eine Datei diese aufs Smartphone übertragen. Vom Android Smartphone kann man Dateien übertragen, indem man die Datei mit *KDE Connect* teilt. Zu finden sind die Dateien dann jeweils im Downloadsordner.

![Datei mit Nautilus vom Computer aufs Smartphone übertragen](transfer-nautilus.png)

## Zwischenablage synchronisieren

Das Feature, das ich am meisten nutze, ist die Synchronisierung der Zwischenablage. Kopierten Text kann man so auf dem anderen Gerät sofort wieder einfügen. Funktionieren tut es in beide Richtungen.

Jedoch muss dieses Feature erst in den Ubuntu-Einstellungen aktiviert werden.

![](clipboard-sync.png)

## Weitere Funktionen

- Über die Statusleiste kann vom Computer aus auch auf das Dateisystem vom Android Smartphone zugegriffen werden.
- Wenn man das Smartphone einmal nicht findet, kann über den Computer einen lauten Ton auf dem Smartphone abspielen, zumindest wenn es in Reichweite ist.
- Auch SMS Nachrichten können über GSConnect verschickt und gelesen werden.
- Smartphone Benachrichtigungen werden, wenn das Gerät verbunden ist, im Benachrichtigungszentrum auf dem Computer angezeigt.


Meiner Meinung nach ist GSConnect ist der **einfachste und komfortabelste Weg**, um sein Android Smartphone mit Ubuntu zu verbinden. Wenn trotzdem irgendetwas nicht funktioniert, empfehle ich Dir auf der [GitHub-Seite des Projektes](https://github.com/andyholmes/gnome-shell-extension-gsconnect) vorbeizuschauen.