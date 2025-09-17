+++
title = "Week 01"
date = 2025-09-16
[taxonomies]
authors = ["fatlum"]
tags = ["pcls"]
+++

*** Drehbücher: https://sgi.pages.fhnw.ch/moduluebersicht/ ***
---

*** Relevante Links***
- 

## Prüfung / Note
- 2 * 25% -> Projekt
- 1 schriftliche Prüfung 50%

## Projects
- laufende Applikation von einem cloud zum anderen migrieren 
  - Iaas (switch) zu Paas (ECS/AWS)
- Artifakte:
  - IaC der infrastruktur
  - kleines screenrecording von der migration
  - die plattform selber
  - kleiner report 
  - Deadline für artefakte:
    - Sonntag, 23:59, KW42/KW47
    - kurze fragerunde zu den Artefakten
---

# Frontal Unterricht
cloud
  - netzwerkzugriff
  - measured meter
  - resourcing pooling
  - rapid elasticity
  - measure service 

cloud deployment models:
  - ***private*** cloud für benutzung von einer organisation 
    - während regelung von firewall
    - dritt person managed die cloud
    - skaliert nicht so gut wie public cloud
  - ***public cloud*** für die öffentlichkeit
    - multi-tenant
    - allgemeine nutzung
    - keine volle kontrolle über daten
  - ***community cloud***
    - für organisationen die miteinander sharen, wie ein Staat oder eine Schule
  - ***hybrid cloud***
    - kaum zu sehen in der realität
    - eine mischung aus public und private

***services:***
  - Infrastructure as a Service
  - Platform as a Service
  - Software as a Service
  - gemeinsamkeit: eine abstraktion, was braucht man?
    - IaaS > PaaS > SaaS >, wo > heisst mehr abstraktion und mehr standardisierung
  - Je weiter links man ist, umso mehr Verantwortung muss man übernehmen
  - Je nachdem was man bezieht, iaas, paas, etc. übernimmt man verschieden viel verantwortung 

***IaaS***
  - Servers und Storage
  - pro:
    - keine hardware, blue-prints für os installation 
    - disaster recovery auf os-level
    - schnelles anpassen von ressourcen, vertical scaling
    - hohe sicherheit aufgrund von automatisierung und audits und monitoring
    - economy of sales, anbieter skaliert eigene infrastruktur und bekommt schneller return of invest
  - cons:
    - teuerster service
    - kapazitäten werden vom kunden skaliert, keine automatische vertical scaling
    - anpassen der ressourcen erfordern ein neustart des services
    - system zu operaten muss vom kunde übernommen werden 
    - kein leichtes horizontales scaling, eigenes system patching

***PaaS***
  - deployment frameworks including build, test, deployen, managing, updating
  - eigenen business code managen
  - analytics und business intelligence
  - auth, workflow engines
  - pro:
    - kürzere entiwcklungsphasen (from coding to production)
    - innovativ toolchains
    - saubere geteilte verantwortung
    - keine os-operating, os-lifecycle
    - automatisches scaling
  - con:
    - vendor locking
    - native services
    - sehr opinionated, mit eigenen services und eigenem eco system
    - sehr steile lernkurve, man lernt dort aws, azure etc. keine konzepte etc.

***SaaS***
  - office 365, google g-suite, atlassian, diverse ERP, Github
  - pro:
    - direkte nutzung
    - kunden können auf eigenes business fokussieren
    - hohe verfügbarkeit
    - es skaliert mit anzahl user
  - con:
    - vendor locking (kunde ist stark abhängig von service)
    - kann teuer werden 
    - keine grosse anpassungsmöglichkeiten an eigenen workflow, charakteristiken
    - wenn unterbruch, dann gewesen 

## Wieso public cloud infrastructure nutzen?
- schneller am markt
- increase in agility (shift left) -> wenn man während entwicklung schon um deployment gedanken macht
- höhere verfügbarkeit
- leichteres kapazitäten planung
- bessere sicherheit include best practice
- auf business fokussieren statt infrastructure
- pay-as-you-go models

***opex vs capex***
- capex (capital expenditure)
- opex (operational expenditure)
- nachschauen und ergänzen

***region and availability zones***
- region:
  - geographische region wo rechenzentren stehen 
  - ganze anlage mit mehreren rechenzentren / gebäuden
- availability zone:
  - eine einziges rechenzentrum innerhalb einer availability zone




