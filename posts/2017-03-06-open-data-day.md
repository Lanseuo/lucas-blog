---
title: Feinstaubsensor und Open Data im OK Lab Stuttgart
image: DSC_0083.JPG
description: Am 4. März 2017 lernten wir beim Open Data Day in Stuttgart, wie man Daten einsetzen kann, um Zustände zu analysieren und zu verbessern.
---

Am Samstag den 4. März 2017 fand der Open Data Day in der Stadtbibliothek am Mailänder Platz statt. Bei dem Event ging es darum, wie man mit Open Data etwas in der Stadt verbessern kann.

# Sessions

Zuerst hörten wir uns drei verschiedene Sessions, zu den Themen Open Data und der Grippewelle an. Hierbei wurde uns als erstes erklärt, wie man Open Data überhaupt nutzen kann und wo es noch Probleme gibt. Später wurde uns der Zusammenhang von Feinstaub und der Grippewelle deutlich gemacht.

> Ewald Thoma hat eine Korrelation von [#Feinstaub](https://twitter.com/hashtag/Feinstaub?src=hash)-Belastung und der Grippewelle festgestellt. Deutlicher Hinweis für kausalen Zusammenhang. [pic.twitter.com/Bxv5RO7KNR](https://t.co/Bxv5RO7KNR)
>
> — Jan Lutz (@Jan_sagt) [4\. März 2017](https://twitter.com/Jan_sagt/status/837989167766306817)

# Feinstaubsensor basteln

Als nächstes ging es damit weiter, einen Feinstaubsensor selber zu bauen. Dafür wird ein NodeMCU, ein Feinstaubsensor (SDS011), ein Temperatur & Luftfeuchtigkeitssensor (DHT22), Kabel, Stromversorgung und ein Rohr benötigt. Die Bauteile wurden über die Kabel miteinander verbunden und in das Rohr gesteckt. Nun musste man den NodeMCU nur noch über ein USB-Kabel mit dem Steckernetzteil verbinden und schon war der Sensor fertig.

![Feinstaubsensor auseinandergebaut](DSC_0078.JPG)

Wenn der NodeMCU das erste Mal Strom erhält, erstellt er einen WIFI-Accesspoint, mit dem man sich dann verbindet. Über ein Webinterface gibt man jetzt noch die Zugangsdaten für das WLAN an und schon kann man die Feinstaubwerte für die eigene Umgebung einsehen. Eigentlich ganz einfach!

<blockquote class="twitter-tweet" data-lang="en"><p lang="de" dir="ltr">Heute entstehen wieder eine ganze Reihe an Feinstaubmessgeräten.<a href="https://twitter.com/hashtag/Stuttgart?src=hash&amp;ref_src=twsrc%5Etfw">#Stuttgart</a> <a href="https://twitter.com/hashtag/Feinstaubalarm?src=hash&amp;ref_src=twsrc%5Etfw">#Feinstaubalarm</a> <a href="https://twitter.com/hashtag/Feinstaub?src=hash&amp;ref_src=twsrc%5Etfw">#Feinstaub</a> <a href="https://twitter.com/hashtag/DIY?src=hash&amp;ref_src=twsrc%5Etfw">#DIY</a> <a href="https://twitter.com/hashtag/ODD17?src=hash&amp;ref_src=twsrc%5Etfw">#ODD17</a> <a href="https://twitter.com/hashtag/opendataday?src=hash&amp;ref_src=twsrc%5Etfw">#opendataday</a> <a href="https://twitter.com/codeforS?ref_src=twsrc%5Etfw">@codeforS</a> <a href="https://t.co/be4aAmys0R">pic.twitter.com/be4aAmys0R</a></p>&mdash; RepairCafé Stuttgart (@RepaircafeStgt) <a href="https://twitter.com/RepaircafeStgt/status/838006884640702465?ref_src=twsrc%5Etfw">March 4, 2017</a></blockquote>
<script async src="https://platform.twitter.com/widgets.js" charset="utf-8"></script>

Wer selber einen Feinstaubsensor basteln möchte, findet hier eine [Bauanleitung](http://luftdaten.info/feinstaubsensor-bauen/).

# Mini Barcamp

Weiter ging es mit drei verschiedenen Mini Barcamps. Zur Auswahl gab es Gesundheitsauswirkungen von Feinstaub, Verbesserung der Hardware bzw. die Patenfindung und Visualisierung. Ich entschied mit für die Verbesserung der Hardware bzw. die Patenfindung. In unserer Gruppe sammelten wir Ideen, wie man den Feinstaubsensor auch für Leute attraktiv machen kann, die sich nicht um die Technik kümmern wollen, sondern nur WLAN und einen Platz anbieten können, an dem man den Sensor anbringt. Außerdem ging es um die Verschönerung des Wetterschutzes und die Möglichkeit auch mobil zu messen. Am Ende unserer Brainstorming-Runde wurden unsere Ergebnisse den anderen Gruppen vorgestellt.

<blockquote class="twitter-tweet" data-lang="en"><p lang="de" dir="ltr">Rund 100 Teilnehmende beim 1. <a href="https://twitter.com/hashtag/odd17?src=hash&amp;ref_src=twsrc%5Etfw">#odd17</a> in der Stadtbibliothek in <a href="https://twitter.com/hashtag/Stuttgart?src=hash&amp;ref_src=twsrc%5Etfw">#Stuttgart</a>. Mehrere Sessions und Bastel-Workshop laufen. <a href="https://t.co/fAfAdNBKvR">pic.twitter.com/fAfAdNBKvR</a></p>&mdash; OK Lab Stuttgart (@codeforS) <a href="https://twitter.com/codeforS/status/838031806687490048?ref_src=twsrc%5Etfw">March 4, 2017</a></blockquote>
<script async src="https://platform.twitter.com/widgets.js" charset="utf-8"></script>

Zum Schluss gab es noch einen Hangout mit den anderen OK Labs aus Deutschland.

# Feinstaubsensor anbringen

Als ich wieder zu Hause war, brachte ich den Feinstaubsensor noch an unserem Balkon an. Dafür befestigte ich das Rohr mit Kabelbinder und verlegte das USB-Kabel.

![Feinstaubsensor am Balkon](DSC_0085.JPG)
