+++
title = "IP5 infos"
date = 2025-09-17
[taxonomies]
authors = ["fatlum"]
tags = ["ip5-infos"]
+++

# EID – Überblick & Workflow
---
## Überblick
Eine EID (External Interface Description) ist eine SGr-konforme XML-Datei, die mehrere Elemente umfasst:
- ein Interface (z. B. REST, MQTT, Bus/Modbus),
- ein oder mehrere Functional Profiles,
- und darin ein oder mehrere Datenpunkte.
  Alle diese Teile gehören in eine gültige, SGr-konforme XML-Datei.
  Die Schwierigkeit liegt vor allem in der korrekten Erstellung und in der Validierung.
---
##Workflow (in unserer Software)

***Auswahl beim Start:***
- EID erstellen, EID öffnen oder EID bearbeiten.
  ***Wenn „Erstellen“ gewählt wird:***

1. Interface auswählen
   Beispiel (pseudomäßig als XML dargestellt):
```xml
<http>RJ45</http>
```

2. Mehrere Functional Profiles auswählen
   Beispiel:
```xml
<funcprofile>PlaceholderProfil</funcprofile>
```

3. Datenpunkte je Functional Profile definieren
   Beispiel:
```xml
<funcprofile>PlaceholderProfil
    <datenpunkt>points</datenpunkt>
</funcprofile>
```
---
## Struktur (vereinfacht)
So könnte das Gesamtbild (vereinfacht) aussehen:
```xml
<interface>
    <funcprofile>PlaceholderProfil
        <datenpunkt>points</datenpunkt>
    </funcprofile>
</interface>
```
Während man im GUI Felder auswählt (an-/abwählt und ausfüllt), erzeugt die Software im Hintergrund eine valide und SGr-konforme XML.

---
## Generierung & Validierung
- Die XML muss webbasiert korrekt generiert werden.
- Validierung: Es ist wichtig, die erzeugte Datei gegen das SGr-Schema zu prüfen.
- Noch offen:
  - Müssen Nutzer manuell Inhalte ergänzen?
  - Oder lesen wir eine bestehende EID des Kunden ein und füllen Felder automatisch vor?
---
## Kataloge & Geräte
- Wir haben Listen für Functional Profiles (in einem Repository).
- Ebenfalls gibt es Listen für Geräteklassen (welche elektronischen Haushaltsgeräte vorhanden sind).
- Eine Gruppe von Datenpunkten bildet gemeinsam ein Functional Profile.
---
## Schnittstellen & Zugriff
- Lesen/Schreiben der Datenpunkte erfolgt über das gewählte Interface, z. B. REST API oder Modbus.
- Ziel ist, dass die GUI-Aktionen direkt in ein valide strukturiertes XML münden.