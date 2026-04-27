+++
title = "Teil 3"
date = 2026-04-27
[taxonomies]
authors = ["fatlum"]
tags = ["wosm"]
+++

---

***Drehbuch: [Modulübersicht PCLS – Drehbuch](https://sgi.pages.fhnw.ch/moduluebersicht/2026fs/wosm/drehbuch.html)***  
***Aufgaben: [Beschreibung Aufgaben](https://spd.pages.fhnw.ch/module/wosm/content/wosm/welcome-wosm.html)***

---

# Part 3

- platform engineer
- features der platform zu bauen
- OCI deployments aufbauen
- netzwerk und infra nutzen
- features:
  - deployment definition
  - IaC
  - was deployen?
  - welche parameter für deployment?
  - automatisiert stattfinden
  - ziel infrastruktur auswählen zum depployen
  - deployment auf single cloud und einmal multi cloud
- golden paths:
  - einen geradlinigen weg für uns definieren je nach applikation
  - user ermöglichen einen sauberen weg zu nutzen um zu liefern
- infra abstraktion
  - möglichst wenig über inhalt der platform wissen
  - möglichst wenig über ziel infrastruktur wissen
  - memory, persistent, ziel infra auswählen können
- seperation of concern
  - user muss keine ahnung haben wie es im hintergrund läuft
- managed services
  - secretmanagment, logging, databases etc.
  - in irgend einer seite einbinden
  - diese services soll auf plattform seite sein
  - der user soll dann dies nutzen können
  - einer der services soll einen state haben
  - platform soll dies unterstützen
  - state darf target infra bleiben
- bonus:
  - bei erfüllung der kriterien gibt es 6er
  - trotzdem eine bonus aufgabe
  - deployte applikation einer anderen gruppe auf unsere platform deployen
  - wir geben doku des golden paths und einer minimalen definition der platform
    und wann soll es deployen können
- lieferobjekte:
  - lauffähige deployment
  - applikationslandschaft
  - das manual, README.md wie ein deployment läuft
