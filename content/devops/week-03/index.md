+++
title = "Week 03"
date = 2025-09-29
[taxonomies]
authors = ["fatlum"]
tags = ["devops"]
+++

## Reflektion Assignement 2
- 12-faktor-app
  - wichtig für die schriftliche prüfung -> anschauen vor der prüfung!!
- security-flaws schnell adressieren im service
- 9 wichtigsten funktioanlitäten erfassen
- git tag machen und das soll system triggern für einen release
- nächste woche die lösung containerisieren

## Introduction, why docker?
- ganze anwendungsschicht als artefakt bauen, sodass es auf jedem OS laufen kann
- portabilität, OIC-kontainer darauf ausgelegt von A nach B zu wandern
  - idee wie es funktioniert ist steinalt
- reproduzierbarkeit, einfacher syntax für ein dockerfile
- container virtualisieren keine software!
- grundidee von CI/CD gab es schon vor Docker
- mit container ist CI/CD viel generischer 

***where does it come from?***
- VM model:
  - app läuft auf os, vm läuft auf hypervisor und diese läuft auf hardware von host
- container model:
  - die apps werden isoliert und laufen nativ auf server
  - eine app wird wie ein prozess behandelt
  - shell und application-schicht wird von docker abgenommen, läuft in einem container
- ![img.png](img.png)
- container gedacht auf rezept zu erstellen

***linking to cloud, para-virtualization***
- idee ist sehr alt
- ein container ist eine gruppe von prozessen
- ein normlaer container hat keinen eigenen kernel und laufen auf anwendungsschicht
- es möglichkeit container bootable zu machen
- brauchen weniger ram, sind sehr schnell
- container startet, wenn prozess dahinter startet 
- bei vm zuerst systemd danahc timer starten etc. 
- vm sind besser isoliert, bei container ist es abhängig von runtime 
- docker runtime kann man rootrechte geben, wenn man root-volum darin mountet
- schwiriger zu entscheiden wann contaienr verwenden wann nicht
- ein prozess ein image und ein container ist best practice

***OCI-container/images***
- docker war nicht mehr als frontend für NIC
- Imagespezifikation und runtime spezifikation, darin steht wie sie aufbeaut werden müssen

***wie läuft es?***
- ![img_1.png](img_1.png)
- wenn man auf oberste schicht etwa baut, muss es augrund von spezifikation in kubernetes laufen
- in wirklichkeit redet man über OIC-Images und nicht dockerimages

***Dockerfile and Dockerimages***
- ![img_2.png](img_2.png)
- FROM, COPY, RUN, CMD
- standard containerisieren mit dockerfile
- alles was im baseimgae ist ist im dockerimage auch drin
- pro linie ist ein layer
- mit 4 lines of code bekommt man eine anwendungsschicht, eine app im container

***immutable software***
- ![img_3.png](img_3.png)
- jedesimage zieht ein weiteres image hinterher 
- wenn im tiefsten image etwas kapput geht, badet man es bei der app aus 
- wir patchen keine software im laufenden container!!!

***grundidee eines containers***
- ![img_4.png](img_4.png)
- isolation der abhängigkeiten 
- in der gesames anwendugnsschiht ist alles drin was ich brauche, also auch verschiedene abhängigkeiten 
- nachteil:
  - mehr speicher
  - ein mechanismus der regelmässig monitort, die verschiedene abhängigkeit
  - man müsste manuell die images patchen
  - automatisiertes testing, lifecycle management um dieses problem zu beheben 

***Images and Container***
- ein image ist ordner auf einem dateisystem
- ein staack von snapchats eines dateisystem die man übereinander legt
- pro layer schaut er ob image änderungen hat
- wenn container beendet, image steht noch 
- grundsätzlich container immer remove
- workflow:
  - lokal image bauen im gitlab CI, danach build prozess pusht die einzelnen layer (jedes layer eine hashsumme), und dann pullt docker
  - wenn layer vorhanden sind, lässt es, pull nur die neuen layer
- images richtig generieren 

***detailed view of layer***
- ![img_5.png](img_5.png)
- wenn mehrere images, gleiche baseimage verwenden 
- überlegen wie dockerfile aufbauen
  - grosse elemente weiter unten im OIC-image
  - elemente die häufig ändern, eher in obere layer
- bei chatbots: LLM wo im image stehen: möglichst weit unten 
- was braucht man wirklich? kleine baseimages machen 
- bsp java app:
  - zum entwickeln braucht man JDK, zum laufen lassen nur runtime
  - maven braucht man nicht zum starten, nur java
- das was hier drauf steht ist für containerisieren sehr wichtig 
- kleine images zur runtime, nur was man braucht 