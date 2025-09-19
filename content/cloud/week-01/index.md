+++
title = "Week 01"
date = 2025-09-19
[taxonomies]
authors = ["fatlum"]
tags = ["cloud"]
+++

## Learning target
- technisches wissen über cloud technologien 
- wissen über die konzepte der darunter liegenden technologie
- selber plattform aufbauen, 
- verstehen was es braucht eine cloud zu builden

## Vorlesungsstruktur
- IaaS:
  - virtualisieren
  - Lab: Proxmox
- PaaS:
  - container, paravirtualisieren
  - Labs: container, docker, swarm, kubernetes
- SaaS:
  - Storage
  - Lab: Ceph Storage

***Lecture (on-site)***
  - normal lecture:
    - kein recording
  - BSS: Lab-Session
    - wir builden cloud plattformen
    - in 4 sessions, kein aktiver content 

***Assessment: building platforms***
    - keine wöchentliche hausaufgaben
    - wir bauen 4 platformen
    - zu jeder platform einen individuellen screen cast 
    - jede platform -> 12.5% zur Erfahrungsnote
    - 50% schriftliche prüfung 
    - zusammen builden mit gleiche anteil

***Daten***
    - Proxmox(IaaS)
      - Duration: 26.9 - 9.10
      - BSS: 3.10.
    - Container, Docker Swarm (Paas)
      - Duration: 17.10 - 30.10
      - BSS: 24.10.
    - Container, Kubernetes (PaaS)
      - Duration: 
      - BSS: 14.11.
    - Storage, Ceph (SaaS)
      - Duration: 28.11. – 11.12.
      - BSS: 5.12.

***Wie Gruppenarbeit***
      - 1er-3er Gruppen

***Motivation***
- coud market wächst
- software eats infrastructure
- IaC (Infrastructure as Code) tools werden brauchbar
- shiftleft, also der dev muss sich immer mehr in cloud und weiteres auskennen
- 3 Sache für AWS-Server
  - Geld, Email, Internet

# Frontaler Unterricht T1
***history of cloud computing***
- 1960, mainframe:
  - alte computer architektur
  - timesharing, man konnte mehrere SW gleichzeitig laufen lassen
- 1969, ARPANET:
  - vorläufer des internets
- 1970, virtualization
- 1997, cloud computing
- 1999, saleforce, cloud kam dazu 
- 2006 amazon launches Elastic Compute cloud (EC2) und Simple Storage (S3)

***Cloud Computing***
- es gibt keine cloud, es ist nur der computer von jemand anderem, bzw. die rechenpower von jemand anderem
- 5 charakterisikten
  - on-demand self-service: ressourcen werden provisioniert ohne human interaction
  - broad network access: muss zugänglich über internet sein
  - ressource pooling: ressourcen werden mehreren nutzer zur verfügung gestellt
  - rapid elasticity: exestierende ressources können wachen oder shrumpfen dynamisch
  - measured service: der usage kann genau gemessen werden und dann verrechnet, pay-as-you-go

***How can clouds be provided? - Cloud Deployment Models***
- private cloud für eine einzelne organisation
  - innerhalb der firewall
  - third-party managed die cloud
  - skaliert nicht so gut wie public cloud (oft nicht eine echte cloud)
- public cloud for the general public
  - multi-tenant
  - allgemeiner nutzen
  - keine volle kontrolle über die daten -> confindential compute
- Community Cloud for organizations that have shared concerns (e.g., government, universities), wie unsere switch
- hybrid cloud 
  - kaum zu sehen, da unternehmen 1-2 public cloud haben und ihre on-prem server physisch vor ort sind, was keine cloud ist

***Services***
- wenn ich PaaS anbieten will, nutze ich IaaS für mich selber
- wenn ich SaaS anbieten will, nutze ich eine PaaS
- die grenzen sind verschomme, wo IaaS anfängt und bis wo und das selbe für PaaS
- fragen um zu entscheiden ob IaaS, PaaS, SaaS
  - muss ich OS selber managen, auswählen etc.? -> IaaS
  - muss ich selber code? -> SaaS
  - wenn OS, virtualisierung gegeben sind -> PaaS

- ***IaaS***
  - beinhaltet vorallem das physische, also network, storage, compute, virtualisierung
  - oben durch ist seine verantwortung

- ***PaaS***
  - network, storage, compute, virtualiserung, OS, Tools & Libraries, Application Runtime wird vom provider geliefert
  - der customer bringt nur noch daten und die app selber
  - am meisten verbreitet

- ***SaaS***
  - provider der sw managed alles
  - da kann man selber keine code mehr schreiben

    
## Fragen
- What is ARPANET?
- You need to migrate windows-instances to your new cloud. What level of service class are you
  using on the new cloud?
- What types of clouds are existing according to NIST?
- What necessary criterias exists for clouds according to NIST?
- Why are the denoted cloud layers much less dependend on each other than the layers from the
  OSI model?
- The following tech stack is given: map the elements of the tech stack to the cloud layer model:

# Frontaler Unterricht T2
- abstraction vs virtualization
  - abstraction
    - das tiefere level verstecken
    - OS macht das oft
    - ein file ist eine abstraktion eines storageblock auf der festplatte
  - virtualization
    - virtuelle repräsentation einer ressource
    - nichts ist versteckt
    - volle flexibilität über speicher und weitere komponente

***VM***
- process virtual machine
  - keinen typischen rechner
  - benutzt intermediate language, java byte code
  - bsp.: JVM
- system virtual machine
  - probiert die ganze hardware to mimic
  - example: Xen, KVM, VMWare
- wir fokussieren uns auf type 1 hypervisor 

***Anforderung für Virtualisierung***
- möglichst weniger overhead, gute performance
- resource control (safety)- isolation zwischen guests und von guest zu host
- equivalence - gleiches ergebnis mit und ohne VMM
- wichtigkeit von virtualization: von ressource pooling

***Hypervisor type 1***
- volle virtualisierung von nutzung von binary translation
- x86 privilege rings
  - ![img.png](img.png)
  - x86 CPU hat vier protection rings
  - nur code in mehr priviled rings kann auf weniger priviledged rings zugreifen
  - ring 0:
    - level mit meisten privileg
    - interagiert mir hardware
  - Full Virtualization using Binary Translation (Type I)
    - jede instruction wird umgeschrieben, sodass auf hardware zugegriffen werden kann
    - vorteil: direkte ausführung von user-level code -> high performance 
    - nachteil: schwierig zu implementieren VMM
    - übersetzung hat impact auf performance (virtual memory → physical memory → machine memory)
    - komplextität aus hypervisor auslagern: ins guetOS oder direkt in die hardware

Nächstesmal: 02-1 - cloud - Virtualization.pdf auf seite 14
