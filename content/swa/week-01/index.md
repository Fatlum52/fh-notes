+++
title = "Week 01"
date = 2025-09-16
[taxonomies]
authors = ["fatlum"]
tags = ["swa"]
+++

## System
- ontologische ansicht: auch white-box
  - wir nehmen diese ansicht, wenn wir wissen wollen wie das system aufgebaut ist
- static view: 
  - zeigt die basis beziehungen zwischen building block 
  - überblick von building blocks und design time 
- dynamische view:
  - wie die komponenten miteinander arbeiten 
---
 ## Building blocks, Bausteine
- können verschiedene typen sein
- bsp: Applikation, Data, Technologie 
- es gibt socio building blocks 
  - zeigt das zwischen menschliche
  - beziehungen zwischen menschen, verantwortung, position etc. 
---
## Architecture Disciples, Architektur Disziplinen
- drei verschiedene disziplinen 
- unterscheiden sich hauptsächlich in der granularität, wie genau wird draufgeschaut
- Jedes Unternehmen folgt diesen drei disziplinen 
- Unternehmen- und Domänen Architekt: 
  - verantworlich das richtige zu machen
- Solution architekt: mache es richtig:

- **Unternehmens Architekt Disziplin**
  - schaut auf systeme (white box)
  - deren fähigkeiten
  - und es schaut auf alle systeme des unternehmens und betrachtet es als system (system von systemenen)
  - was bedeutet es für die bausteine des unternehmens
  - bausteine auf die es guckt, sind immer noch grob granular 
  - auf oberster ebene zerfällt unternehmen in divisionen (Domänen) am beispiel von novartis 

- **Domain Architekt**
  - Schaut so eine einzelne Domäne genauer an
  - Wie ist eine Domäne aufgebaut
  - Bsp Novartis: Generica, Vaxines, Pharma etc. 

- **Lösung Architekt**
    - Die Solution befindet sich innerhalb einer Domäne 
    - Ein Architekt der auf Lösungen innerhalb einer Domäne anschaut 
    - Die Disziplin auf der wir uns eher befinden (IT)
---
## System Architektur
- man kann alles system betrachten (Auto, Kirche, Bahnhof, etc.)
- Jedes System hat eine Architektur 
- Es gibt einen Grund für ein System
- Es kann eine inhärente Architektur und diese hat eine Beschreibung 
- Verbinden von Systemen erschafft weitere Systeme

- **IT-Systeme**
- bestehen aus:
  - Strukturen
  - Bausteine, statische und dynamische
  - Prinzipien und Guidelines
  - definieren das design und evaluation

- **System evolution**
  - System kann sich über Zeit verändern
  - Auch die Architektur kann sich mit der Zeit ändern
  - Wenn eine Änderung teuer ist, dann ist dies Architektur 

- **Architecture view models**
- Eine Viewmodel kombiniert isolierte Perspektiven
- Es gibt das sogenannte Sichtmodell, 4 Views + 1 Reality, auch das Kruger-Modell
- Anhand der Analogie "Stad Aarau" schauen wir 4 Views und 1 Reality an
  - **Map View**
    - Zeigt Aarau von oben, schwarz auf weiss, alles drauf
  - **Public Transport View**
    - Zeigt die Transport wege in Farbe
  - **Population Density View**
    - Zeigt die Bevölkerungsdichte in den einzelnen Stadtteilen
  - **Public Transport Buffer Zones**
    - Zeigt wie gut die Bevölkerung am Transportnetz angeschlossen ist, wieder in anderen Farben 
  - **Reality**
    - Ein echtes originales Foto von der Stadt Aarau von oben 

- Eine Beobachtung: 
  - Grosse Systeme evolvieren sich mit steigender Funktionalität, dass sie immer weniger agillität aufweisen
  - Man muss einen evolve-koridor machen, wo man sagt: nur in diesem bereich bewegen wir uns
  - also nicht einfach funktionalität steigern, man muss auch dagegen wirken damit die agilität nicht leidet
  - Das heisst konkret: Die Size ändern, archtekturische änderungen vornehmen

- Wo kommt Software Architektur hin?
  - System under Design kann man in folgende themen aufteilen:
    - uses case realization
    - system core: domain und technical model
    - quality attribute realizations
