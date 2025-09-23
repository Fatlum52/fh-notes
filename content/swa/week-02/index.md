+++
title = "Week 02"
date = 2025-09-23
[taxonomies]
authors = ["fatlum"]
tags = ["swa"]
+++

# Fragen von Menti:
- modell repräsentiert etwas
- ***view model:***
  - viewpoint: entspricht einer klasse
  - view ist eine instanz des viewpoints
  - view-modell -> sichtenmodell
- ***How do View Models support the process of designing software architecture?***
  - kruchten-modell
  - legen reihenfolge gewisser prozesse
  - in den unterschiedlichen grossen phasen leisten beiträge
    - wenn man ein modell durchzieht, hat mann hohe stabilität 
    - man hat es auf papier schon getestet, wenn man es durch zieht -> kosten senkung
- ***Name the 5 viewpoints of the Kruchten 4+1 View Model***
  - development view
  - logical view
  - physical view
  - scenarios
  - process view
- ***Why does the View Model refer to 4+1 viewpoints and not 5 – what categorical difference is made here?***
  - mit den scenarios erfasst man keine lösung, sondern eine problematik
  - use case sind generisch
    - szenrario sind instanzen von use cases
  - szenarios stick everything together 
  - szenario geben hinweis, wie wir die building block arangieren/orchestrieren
  - szen. sind lösungsstrukturen
- ***What does the low representational gap require from a good software design?***
  - die fachliche und die reprsentanz in der software sollen nahe beieinander sein 
  - OOP ist so etwas gewesen dass man die realität gut modellieren kann in der software
  - good naming convention etc. 

# Aufgabe
- Es ging vorallem um UML Sequenz diagrammen
- wie könnten die Use Cases, anwendungsfälle, szenarios auf objektstrukturen verteilen?
- Logical View: war in diesem fall ein UML-Sequenzdiagramm
- Aus logical view folgt ein development view
  - aus dem logical, hat man die titel der sequenzen entnommen, und diese sind direkt klassen in java
- development view (analysis model -> system disgn)
- process-view: 
  - gibt es mehrere programme, die ich getrennt voneinander laufen lassen will
  - wenn es zu einer verteilung kommt, was sind anforderungen von den einzelnen prozessen
  - wo würden die pakete von dev. view landen? wie würden sie laufen? etc. 
  - prozesse laufen auf physical view, wie wird dieser organisiert etc. 
- logical, dev, process und physical view kommen in einem scenario vor
- scenario driven design -> anhand den 4 + 1 view model haben wir das gemacht. 
- aus dem logical view, eine dev view gemacht und dann in java überführt