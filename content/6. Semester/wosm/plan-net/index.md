+++
title = "Plan of Network"
date = 2026-02-28
[taxonomies]
authors = ["fatlum"]
tags = ["wosm"]
+++

---

***Drehbuch: [Modulübersicht PCLS – Drehbuch](https://sgi.pages.fhnw.ch/moduluebersicht/2026fs/wosm/drehbuch.html)***  
***Aufgaben: [Beschreibung Aufgaben](https://spd.pages.fhnw.ch/module/wosm/content/wosm/welcome-wosm.html)***

Der Konkrete plan sieht wie folgt aus:
Verwendete Clouds, Infrastrukturen: Azure, AWS, SWITCHengines, on-prem

Pro Cloudumgebung (Site):

- VM die als Router fungiert
- k3s cluster aufbauen
- 1 subnet für das mgmt (controle plane)
- 1 subnet für worker node (Pods mit der App)
- 1 subnet für data (DB)

Zwischen den Sites soll ein FullMesh entstehen, also jede Site ist mit jeder Verbunden.
Es soll auch auf Ausfallsicherheit geschaut werden, dass heisst die Sites sollen mit OSPF geroutet werden.
Weiter muss ein Monitoring vorhanden sein, es soll zum einten Netzwerktraffic gemonitort werden und zum anderen
auf App-Level. Für beide Vorhaben, kann man vielleicht Promtheus und Grafana nutzen.
