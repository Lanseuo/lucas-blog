---
title: Python auf dem ESP8266 (MicroPython)
image: DSC_0067.JPG
description: Der preiswerte NodeMCU ESP8266 lässt sich mit MicroPython programmieren. Somit kann man Sensoren über das Internet auslesen und Ausgabegeräte steuern.
---

Der [NodeMCU ESP8266*](https://amzn.to/2FbCewm) ist ein Microcontroller, der wirklich sehr preiswert ist. Auf ihm befindet sich ein WIFI-Chip und 30 GPIO-Ports, mit denen Hardware angesprochen werden kann. Durch seinen niedrigen Preis und den geringen Energieverbrauch, eignet er sich besonders gut für IoT (Internet of Things) Projekte. Man kann zum Beispiel einige Sensoren an den ESP8266 anschließen, die man dann über WIFI an das [SmartHome-System](https://blog.lucas-hild.de/2017/01/home-assistant-installieren/) überträgt. Oder man kann eine LED-Leiste anschließen, die man dann über das Smartphone steuern kann.

Eine Sache hat mich aber an dem NodeMCU gestört: Normalerweise muss die Software in Lua oder C geschrieben werden. Da ich aber ein absoluter Fan von Python bin, habe ich mich nach einer Lösung umgeschaut, wie man Python auf einem ESP8266 zum Laufen bekommt. Dabei stieß ich auf ein Projekt mit dem Namen [MicroPython](https://micropython.org/). Dies erlaubt es einem, Python für einen Microcontroller zu schreiben. MicroPython ist sehr ähnlich wie das normale CPython und im Großteil auch kompatibel. Trotzdem gibt es einige [kleine Unterschiede](http://docs.micropython.org/en/latest/esp8266/genrst/index.html) und leider können auch nur sehr wenige [Libraries](http://docs.micropython.org/en/latest/esp8266/library/index.html) importiert werden.

![NodeMCU ESP8266](DSC_0067.JPG)

# Installation von MicroPython

Als erstes öffnen wir unser Terminal, um ein Programm mit dem Namen esptool zu installieren. Mit ihm können wir die neue Firmware auf den Microcontroller flashen. Das Programm installieren wir mit pip:

    sudo pip3 install esptool

Als nächstes schließen wir den Chip über den MicroUSB-Port an den Computer an. Standardmäßig sollte er unter dem Port /dev/ttyUSB0 zu finden sein. Um den Speicher des Microcontrollers zu löschen, geben wir folgendes in das Terminal ein:

    esptool.py --port /dev/ttyUSB0 erase_flash

Als nächstes lädst Du dir die Firmware von MicroPython herunter. Diese findest Du auf der [Download-Seite von MicroPython](http://micropython.org/download#esp8266). Wähle hier die Version mit dem Namen *latest* aus und lade diese auf deinen Computer herunter. Nun wollen wir MicroPython auf unserem ESP8266 installieren. Bei dem folgenden Befehl, müssen wir noch den Dateiname von der Firmware, die wir gerade heruntergeladen, am Ende anpassen. Versuche es erst mit:

    esptool.py --port /dev/ttyUSB0 --baud 460800 write_flash --flash_size=detect 0 esp8266-20170108-v1.8.7.bin

Wenn das **nicht** geklappt hat, versuche es mit diesem Befehlt:

    esptool.py --port /dev/ttyUSB0 --baud 460800 write_flash --flash_size=detect -fm dio 0 esp8266-20170108-v1.8.7.bin

Wenn jetzt hier kein Fehler angezeigt wird, solltest Du mit MicroPython erfolgreich installiert haben. Falls es nicht geklappt hat, kannst Du mal auf [dieser Webseite](http://docs.micropython.org/en/latest/esp8266/esp8266/tutorial/intro.html#intro) vorbeischauen oder mir einen Kommentar schreiben.

# Python auf der Shell

Nachdem wir MicroPyton erfolgreich installiert haben, können wir Python interaktiv in der Shell ausprobieren:

    screen /dev/ttyUSB0 115200

Jetzt musst Du nur noch einige Male *Enter* und/oder *Strg + C* drücken und drei *>>>* sollten erscheinen. Nun kannst Du mit deinen ersten Zeilen Code beginnen:

    :::python
    >>> print("Hello World from MicroPython on ESP8266!")
    Hello World from MicroPyton on ESP8266!

Dieser Code wird direkt auf dem ESP8266 aufgeführt. Nun wollen wir eine LED an den NodeMCU anschließen. Dafür verbinden wir TX (GPIO1) mit einem 220Ω Widerstand. Daran kommt dann eine LED, die mit Ground verbunden ist:

![LED und Widerstand am NodeMCU](nodemcu_led.png)

Um den Ausgang des Microcontrollers zu steuern, brauchen wir folgenden Code:

    :::python
    >>> import machine
    >>> pin = machine.Pin(1, machine.Pin.OUT)
    >>> pin.high()
    >>> pin.low()

Damit solltest Du deine LED an- und auch wieder ausschalten können.

# Scripts speichern

Bis jetzt mussten wir jede Zeile Python Code einzeln eingeben. Wenn wir aber ein echtes Programm schreiben wollen, wäre das äußerst unpraktisch. Deswegen gibt es die Möglichkeit eine Datei mit dem Namen main.py auf das Filesystem zu spielen, die bei jedem Neustart ausgeführt wird. [Adafruit](https://adafruit.com) stellt ein Programm bereit, mit dem man auf dieses einfach Zugriff hat. [Ampy](https://github.com/adafruit/ampy) (Adafruit MicroPython tool) lässt sich, wie folgt, installieren:

    sudo pip3 install adafruit-ampy

Nun kannst Du ein einfaches Programm auf deinem Computer schreiben, das Du main.py nennst. Dieses Beispiel-Programm führt zwei verschiedene Animationen auf drei LEDs aus aus:

    :::python
    import machine
    import time

    ###
    # SETUP CODE
    ###

    yellow = machine.Pin(16, machine.Pin.OUT)
    white = machine.Pin(5, machine.Pin.OUT)
    red = machine.Pin(4, machine.Pin.OUT)
    pin_input = machine.Pin(12, machine.Pin.OUT)

    ###
    # LOOP CODE
    ###

    while True:
        # Animation 1
        for i in range(5):
            yellow.high()
            white.high()
            red.high()
            time.sleep(0.1)
            yellow.low()
            white.low()
            red.low()
            time.sleep(0.1)
            time.sleep(1)

        # Animation 2
        for i in range(5):
            yellow.high()
            time.sleep(0.1)
            white.high()
            time.sleep(0.1)
            red.high()
            time.sleep(0.1)
            yellow.low()
            time.sleep(0.1)
            white.low()
            time.sleep(0.1)
            red.low()
            time.sleep(0.1)


Mit dem folgenden Befehl speicherst Du das Script auf deinem NodeMCU:

    ampy --port /dev/ttyUSB0 put main.py

Jedes Mal, wenn Du den NodeMCU neustartest oder auf den Reset-Button klickst, wird das Programm jetzt ausgeführt.

![NodeMCU und Breadboard mit LEDs](DSC_0063.JPG)

# WLAN einrichten

Da sich auf dem NodeMCU ESP8266 ein WIFI-Chip befindet, lässt sich dieser auch ganz einfach mit MicroPython verwenden. Dafür gibt es zwei Möglichkeiten: Access Point oder Client. Um den NodeMCU als Access Point einzurichten, geht man wie folgt vor:

    :::python
    >>> import network
    >>> sta_if = network.WLAN(network.STA\_IF)
    >>> ap_if.ifconfig()

Nun kannst Du dich mit deinem Smartphone mit dem WIFI-Netzwerk des ESP8266 verbinden. Das Passwort lautet hierfür: *micropythoN*. Außerdem kann man den Chip aber auch nutzen, dass er sich mit dem eigenen Netzwerk (des Routers) verbindet:

    :::python
    >>> sta_if.active(True)
    >>> sta_if.connect('<your ESSID>', '<your password>')
    >>> sta_if.isconnected()
    >>> sta_if.ifconfig()

Nun könntest Du einen HTTP Webserver aufsetzen, über den Du deine Hardware steuerst. Meiner Meinung nach ist MicroPython ein richtig tolles Projekt. Ich werde in Zukunft noch einige Sensoren und Ausgabegeräte mit dem ESP8266 bauen, die ich auch in mein SmartHome-System einbinden werde. Wenn ihr Lust habt, könnt ihr euch einen [NodeMCU bestellen*](https://amzn.to/2FbCewm), auf dem ihr dann Python zum Laufen bringt. Viel Spaß!
