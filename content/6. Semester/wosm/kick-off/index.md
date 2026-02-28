+++
title = "Week 01"
date = 2026-02-23
[taxonomies]
authors = ["fatlum"]
tags = ["wosm"]
+++

---

***Drehbuch: [Modulübersicht PCLS – Drehbuch](https://sgi.pages.fhnw.ch/moduluebersicht/2026fs/wosm/drehbuch.html)***  
***Aufgaben: [Beschreibung Aufgaben](https://spd.pages.fhnw.ch/module/wosm/content/wosm/welcome-wosm.html)***

netzwerksicherheit

- zugang swtich engines
- azure zugang
- diese woche zu mass cluster, on prem
- sie sollen miteiander reden
- vpn zueiander ziehen
- open sense verwenden vielleicht
- maschinen mit openVPN
- wireguard vielleicht nutzen
- full mesh zwischen clouds
- vpn von jeder cloud zu anderer
  - ausfall sicher machen

- zugriffsseite
- den daten verkehr filtern, also nicht plain umher senden
- firewall regeln:
  - argumentieren wieso wir welche gesetzt haben
  - nicht schlimm, wenn man hätte welche einführen können

- rendundant machen
- abgabe teil 1:
  - bericht, welche technologie verwenden etc.
  - offenen vpn technologien nutzen -> wäre schön¨
  - 2-3 seiten, nicht übertreiben

infrastruktur:

- bilden basis für 3 abgabe
- deploymentplattform
- was wir deployen, als source code, als IaC
- cloud übergreifend etwas monitoren
- stack, vpn, deploymentplattform montioren
- die logs aggregieren
- die architektur soll erweiterbar sein
- alterting einrichten, egal per was, email, teams, was auch immer
- monitoring muss nachgezogen werden
- alles mit IaC
- lieferobjekte:
  - bericht, mit architekturübersicht, viele grafiken, komponenten auflisten etc.
  - nicht all zu viele seiten
  
deployment freigabe:

- die deployenden services sollen OCI-Container sein
- golden paths definieren -> wie muss die applikation geliefert werden
- infra abstraktion:muser muss nicht wissen, wie wir alles aufgebaut haben
- die app umfasst services, eine muss minimum eine state habe
- eine kann singel cloud sein, die anderen services müssen multi cloud sein

- lieferobjekte
    -
