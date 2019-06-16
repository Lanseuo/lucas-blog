---
title: LineageOS installieren
image: DSC_0481.JPG
description: LineageOS ist eine offene Alternative zum normalen Android. In dieser Anleitung zeige ich dir Schritt für Schritt, wie Du die CustomROM installieren kannst.
---

Seit einigen Monaten ist mein Smartphone schon sehr langsam. Deswegen habe ich mich nach einem alternativen Betriebssystem umgesehen. Dabei fiel mir natürlich als erstes Lineage OS ein. Dies ist eine freie CustomROM für Android-Geräte. LineageOS gefällt mir besonders gut, da es sehr viele Möglichkeiten zur Anpassung gibt und das alternative Betriebssystem einem viel Privatsphäre bietet. In dieser Anleitung zeige ich dir, wie Du LineageOS auf deinem Smartphone installierst. Ich habe hierfür ein [Moto G (2014)*](https://amzn.to/2InVkBH) verwenden. Mit den meisten Smartphone sollte es aber ähnlich funktionieren.

![Startbildschirm von LineageOS](DSC_0490.JPG)

**Beim Aufspielen einer CustomROM werden alle Daten gelöscht und es kann bei Fehlern zu Schäden am Gerät kommen. Außerdem geht bei den meisten Smartphones bei diesem Vorgang die Garantie verloren.**

Bevor Du anfängst solltest Du natürlich überprüfen, ob es LineageOS überhaupt für dein Smartphone gibt. Eine Liste aller Geräte findest Du im [Downloadbereich von LineageOS](https://download.lineageos.org/).

# Backup erstellen

Als erstes sollte man ein Backup des Smartphones machen, da beim Installieren von LineageOS alle Daten auf dem Gerät gelöscht werden. Hierfür schließt man am besten sein Gerät an den Computer an und überspielt alle Dateien auf den Computer. Apps können leider nicht ohne weiteres gesichert werden.

# Bootloader entsperren

Um eine CustomROM auf einem Smartphone zu installieren, muss in den meisten Fällen der Bootloader entsperrt werden. Dies ist bei jedem Smartphone anders. Hier erkläre ich, wie dies für das Moto G (2014) funktioniert. Suche einfach mal nach "Bootloader entsperren" und deinem Gerätename mit der Suchemaschine deiner Wahl und Du wirst sicherlich eine gute Anleitung dafür finden. Mit einem Computer gehst Du als erstes auf [diesen Link](https://motorola-global-portal.custhelp.com/app/standalone/bootloader/unlock-your-device-a), klickst auf weiter und meldest Dich mit deinem Motorola-Konto an. Dort lädst Du dir die "Motorola USB Drivers" herunter und installierst diese. Dies geht leider nur mit einem Windows oder Apple-Computer. Nun fährst Du dein Smartphone herunter und startest es im Recovery Mode. Dafür hältst Du den Power-Knopf und die Lautstärke-Down-Taste für einige Sekunden gleichzeitig gedrückt. Nun sollte Dein Gerät im Recovery Mode sein. Du kannst es nun über ein USB-Kabel an deinen Computer anschließen.

![Recovery Mode](DSC_0477.JPG)

Als nächstes lädst Du dir [AndroidSDKSlim](https://mega.nz/#!ZZdSGaiZ!lvupzZWRPj8kfH2kCW-Y_hKd5zkTFsyy3IwbDNWbVt8) herunter und entpackst es. Du wechselst in den Ordner *platform-tools* und öffnest dort die Eingabeaufforderung (Shift - Rechtsklick - Eingabeaufforderung öffnen). Dort gibst Du folgenden Befehl ein, um die angeschlossenen Geräte anzuzeigen.

    fastboot devices

Hier sollte dein Gerät auftauchen. Sollte das nicht der Fall sein, hast Du die Treiber nicht richtig installiert. Nun holst Du dir den "Entsperrcode", indem Du folgendes eingibst:

    fastboot oem get_unlock_data

Dies sollte dir 5 Zeilen mit einer Zahlen- und Buchstabenfolge ausgeben. Diese kopierst Du und fügst sie zu einer Zeichenkette zusammen.

Beispiel:

    (bootloader) 0A40040192024205#4C4D3556313230
    (bootloader) 30373731363031303332323239#BD00
    (bootloader) 8A672BA4746C2CE02328A2AC0C39F95
    (bootloader) 1A3E5#1F53280002000000000000000
    (bootloader) 0000000

wird zu

    0A40040192024205#4C4D355631323030373731363031303332323239#BD008A672BA4746C2CE02328A2AC0C39F951A3E5#1F532800020000000000000000000000

Auf der [Motorola-Webseite](https://motorola-global-portal.custhelp.com/app/standalone%2Fbootloader%2Funlock-your-device-b), auf der wir vorhin die Treiber heruntergeladen haben, gibst Du nun bei Schritt 6 diese Zeichenkette ein. Dann musst Du noch einige Bedingungen akzeptieren. Per Mail hast Du einen weiteren Entsperrcode erhalten. Diesen kopierst Du und fügst Du in den nächsten Befehl ein:

    fastboot oem unlock DEINENTSPERRCODE

Nun wird dein Smartphone neustarten und es sollte entsperrt sein. Hier wirst Du den Einrichtungsbildschirm sehen. Diesen kannst Du aber ignorieren, da noch einige Schritte zu befolgen sind.

# TWRP installieren

Um eine CustomROM zu installieren, brauchst Du ein Custom Recovery mit dem Du das Betriebssystem installierst. Dieses kannst Du dir für dein Gerät auf der [TWRP Webseite](https://dl.twrp.me/) herunterladen. Die Datei verschiebst Du nun in den Ordner *platform-tools*, indem sich auch schon die fastboot.exe befindet. Nun startest Du dein Handy wieder im Recovery Mode (Power-Knopf und die Lautstärke-Down-Taste für einige Sekunden gleichzeitig gedrückt halten) und schließt es an den Computer an. In der Eingabeaufforderung gibst Du nun folgenden Befehl ein, um TWRP zu flashen:

    fastboot flash recovery TWRP....img

Dabei musst Du "TWRP....img" durch den Dateinamen der Datei, die Du gerade heruntergeladen hast, ersetzen. Dein Smartphone kannst Du nun vom Computer trennen. Im Recovery Mode wählst Du mit der Lautstärke-Down-Taste den Punkt *Recovery* aus. Nun sollte TWRP starten. Bevor wir weiter machen, solltest Du noch ein Backup deines Systems machen. Dafür wählst Du den Punkt *Backup* und setzt bei *System* und *Data* einen Hacken. Dieser Vorgang dauert ungefähr eine halbe Stunde. Das Backup solltest Du am besten auf einer externen microSD-Karte oder einem Computer speichern, da Du es benötigst, falls etwas schief läuft. Nun gehst Du noch auf *Wipe* um alle Daten auf deinem Gerät unwiderruflich zu löschen.

![TWRP Recovery](DSC_0464.JPG)

# LineageOS installieren

Auf der offiziellen Webseite von LineageOS solltest Du nun als nächstes die Software für dein Smartphone herunterladen. Außerdem solltest Du noch beim Punkt *Extras* das Paket *addonsu* herunterladen, falls Du dein Gerät rooten möchtest. Diese beiden Dateien schiebst Du nun auf dein Gerät oder deine microSD-Karte. In TWRP wählst Du den Punkt *Install* aus und installierst zuerst das Image für LineageOS und dann das Paket, um dein Gerät noch zu rooten.

![LineageOS startet](DSC_0479.JPG)

# Fazit

Nun kannst Du dein Gerät ganz normal starten und LineageOS sollte automatisch starten. In den Einstellungen drückst Du sieben mal auf die *Build Number*, um die Entwickler-Optionen freizuschalten. Nun sollte in den Einstellungen die Kategorie Entwickleroptionen dazugekommen sein. Dort musst Du bei *Root access* den Punkt *Apps and ADB* auswählen, um Root-Rechte zu bekommen. Meiner Meinung nach ist LineageOS eine tolle Alternative zum Betriebssystem des Herstellers. Falls Du die Google-Apps benötigst, kannst Du die [Open GApps](http://opengapps.org/) ausprobieren. Sonst rate ich dir noch den F-Droid-Store als Alternative zum Play Store zu verwenden.
