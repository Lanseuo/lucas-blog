---
title: Home Assistant installieren
image: DSC_0007.JPG
description: Hier zeige ich Dir, wie Du die Heimautomatisierungs-Software Home Assistant auf deinem Raspberry Pi installierst und einrichtest.
---

[Home Assistant](https://home-assistant.io/) ist eine relative junge Heimautomatisierungs-Software, die in Python geschrieben wurde. Das ganze Projekt ist open-source und lässt sich mit dem Raspberry Pi als Basis schnell und einfach installieren. Der Raspberry Pi eignet sich besonders gut für ein Heimautomatisierungsprojekt, da er nicht viel Strom verbraucht, wenn er durchgehend läuft und man Hardware-Komponente einfach über die GPIO-Ports anschließen kann. Die Software hat eine breite Basis an [Komponenten](https://home-assistant.io/components/) und unterstützt die wichtigsten Protokolle und Schnittstellen. Außerdem gibt es eine schicke Weboberfläche, die auch nach den eigenen Wünschen angepasst werden kann. Ich verwende für dieses Projekt den Raspberry Pi 3 Model B und Home Assistant in der Version 0.35.

# Image aufsetzen

Home Assistant läuft ganz normal auf Raspian Jessie. Als erstes lädst Du dir das Image von der [offiziellen Raspberry Pi Downloadseite](https://www.raspberrypi.org/downloads/raspbian/) herunter. Dieses schreibst Du mit einem Programm (z. B Win32 Disk Imager) oder per Terminal auf deine SD-Karte. Um SSH auf dem Raspberry Pi zu aktivieren, musst Du noch eine leere Datei mit dem Namen "*SSH*" (ohne Dateiendung) in das *boot*-Verzeichnis schreiben. Nun kannst Du deinen Raspberry Pi mit einem Ethernet-Kabel und einem Netzteil verbinden. Per SSH wählst Du dich jetzt auf deinem Raspberry Pi ein. Unter Linux gibst Du einfach in das Terminal folgenden Befehl ein:

    ssh pi@raspberrypi

Unter Windows brauchst Du das Programm *Putty*. Der Hostname ist raspberrypi und der Benutzername *pi*. In beiden Fällen gibst Du als Passwort "*raspberry*" ein. Nun gibst Du in das Terminal folgenden Befehl ein, um zur Konfiguration zu gelangen:

    sudo raspi-config

Hier wählst Du (mit Pfeiltasten und Enter) den ersten Punkt "*Expand Filesystem*" aus, um das Betriebssystem an die Größe deiner microSD-Karte anzupassen. Nun änderst Du noch dein Passwort, die Uhrzeit (*Europe / Berlin*) und kannst wahlweise den Hostname unter "*Advanced*" ändern. Nun verlässt Du die Einstellungen wieder und startest deinen Raspberry Pi neu. Um dein System auf den neusten Stand zu bringen, gibst Du folgende Befehle ein:

    sudo apt-get update
    sudo apt-get upgrade

Dies kann einige Zeit beanspruchen.

# Home Assistant installieren

Um Home Assistant herunterzuladen und zu installieren, gibst Du folgenden Befehl ein:

    wget -Nnv https://raw.githubusercontent.com/home-assistant/fabric-home-assistant/master/hass\_rpi\_installer.sh && chown pi:pi hass\_rpi\_installer.sh && bash hass\_rpi\_installer.sh

Dieser Vorgang wird um die zwanzig Minuten dauern. Zwischendurch wirst Du nach deinem Passwort gefragt, welches Du vorhin festgelegt hast. Dieses wird gebraucht um deinen Raspbery Pi neuzustarten. Wenn der Vorgang abgeschlossen ist, sollte Home Assistant installiert sein. Dies kannst Du überprüfen, indem Du die Weboberfläche mit dem Browser deiner Wahl öffnest. Der Link dazu lautet *hostname:8123*, wobei Du hostname durch den Hostnamen deines Raspberry Pi ersetzt. Außerdem kannst Du zu dieser Oberfläche auch mit der IP-Adresse gelangen: *192.168.178.73:8123* (Beispiel). Dort solltest Du die Weboberfläche von Home Assistant zu Gesicht bekommen.

![Weboberfläche](weboberflaeche.png)

# Erstes Modul hinzufügen

Für Home Assistant gibt es viele verschiedene Module. Mit einem ganz einfachen kannst Du die [CPU Geschwindigkeit](https://home-assistant.io/components/sensor.cpuspeed/) deines Raspberry Pis herausfinden. Dafür öffnest Du die Konfigurationsdatei "*configuration.yaml*" von Home Assistant:

    sudo nano /home/homeassistant/.homeassistant/configuration.yaml

Hier schreibst Du folgende Zeilen hinein:

    sensor:
      - platform: cpuspeed

Wichtig ist hierbei, dass eine Einrückung genau zwei Leerzeichen breit ist. Nun öffnest Du wieder die Weboberfläche. Bevor die Änderung sichtbar wird, musst Du Home Assistant neu starten. Dafür gehst Du unten links bei "Developer Tools" auf das erste Symbol. Als Domain wählst Du "*homeassistant*" aus und als Service wählst Du "*restart*". Um Home Assistant jetzt neuzustarten, gehst Du auf "*Call Service*". Nun musst Du 5 Sekunden warten und kannst dann die Seite neuladen.

![Home Assistant neustarten](restart.png)

## Fehlerbehebung

Sollte nach mehrfachem Neuladen, die Seite immer noch nicht wieder da sein, musst Du nach einem Fehler in deiner Konfiguration suchen. Dafür gibst Du folgenden Befehl in das Terminal ein:

    sudo cat /home/homeassistant/.homeassistant/home-assistant.log

Hier sollte Dir dann dein Fehler angezeigt werden. Wenn Du den Fehler behoben hast, musst du Home Assistant per Hand neustarten:

    sudo systemctl restart home-assistant.service

Meinung nach ist Home Assistant ein tolles System. Ich werde in den nächsten Wochen und Monaten anfangen einige Geräte aus unserem Haushalt einzubinden. Mit Home Assistant sind auch komplexe Automatisierungen möglich. Wenn Du mehr über Home Assistant und seine Konfiguration erfahren möchtest, kann ich Dir die [offizielle Dokumentation](https://home-assistant.io/getting-started) empfehlen.

> Welche smarten Geräte hast Du schon in deinem Haushalt und welche Automatisierungen würdest Du mit Home Assistant durchführen?
