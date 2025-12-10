+++
title = "Idee"
date = 2025-12-02
[taxonomies]
authors = ["fatlum"]
tags = ["lean"]
+++

- Idee:
  - Wanderapp
  - Routen laden
  - Durch Route führen
  - Entlang der Route Anmerkungen machen (Bilder, Videos, Text)
  - Charts der Route anzeigen
  - Online Routen
  - Offline herunterladbar
  - Exportierbar auf kompatible Geräte
  - Routen Zeichnen
  - Packliste teilen, erstellen

---

- Expansionsmöglichkeiten:
  - Routen ausserhalb CH
  - SAC-Hütte mieten
  - Biking Routen
  - (Klettern)

---

- Finanzen:
  - Liteversion gratis aber mit Werbung
  - Vollversion 15.- einmalig

---

- 3 solution interviews
  - alle KI sein
  - SW10 ab S35

- 3 berater gespräche
  - 1 real, 2 KI
  - SW5 ab S15
  - SW7 ab S17
  - ertragsmodell unterstützt?

- 3 problem interviews
  - 1 real, 2 KI
  - SW9

- slide 9 steht etwas über problem
- slide 11 steht der rest was erwartet wird

---

Vision:
WanderGo definiert das Wandererlebnis neu, indem es die Grenzen zwischen Planung, Abenteuer und Erinnerung aufhebt.
Wir bauen nicht nur ein Navigationswerkzeug, sondern das digitale Gedächtnis für jeden Schritt in der Natur.
Unsere Vision ist eine Welt, in der jeder Wanderer – vom Anfänger bis zum Profi – die Freiheit hat, eigene
Wege zu gehen, sie sicher zu meistern und die schönsten Momente nahtlos mit anderen zu teilen.
Wir machen Technik unsichtbar, damit das Erlebnis im Vordergrund steht

Slogan:
WanderGo: Dein Weg. Deine Geschichte

---

Features:

- Create & Discover (Planung):
  - Feature: Live-GPS-Tracking & Routen-Aufzeichnung
  - Nutzen: Einfach loslaufen und Neues entdecken. Die App zeichnet den gegangenen Weg automatisch auf und erstellt daraus eine speicherbare Route für die Zukunft – inkl. aller Höhenmeter und Statistiken.

- Guide & Survive (Unterwegs):
  - Feature: Präzise Turn-by-Turn Führung, vollständige Offline-Verfügbarkeit, Export auf Wearables/Garmin.
  - Nutzen: Sicherheit in jedem Gelände, ohne vom Smartphone abhängig zu sein.

- Capture & Relive (Erinnerung):
  - Feature: Geo-getaggte Anmerkungen (Text, Foto, Video) direkt auf der Route.
  - Nutzen: Die Wanderung wird zum digitalen Reisetagebuch. Man sieht nicht nur wo man war, sondern was man dort erlebt hat.

- Analyze & Prepare (Optimierung):
  - Feature: Höhenprofile, Leistungscharts, teilbare Packlisten.
  - Nutzen: Perfekte Vorbereitung und detaillierte Nachbereitung der eigenen Leistung.

---

