+++
title = "Week 01"
weight = 1
date = 2025-09-15
[taxonomies]
authors = ["fatlum"]
tags = ["devops"]
+++

# Intro

## Learning target
- Architektur berücksichtigt
- Build and deployment
- basic logging / monitoring
- Applikation entwickeln und selber betreiben

## Gruppenarbeit ganzes Semester
- Chatbot implementieren
- Bauen, releasen und runnen auf kubernetes cluster
- Fähigkeit was gebaut wurde zu deployen, für alle verfügbar
- Day 2-Operations: Es soll laufen, auch am nächsten tag
  - ## Constraint
  - 3 micro services
  - chattende chatbots
  - kommunikation über urls
  - pro person, andere programmiersprache 

## Struktur Vorlesung
- Wöchentliche Hausarbeit
- Erste 45 min der vorlesung, besprechung von alter Aufgabe
- Frontal-Unterrricht beginn: 09:00
- Siehe mehr in intro-01 Folien

## Wieso DevOps?
- Software betrieb nicht nur entwickeln
- Sauberes Arbeit: konventionelle commits, fixes prefix
- fixes prefix: Filtern möglich, bsp: GL-xxx: lorem ipsum

## Notengebung
- 25% Project, 25% Project, 50% Schriftliche Prüfung

# Frontaler Unterricht

## Motivation 1
- Wieso DevOps?: Es muss laufen, heute morgen und in 5 tagen
- Ops sorgrt dafür, dass man nicht einfach etwas entwickeln kann, hürden setzen
- wann ist software stabil?: mainframe, man bringt keine featuer mehr rein, aber max stabil
- devs wollen änderungen, schön aussehen, featues etc. während ops keine änderungen haben wollen
- ops prozesse sind starr, schlicht und straight forward
- grundidee hinter devops:
  - so deployen, dass es läuft
  - coden, builden, testen, deployen, releasen und monitoren 
- problem früher: alles manuell, und sehr lange -> bis zu 6 monate für einen change 
- viele manuelle interaktionen, copy pasten dateien die programmiert wurde
- manuelles feedback
- wenn menschen miteinander reden, ist fehlerquelle hoch

## Motivation 2
- komplexität händeln 
- wir sind bei sehr komplexen prozessen, fokussieren uns aber auf altes zeug (1980)
- versionenkontrollen handhaben die komplexität in einem ersten schritt

## Motivation 3
- technologien über prozesse
- man sollte service managemenet automatisieren
- fehler sind zusammenhängend, ein fehler löst oft weitere aus
- mean time to repair (MTTR) = wie lange brauche ich, bis man erkennt wo der fehler ist

## Motivation 4
- den flow beschleunigen
- 70er: 1-3 jahre für einen release
- 90er: 3 bis 12 monate 
- 00er: 2 - 12 wochen 
- zweit stabilste software ist die, die am meisten änderungen hat
- bsp: alle 6 monate liefert ihr einen riesen change, viel kann schief laufen
- wenn man kontinuierlich released, ist die chance klein das etwas bricht, weil immer kleine steps 
- in diesem kurs machen wir viele kleine steps
- was ist gut durch automatisieren: 
  - je grösser die batchsize, höhere holding cost
  - die kosten kann man ausrechnen (siehe folien "motivation")
- wichtige metriken:
  - lead time, cycle time, lead time for changes
    - kunde will änderung
    - team fängt an zu arbeiten
    - es wird commitet
    - deployment 

## Motivation 5
- reabiliät ist das wichtigste feature
- kunden und menschen wollen zuverlässigkeit und genauigkeit
- wenn man dem system nicht vertaut, nutzt man es nicht
- schauene das man frühgenug eine nachricht bekommt, dass etwas nicht stimmt
- dora metrics:
  - lead time, deployment frequency, change fail, time to restore, availability

# Wieso kommt devops?
## Driver 1: Cloud
- cloud ist sourcecode 
- cloud ist automation
- cloud is shared
- cloud is transparent
- cloud is scalable 

## Driver 2
- isolation
  - überall deployen wo man will und auf was man will
- architecture
  - micro services, jeder macht sein eigenes ding und hinten kommt ein container raus
  - früher: 20 teams, 1 jar file

## Driver 3
- automate everything / remove toil
- grösse der datenzentren steigt exponentiell 
- immer mehr sachen zum machen, mit gleich viel leuten 
- man sollte sich weg automatisieren -> automatismen entwickeln 

## Driver 4
- take responsibility 
- was man deployt soll verheben 

## Driver 5
- kultur
- wichtigste ist zu sagen "wir wollen etwas zusammenbauen"

## recaps questions, können an prüfung dran kommen:
1. Name and describe the 5 DORA metrics
2. Why is Cloud important for DevOps and why is DevOps important for Cloud?
3. Name and explain different targets classical Developer- and Operationsteams have. Why do
   they have them?
4. Explain why containerization is important for DevOps.
5. Automation is the key for successful DevOps-Workflows. Why is scalability, ongoing with
   automation so important when it comes especially to deploying microservice architectures?
   Why is it important with respect to the lead time?

