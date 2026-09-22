---
title: "Week 02"
---

# Week 02 - Workload Management

[Drehbuch](https://sgi.pages.fhnw.ch/moduluebersicht/2026hs/sysd/drehbuch.html)
[Aufgaben](https://spd.pages.fhnw.ch/module/sysd/assignments/system-design/index.html)

---

## Onboard Kubernetes

- ![alt text](image.png)
- control plane für kubenretes eigene pods
- workernodes für eigenen workload pods
- cri, runc für pods starten stoppen
- kubelet macht das für uns, diese runtimes nutzen
- CNI für networking zwischen pods
- registry: liegt ausserhalb
  - OCI registry wo images liegen
  - wenn die nicht läuft, können keine images gezogen werden
  - heut zu tage, direkt bei start wird images gezogen
- wichtigste architektur komponenten

## Kubernetes Architecture

- ![alt text](image-1.png)
- CRI, contaienr run times zum starten stoppen von container
- CNI ist ein overlay network, eigenen i-adressen ranges
  - CNI zusatztool für cilium
  - network policy wo jedes CNI selber implementiert
- CSI für container storage interface
- in der cloud kommt CRI, CNI und CSI selber mit

## K8s Control Plane – Api Server

- ist quasi der API server
- kubectl, alle k8s services etc. kommunizieren über den API server
- technische accoutn, service account, persönliche account laufen über den API server

## K8s Control Plane - Scheduler

- ein control plane service
- scheduler sieht wenn wir einen pod starten, wo am besten den pod laufen lassen, auf welche node
- hat viel logik, zum schauen wo am meisten platz etc

## K8s Control Plane – Controller Manager

- scheduler entschiedet wo
- manager schaut das es auch effektiv wo es starten soll

## Reconciliation Loop

- ![alt text](image-2.png)
- in yml files beschreiben wir den desired state
- controller manager macht diesen loop, also er schaut nonstop was ist der desired state und macht änderungen damit er vorhanden ist
- k8s hat das für eigene pods gemacht
- man hat gemerkt das dieser loop extrem nützlich ist
- man hat angefangen ressourcen ausserhalb von k8s zu nutzen, aufgrund dieses loopes, weil so non stop sichergestellt wird, dass provisioniert wird
- controller kann man selber schreiben

## Kubelet

- kubelet ist wichtigste node agent der auf jedem node läuft

## etcd

- ![alt text](image-3.png)
- vorallem hochverfügbar ist etcd
- mehrheitsentscheid, es gibt immer 3 etcd mit leader election
- 3 weil, wenn einer stürzt haben 2 einen gleichen stand, wenn der 3. wieder kommt, ist klar welcher zustand der korrekte ist

## Interaction of components - "loosely coupled"

- ![alt text](image-4.png)
- alle dinge sind voneinander entkoppelt
- wenn irgendeiner dieser komponenten nicht läuft, läuft der rest weiter
- grund wieso es horizontal so gut skaliert
- k8s managed keine hardware und hat kein GUI

## K8s objects – main primitives

- ![alt text](image-5.png)

## Deployment

- im pod kann theoerisch mehrere container läufen, deshlab ist ein pod ein pod
- replicatset steuert zur runtime die pods, also wie viel etc.
- wenn im deployment steht replica, wird im hintergrund ein replicaset resource erstellt der dann konstant schaut, wie viele pods laufen müssen

## Service

- ![alt text](image-6.png)
- stellt eine virtuelle IP bereit
- default k8s loadbalancer ist ein Service
- im Service sage ich, für wen der Service gültig sein soll über selector
- er schaut nur auf labels

## Ingress

- ![alt text](image-7.png)
- eine öffung gegen aussen macht man mit Ingresscontroller
- ingress vs api gateway, ingress hat viele limitationen
- gateway API nehmen, mehr kontrolle, zertifikate etc.

## Multiple Containers in one Pod

- ![alt text](image-8.png)

## Networking

- ![alt text](image-9.png)
- k8s im default modus deployt und hochfährt kann jede komponente mit der anderen kommunizieren
- jeder pod bekommt eine ip
- alle pods mit pods reden ohne probleme
- default mässig ist alles offen
- ![alt text](image-10.png)
- dns thema ist wichtig
- ns übergreifende kommunikation nur über fqdn möglich
- innerhalb von ns kann mit serivcenamen kommuniziere

## Namespaces

- ![alt text](image-11.png)
- logische trennung
- limits und requests setzen
- mit limit range kann man das setzen

## ConfigMap & Secrets

- ![alt text](image-12.png)
- wenn wir dynamisch werte zur deployzeit unterschiedliche werte deployen will, dann sollen wir das mit variables machen
- das selbe für secrets
- nicht im container builden

## Context

- ![alt text](image-13.png)

## Troubleshooting application failures

- ![alt text](image-14.png)
- pullbackoff heisst image kann nicht gepullt werden
- crashlookback off heisst image kann gefunden werden aber nicht gestartet
- createcontainerconfigerror heisst config fehlt oder ähnliches

---

# Scalability Workload Management

## Deployment strategies

- default in k8s ist rolling deployment
  - nachteil ist, doppelte ressourcen
  - zwei versionen sind am laufen auf der infra
  - nur bei deployment macht er das, wenn es dann mal läuft nicht mehr
- recreate ist auch ein k8s standard
  - zuerst wird alles abgeräumt
  - auf knopfdruck sind alle neuen da
  - nachteil, unterbruch
- blue/green ist ein anderes
  - die neue version kann man alles hochfahren etc. testen und alles was man will
- canary
  - bestimmte user sehen die alte
  - nur ein ausgewählter teil sieht die neue version
  - sehr gut zum testen
- ![alt text](image-15.png)
- ![alt text](image-16.png)
- ![alt text](image-17.png)
- ![alt text](image-18.png)
- ![alt text](image-19.png)
- ![alt text](image-20.png)
- ![alt text](image-21.png)
- connectingworlds ist die komponente die es nur einmal geben darf

## Singleton Pattern

- ![alt text](image-22.png)
- mit singelton pattern kann man garantieren, dass es von einer komponente nur einmal geben darf
- ist ein bewährtes pattern
- auf k8s kann man das selber machen
- ein statefulset bauen statt replicatset bei k8s
- eine bisschen andere komponente
- stateful set kommt immer mit selbe ip hoch, immer mit selbe config hoch
- headless service: heisst eigentlich ein service ohne ip nix der schaut nur auf den einten service namen den ich in statefulset gesetzt habe
- ![alt text](image-23.png)

## Pod Disruption Budget

- ![alt text](image-24.png)
- wichtiges konstrukt ist dass wir ausserhalb von deployment konfigurieren
- geplante maintenance
- einstellen, dass nicht alle pods gleichzeitig herunterfahren auf node
- ein node rausnehmen, aber nur 2 pods max ausschalten mit ressource poddisruptionbudget (pdb)
- mit pdb kann man einstellen, ob eine node überhaupt jemals heruntergefahren werden sollen, wenn man anzahl auf 1 macht

## Workload – Automated Placement

- ![alt text](image-25.png)
- anhand nodeselector kann man bestimmte nodes auswählen, z.b mit ssd odr ähnliches
- ![alt text](image-26.png)
- ![alt text](image-27.png)
  - mit topology contraints kann man steuern balacing durch zonen
- ![alt text](image-28.png)
  - k8s macht kein automamtisches reblanacing
- im prinzip kann man mit diesen affinity rules und anti affinity topology spread etc. nur bei deployment steuern
- wenn es einen ausfall gibt, einfach sein lassen
- descheduler ist sehr selten in gebraucht

## Pod termination lifecycle

- ![alt text](image-29.png)
- pod wird auf terminating state gesetzt
- diese lifecycle undn diese punkte finden statt, wenn wir einen node herunterfahren, gezielt
- auch bekannt als graceful shutdown
- passiert beim gezielten herunterfahren, beim scalen, beim umziehen etc.
- die 30 sekunden sind dafür da, um noch irgendwelche commands auszuführen, speichern, umziehen was auch immmer
- irgendwann aber würde der cluster das aber erzwingen

## Signal Handling

- ![alt text](image-30.png)

## Workload – Stopping Gracefully

- ![alt text](image-31.png)

---

# Assignement 2

- zeigen, dass pods vom selben deployment auf verschiedenen nodes laufen
- part 4, graceful shutdown machen
- das goodby in log schreiben