unter folgendem link sieht man, dass die schweiz ca. 4 millionen aktive wanderer hat:
[wanderer statistik](https://wandern-in-zahlen.ch/die-wandernden)

---

Geschäftsmodell:

***Phase 1 (1-2 Jahre):***
Die Schweiz hat 4 Millionen aktive Wanderer. Wenn nur 3000 von den 4 Millionen aktiven Wanderer eine einmalige Zahlung von 15.-
machen würden, dann wären wir bei einem Brutto gewinn von: 45’000
Die Serverkosten belaufen sich auf ca. 200 pro Monat, was etwa 2400.- für ein Jahr ausmacht.
Apple verdient 15% für jeden App-Kauf bei dem der Firmenwert unter 1 Mio liegt.
Das macht also einen Abzug von 2.25 pro Kauf. Nachfolgend sind alle Zahlen in `CHF`.

```bash
Zahlen pro Kauf:
App:              + 15.0
MwSt(8.1):        -  1.2
Apple/Google-fee: -  2.1
                 _______
Gewinn pro Kauf:    11.7
```

```bash
Netto gerechnet kommen wir auf folgende Zahlen:
3000 Käufe:    + 35'100
Serverkosten:  -  2'400
              _________
Gewinn:          32'700
```

Extrem viel ist das nicht, aber für das erste oder zweite Jahr ist das ein gutes Startkapital was man sich nebenbei aufgebaut hat.
Mit diesem Geld könnte man sich dann überlegen, ob man expandieren will, ausserhalb der Schweiz und in Marketing investieren.
Hat man sich erst mal einen Namen gemacht, kann man auf ein Abo-Modell umstellen.

***Phase 2 (Skalierung & Abo-Modell):***
Nach Etablierung der Marke Umstellung auf Recurring Revenue (SaaS), um laufende Cloud-Kosten zu decken und Weiterentwicklung zu finanzieren.
Preismodell: Jährlich 60.- (Rabatt) oder Monatlich 7.- (Flexibilität).

Annahme Szenario:
Wachstum auf 5'000 aktive Abonnenten.
Split: 70% Jahres-Abos (3'500 User), 30% Monats-Abos.
Serverkosten steigen auf ca. 400.-/Monat (4'800.-/Jahr) durch erhöhten Datenspeicher (Bilder/Videos).

Zahlen pro Abo (Unit Economics):

```bash
Option A (Jahres-Abo):
Preis:            + 60.00
MwSt(8.1):        -  4.50
Apple/Google-fee: -  8.33
                 ________
Gewinn pro User:    47.17
```

```bash
Option B (Monats-Abo):
Preis:            +  7.00
MwSt(8.1):        -  0.52
Apple/Google-fee: -  0.97
                 ________
Gewinn pro Monat:    5.51

Gesamtrechnung (Pro Jahr):
3'500 Jahres-Abos:          + 165'095
1'500 Monats-Abos (x6):     +  49'590
Serverkosten:               -   4'800
                           __________
Gewinn (EBIT):                209'885
```

Strategisches Vorgehen:
Der Hebel beim Abo-Modell ist deutlich grösser. Während Phase 1 Startkapital liefert, baut Phase 2 ein echtes Unternehmen auf.
Wichtig: "Grandfathering" für die frühen Käufer aus Phase 1 (sie behalten Pro-Status auf Lebenszeit), um Loyalität zu sichern.
Saisonale Schwankungen bei Monats-Abos (Wintermonate) müssen durch Jahres-Abos abgefedert werden.

---

Berater Persona 1: Die Verbands-Strategin
Diese Persona vertritt die Sicht der breiten Masse und der offiziellen Institutionen. Sie weiß, wie „Herr und Frau Schweizer“ ticken.
Name: Ursula Gerber Alter: 48 Jahre Beruf: Projektleiterin bei einer Tourismus-Region (z.B. Graubünden Tourismus) & Vorstandsmitglied in einem regionalen Wanderweg-Verein.
Hintergrund & Expertise: Ursula arbeitet seit 20 Jahren im Schweizer Tourismus. Sie kennt die Statistiken: Wer wandert, wie alt sind die Leute und wofür geben sie Geld aus. Sie ist keine Tech-Expertin, nutzt aber beruflich digitale Tools zur Besucherlenkung.

- Ihre Haltung zur App & Zahlungsbereitschaft:
  - Markt-Einschätzung: Sie weiß, dass Schweizer Wanderer hohe Qualität erwarten. Die Signalisation (gelbe Wegweiser) ist in der Schweiz perfekt. Eine App muss also mehr bieten als nur „Wegfindung“, sonst nutzt man einfach die kostenlose Swisstopo-App.
  - Zahlung: Sie glaubt, dass Schweizer bereit sind, einmalig 15.- zu zahlen (wie für eine gute Wanderkarte aus Papier), aber sehr skeptisch gegenüber Abos sind, wenn sie keinen massiven, regelmäßigen Mehrwert sehen.

Kritischer Punkt: „Warum soll ich für Routen zahlen, wenn SchweizMobil gratis ist? Dein Mehrwert muss das 'Erlebnis' sein, nicht die Karte.“

---

Berater Persona 2: Der Outdoor-Händler & Blogger
Diese Persona ist näher am kommerziellen „Point of Sale“. Er weiß, wofür Wanderer bereit sind, das Portemonnaie zu öffnen.
Name: Marco Bieri Alter: 36 Jahre Beruf: Inhaber eines spezialisierten Bergsport-Ladens und Betreiber eines bekannten Schweizer Outdoor-Blogs.
Hintergrund & Expertise: Marco verkauft jeden Tag Ausrüstung. Er redet mit Kunden darüber, welche Gadgets sie nutzen. Er testet selbst Apps und schreibt darüber. Er ist pragmatisch: Was nicht funktioniert oder zu kompliziert ist, fliegt raus. Er kennt die Konkurrenz (Komoot, Strava, Outdooractive) sehr gut.

- Ihre Haltung zur App & Zahlungsbereitschaft:
  - Markt-Einschätzung: Er sieht eine Nische für „Genuss-Wanderer“, die ihre Erlebnisse festhalten wollen (dein Feature mit Bildern/Notizen). Die reinen Sportler sind schon bei Strava, die Traditionalisten bei Swisstopo.
  - Zahlung: Er findet das Modell „15.- Einmalzahlung“ sehr attraktiv für den Verkauf. Er sagt: „Die Leute kaufen bei mir Wanderschuhe für 300 Franken. 15 Stutz für eine App ist ein 'No-Brainer' (Mitnahmeartikel), wenn sie gut aussieht.“
  - Kritischer Punkt: „Die App muss 'sexy' sein. Wenn das Routen-Tracking Akku frisst oder das Teilen der Bilder kompliziert ist, bekommst du schlechte Bewertungen, und dann kauft es keiner mehr.“

---
