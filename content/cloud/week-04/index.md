+++
title = "Week 04"
date = 2025-10-10
[taxonomies]
authors = ["fatlum"]
tags = ["cloud"]
+++

[Drehbuch](https://sgi.pages.fhnw.ch/moduluebersicht/cloud/drehbuch.html)  
[Aufgaben](https://spd.pages.fhnw.ch/module/cloud/platforms_site_generated/cloud-reports/hs25/index.html)

Abgabe zweites Projekt: **30.10.2025**

---

## Container

***What is a container?***

- proxomos sind emulatoren
- cotainer sind ein anderer ansatz
- datei system, ressourcen und prozessraum nutzen
- container muss nicht aus images bestehen

---

***Containers are disruptive…***

![image.png](image.png)

- egal was drin läuft (workload) kann ich nehmen und auf maschine laufen lassen
- so bekommt man basis für agile software entwickelt
- nicht mehr als ein linux prozess
  - hat overhead eines prozesses
- container nimmt ganze Anwedungsschciht(AS)
  - abstrahiert hardwarde und kernel
- problemlos provisioniere, starten, stopp etc.
- gegensatz zu VM, kein systemd, bootprozess etc.
- horizontal skalieren geht instant
- sehr portabel
- gesamte AS zippen und übers netzwerk schieben
- alles ist drin, libs, packages etc.

---

***… but what are containers?***

- ![image-1.png](image-1.png)
- nutzen so viel ram wie auch der prozess ram braucht
- starten schneller weil ohne startprozess, systemd etc.
  - kann jeder prozess sein, java, python...
- eine vm ist isoliert, aus vm auszubrechen ist schwer
- bei container kann man durch falsche verwendung sicherheitslücken erschaffen
- bsp: filesystem kann man rein mounten
  - docker run ubuntu:latest /:/opt
    - ich maunte das ganze root verzeichnis in /opt
- aus container kommt man leichter raus als aus vm
- schwer zu wissen, was man in einem container alles machen kann
- immer nur einen prozess in einem container

---

***We all us Docker …***

- ![image-2.png](image-2.png)
- läuft auf einer container engine dann

---

***Containerization VS Virtual Machines***

- ![image-3.png](image-3.png)

---

***Recap: Paravirtualized Environments***

- ![image-4.png](image-4.png)

---

***Containerization***

- ![image-5.png](image-5.png)
- das zeig ist stein alt
- verschiedene level:
  - app level
  - os level
- kann container so bauen dass sie ein komplettes os haben
- erster prozess der gestartet ist, war ein systemd
- in container kann man jeden prozess rein schreiben

---

***Under the hood: What is a container?***

- ![image-6.png](image-6.png)
- docker container nach start oder stopp löschen
- erst dann ist prozess echt gestoppt
- container soll lebel wie ein prozess

---

***Such containers are ooooooooooooold***

- docker war (2013) eigentlich nicht mehr wie ein frontend das LXC nutzt

---

***How to implement a Container from scratch?***

- ich brache drei sachen changeroot, namespaces, cgroups
- chroot:
  - sagen wo der neue root ist
  - irgendwo im host file system liegt das filesystem von einem container
- namespaces:
  - mit chatgpt ergänzen
- cgroups:
  - sagen er soll nur bestimmte anzahl cpu's haben
  - mit chatgpt ergänzen

---

***Chroot***

- ![image-7.png](image-7.png)
- ![image-8.png](image-8.png)
- man kann sagen wo das neue root liegen soll

---

***Cgroups***

- ![image-9.png](image-9.png)
- regeln die ich fest lege
- diese regeln sind festgelegt in dateien
- kann in hirarchie festlegen
- wie schaut so eien aus?:
  - ![image-10.png](image-10.png)
- ab jetzt langsam durch man pages navigieren
- hirarchie of file system:
  - ![image-11.png](image-11.png)
- cgroup geht auf prozess
- jetzt kann man für einen prozess einen bestimme cgroup erstellen, z.B. um weniger CPU zu bekommen
- wir müssen solche auslastungen mit LXC auf der plattform machen

---

***Namespaces***

- ![image-12.png](image-12.png)
- ![image-13.png](image-13.png)
- virtuelles filesystem auf linux
- neu was container machen:
  - prozesse kann man clustern
  - p6 bist jetzt in einem eigenen namespace, du denkst du bist p1, auf host ist er es aber nicht
- prozesse können geclustert werden
- können sagen prozess läuft in eigenem namespace
  - bekommt eigene cgroup
- ![image-14.png](image-14.png)
- ![image-15.png](image-15.png)
- ![image-16.png](image-16.png)

---

***Putting it all together, lxc/lxd***

- ![image-17.png](image-17.png)
- lxc ist command-line interface

---

***Docker***

![image-18.png](image-18.png)
