---
title: Alexa Skill entwickeln
image: amazon-alexa-entwickeln-lucas-hild.JPG
description: Für den Amazon Echo Dot lassen sich mit Hilfe von Flask-Ask eigene Skills entwickeln. Ich zeige dir, wie Du diese Alexa Skills mit Python erstellen kannst.
---

Der [Amazon Echo*](https://amzn.to/2Riy4HN) ist ein smarter Lautsprecher, den man über Sprachbefehle steuern kann. Von Haus aus hat Alexa, die Software, die hinter dem Echo steht, bereits viele Funktionen und Möglichkeiten. Jedoch kann man auch eigene Skills für Alexa bauen. Besonders faszinierend finde ich Alexa auch, da es nicht wirklich schwer ist, neue Skills hinzuzufügen. Für die Entwicklung eines Alexa Skills habe ich mich für die Library Flask-Ask entschieden, die in Python geschrieben ist.

Zuerst müssen wir uns überlegen, was unser Skill überhaupt können soll. Ich habe mich in diesem Tutorial für ein einfaches Spiel entschieden, bei dem man eine bestimmte Zahl erraten muss.

# Entwicklung

## Entwicklungsumgebung

Als erstes erstellen wir einen neuen Ordner und eine virtuelle Umgebung, in der wir alle Libraries installieren:

    mkdir memorygame
    cd memorygame
    virtualenv venv
    . venv/bin/activate
    pip3 install flask
    pip3 install flask_ask

## Grundgerüst von Flask-Ask

Nun können wir das Grundgerüst unserer Programmes schreiben. Dafür wird das Microframework Flask verwendet. Bei jedem Sprachbefehl, wird ein Request an den Flask-Webserver geschickt. In der Antwort steht dann der Text, den der Lautsprecher ausgeben soll.

from flask import Flask
from flask_ask import Ask, statement, question, session

    :::python
    app = Flask(__name__)
    ask = Ask(app, "/zahlenraten")

    # CODE

    if __name__ == "__main__":
        app.run(debug=True)

In diesem Schritt haben als erstes alle benötigten Libraries importiert. Im Weiteren haben wir eine neue Instanz der Klasse Flask und eine Instanz der Klasse Ask erstellt. Dabei haben wir den Parameter /zahlenfinden mitgegeben. Dies ist der Basispfad für unseren Alexa Skill. Dadurch wird es ermöglicht, dass man mehrere Skills auf einem Flask-Server hat.

## Launch

Nun kommen wir zur eigentlichen Entwicklung eines Skills. Wenn wir unseren Skill starten, wird als erstes die launch-Funktion ausgeführt:

    :::python
    @ask.launch
    def launch():
        return question("Hallo, bist Du bereit für ein Zahlenspiel?")

Die Funktion gibt eine einzelne Nachricht aus, die in der Funktion question steht. So weiß Alexa, dass es nach diesem Event noch weitergehen soll.

## Intents

Nun kann der Nutzer mit Ja oder mit Nein antworten. Dafür müssen wir unterhalb von dem Launch zwei Funktionen erstellen. Jede Funktion bekommt ein Intent zugewiesen. Dieses besagt, bei welcher Antwort die jeweilige Funktion ausgeführt wird. In der Library Flask-Ask werden dafür Python Decorators verwendet.

    :::python
    @ask.intent("YesIntent")
    def yes_intent():
        if not session.attributes.get("zufallszahl"):
            zufallszahl = random.randint(1, 100)
            print("Zufallszahl: {}".format(zufallszahl))
            session.attributes["zufallszahl"] = zufallszahl
        return question("Ich habe mir eine Zahl zwischen 1 und 100 überlegt. Du darfst raten!")


    @ask.intent("NoIntent")
    @ask.intent("AMAZON.StopIntent")
    def stop_intent():
        return statement("Bis zum nächsten Mal!")

In der Funktion yes_intent schauen wir als erstes, ob es für die aktuelle Session schon eine Zufallszahl gibt. In einer Session werden die Daten für einen Echo gespeichert. So vermeidet man, dass zwei Echos die gleiche Zahl haben. Im Weiteren wird dann eine neue Zufallszahl zwischen 1 und 100 gewählt.

Wenn der Nutzer jedoch Nein oder Stop sagt, wird die zweite Funktion aufgerufen und der Skill beendet.

## Überprüfen der Antwort

Im nächsten Schritt wird die Antwort überprüft.

    :::python
    @ask.intent("AnswerIntent", convert={"number": int})
    def answer_intent(number):
        if not session.attributes.get("zufallszahl"):
            zufallszahl = random.randint(1, 100)
            session.attributes["zufallszahl"] = zufallszahl

        if number == session.attributes["zufallszahl"]:
            session.attributes["zufallszahl"]
            return question("Herzlichen Glückwunsch! Du hast die richtige Zahl erraten. Möchtest Du noch eine Runde spielen?")
        elif number > session.attributes["zufallszahl"]:
            return question("Deine Zahl war zu groß! Rate noch einmal.")
        elif number < session.attributes["zufallszahl"]:
            return question("Deine Zahl war zu klein! Rate noch einmal")

Der Funktion answer_intent müssen wir den Parameter number mitgeben, in dem sich die Zahl befindet, die der Nutzer gesagt hat. Im Folgendem wird dann überprüft, ob die Zahl zu groß, zu klein oder richtig ist. Daraus wird eine Antwort generiert.

Der vollständige Code sieht dann wie folgt aus:

    :::python
    import random

    from flask import Flask
    from flask_ask import Ask, statement, question, session


    app = Flask(__name__)
    ask = Ask(app, "/zahlenraten")


    @ask.launch
    def launch():
        return question("Bist Du bereit für ein Zahlenspiel?")


    @ask.intent("YesIntent")
    def yes_intent():
        if not session.attributes.get("zufallszahl"):
            zufallszahl = random.randint(1, 100)
            print("Zufallszahl: {}".format(zufallszahl))
            session.attributes["zufallszahl"] = zufallszahl
        return question("Ich habe mir eine Zahl zwischen 1 und 100 überlegt. Du darfst raten!")


    @ask.intent("NoIntent")
    @ask.intent("AMAZON.StopIntent")
    def stop_intent():
        return statement("Bis zum nächsten Mal!")


    @ask.intent("AnswerIntent", convert={"number": int})
    def answer_intent(number):
        if not session.attributes.get("zufallszahl"):
            zufallszahl = random.randint(1, 100)
            session.attributes["zufallszahl"] = zufallszahl

        if number == session.attributes["zufallszahl"]:
            session.attributes["zufallszahl"]
            return question("Herzlichen Glückwunsch! Du hast die richtige Zahl erraten. Möchtest Du noch eine Runde spielen?")
        elif number > session.attributes["zufallszahl"]:
            return question("Deine Zahl war zu groß! Rate noch einmal.")
        elif number < session.attributes["zufallszahl"]:
            return question("Deine Zahl war zu klein! Rate noch einmal")


    if __name__ == "__main__":
        app.run(debug=True)

# Ausprobieren

## Ngrok

Nun wollen wir den Skill auch ausprobieren. Wie vorhin schon erklärt, läuft im Hintergrund von unserem Skill ein Webserver, der alle Anfragen mit Hilfe von Flask-Ask beantwortet. Um es etwas einfacher zu machen, können wir unseren Flask Webserver mit dem Tool Ngrok öffentlich machen. Wir bekommen eine öffentliche Domain, die wir später bei Amazon angeben müssen. Das Tool kann man sich auf der Webseite von Ngrok herunterladen.

    ./ngrok http 5000

Nun sehen wir ein Fenster mit unserer öffentlichen Domain. Dieses Fenster dürfen wir nicht schließen, da Amazon sonst keine Verbindung mehr mit unserem Webserver hat.


![Tunnel mit ngrok von Flask-Ask zu Amazon](ngrok-flask-ask.png)

## Amazon Developer Console

Damit dein Skill auf deinem Echo verfügbar wird, musst Du dich auf der Amazon Developer-Seite mit deinem Amazon-Konto anmelden. Es ist wichtig, dass dieses das gleiche ist, wie auf deinem Echo. Wenn Du dich angemeldet hast, klickst Du oben rechts auf Developer Console, auf Alexa und dann bei Alexa Skills Kit auf Get started. Nun klickst Du auf den Button „Add a New Task„. Im folgenden musst Du einige Informationen zu deinem Skill angeben. An einigen Stellen gibt es aber folgendes zu beachten:

Lasse den „*Skill Type*“ auf „*Custom Interaction Model*„.

![Amazon Developer Console](amazon-developer-console-skill.png)

Beim Bereich Intent Schema unter Interaction Model musst Du folgendes angeben:

    :::json
    {
      "intents": [
        {
          "intent": "YesIntent"
        },
        {
          "intent": "NoIntent"
        },
        {
          "intent": "AMAZON.StopIntent"
        },
        {
          "slots": [
            {
              "name": "number",
              "type": "AMAZON.NUMBER"
            }
          ],
          "intent": "AnswerIntent"
        }
      ]
    }

Etwas weiter unten bei Sample Utterances gibst Du folgendes an.

    YesIntent ja
    YesIntent sicherlich
    YesIntent warum nicht
    NoIntent nein
    AMAZON.StopIntent stop
    AnswerIntent {number}
    AnswerIntent Vielleicht {number}
    AnswerIntent Was ist mit {number}

Im Bereich *Configuration* wählst Du HTTPS aus und trägst als URL die Domain ein, die wir mit ngrok generiert haben. Vergiss aber den Basispfad nicht. Die URL könnte dann also wie folgt aussehen: https://123456789.ngrok.io/zahlenraten. Auch das HTTPS am Anfang ist wichtig. Die restlichen Einstellungen in diesem Tab lässt Du auf den Standardeinstellungen.

Schlussendlich wählst Du beim Tab *SSL* den zweiten Punkt aus (My development endpoint is a sub-domain of a domain that has a wildcard certificate from a certificate authority).

# Testen

Nun kannst Du deinen Skill testen. Dafür fragst Du deinen Echo (Dot), dass er deinen Skill öffnen soll. Wenn Du keinen Echo hast, kannst Du aber auch die Webseite EchoSim.io verwenden. Dort meldest Du dich an und dann kannst Du einen virtuellen Echo ausprobieren.

![Alexa Skill testen](echosim-skill-testen.png)

Ein Gespräch könnte wie folgst aussehen:

**Du**: Alexa, starte Zahlenspiel.  
**Alexa**: Bist Du bereit für ein Zahlenspiel?  
**Du**: Ja.  
**Alexa**: Ich habe mir eine Zahl zwischen 1 und 100 überlegt. Du darfst raten!  
**Du**: 50.  
**Alexa**: Deine Zahl war zu groß! Rate noch einmal.  
**Du**: Was ist mit 16?  
**Alexa**: Herzlichen Glückwunsch! Du hast die richtige Zahl erraten. Möchtest Du noch eine Runde spielen?
**Du**: Nein.    
**Alexa**: Bis zum nächsten Mal!

![Amazon Echo Dot mit Alexa](alexa-echo-dot-lucas-hild.JPG)


Nun hast Du Deinen ersten eigenen Alexa Skill für Deinen [Echo*](https://amzn.to/2Riy4HN) erstellt. In diesem Tutorial haben wir nur einen sehr einfachen Skill programmiert. Denkbar wären noch weitere Funktionen, wie zum Beispiel Highscores oder mehrere Schwierigkeitsstufen. Für weitere Informationen kann ich dir die Dokumentation von Flask-Ask und die offizielle Dokumentation von Amazon empfehlen.

> Welche Skills hast Du schon entwickelt oder möchtest Du noch bauen?
