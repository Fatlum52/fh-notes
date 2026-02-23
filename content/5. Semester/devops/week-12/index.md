+++
title = "Week 12"
date = 2025-12-01
[taxonomies]
authors = ["fatlum"]
tags = ["devops"]
+++

- [📘 Aufgaben – DevOps Foundations HS25](https://spd.pages.fhnw.ch/module/devops/templates/reports/devops-foundations/hs25/index.html)
- [Drehbuch](https://sgi.pages.fhnw.ch/moduluebersicht/2025hs/devops/drehbuch.html)
- [☁️ Azure Portal (AKS)](https://portal.azure.com)
- [🦊 GitLab – FHNW DevOps Projekte](https://gitlab.fhnw.ch/spd/module/devops)

---

# K12

## Availability and SLOs

## Recap: Reliability is the most important feature

- ![alt text](image.png)
- verfügbarkeit wiederspiegelt zugriff auf ganzes netz
- wir wollen an metric messen, ohne das es kunde mitbekommt
- wenn nutzer mitbekommt, dann ist es zu spät
- mit monitoring weiss man etwas fix

## What 99.999 really means…

- ![alt text](image-1.png)
- pro jahr, eine downtime von 5 minuten
- wenn jemand solche verfügbarkeiten verspricht, immer skeptisch sein
- aws verspricht es 99.5%

## Want VS Need

- ![alt text](image-2.png)
- hohe verfügbakreit, kostet richtig viel geld
- technische schuld ist hauptverursacher, für niedrige verfügbarkeit

## 99.999% really possible?

- ![alt text](image-3.png)

## Availability, Sequentiel Availabilty

- ![alt text](image-4.png)
- seriell aufschalten (sequentiell)
- services schlau hintereinander kombinieren

## Availability, Parallel Availabilty

- ![alt text](image-5.png)
- parallel aufschalten
- das ist der grund wieso man horizontal skaliert
- das kommt in klausur

## Chaining of Availability

- ![alt text](image-6.png)
- zuerst linken cluster ausrechnen, dann rechten

## Availability, Parallel vs Serial

- ![alt text](image-7.png)
- ein email service lauft eher parallel
- dinge die persistieren, einen state haben, lassen sich schwer parallelisieren
- in architektur gibt es immer dinger die sequentiell laufen
- da wo man nicht paralleliseren kann, sollte man auskoppeln

## 99.999% is expensive

- ![alt text](image-8.png)
- alle komponenten doppelt
- wenn man das so macht, kann man nicht für persistenz garantieren

## Caveats of common Availability Assumptions

- ![alt text](image-9.png)
- wenn man das so macht, kommt man auf 88%

## SLA?

- ![alt text](image-10.png)
- was ist die verfügbarkeit? ist es ein ping, latenz...
- SLA von einem pull, muss viel höher sein als sonst

## SLI (Service Level Indicator)

- ![alt text](image-11.png)
- "Der pull muss inneerhalb von einer sekunde stattfinden"

## SLO

- ![alt text](image-12.png)
- von 5 pulls, müssen so viel und so viel erfolgreich sein
- nimm den SLI und binde den an Schwellwert
- Alert fatigue:
  - alerts die zu häufig kommen, klickt man einfach weg
  - wenn schwellwerte zu streng sind, schaut man die logs garnicht mehr an

## Target for SLOs

- ![alt text](image-13.png)
- ich will LB montioren, monitore ich webseite
- verschiedene SLO's monitoren

## Example for SLOs

- ![alt text](image-14.png)
- kein mittelwert, mittelwert isch schwer für metriken
- mittelwert zeigt keine ausreisser an

## SLA

- ![alt text](image-15.png)

## Putting it all together

- ![alt text](image-16.png)
- inikators mit schwellwerten
- SLI und SLO definiert man technisch
- SLA sind dann manager sache

## Recap: Accelerate the flow

- ![alt text](image-17.png)
- je weniger änderungen umso stabiler
- mainframe läuft sehr stabil
- zweit stabilste system ist das mit vielen änderungen
- viele änderungen = kleine diffs
- kurze schnelle releases, sorgen dafür, dass die letzte änderungen vor 2-3 wochen war

## Dora Metrics

- ![alt text](image-18.png)
- lead time: zeit bis ein feature erfasst ist und in produktion kommt
- deoloyment freq: wie oft deploye ich, wie oft rolle ich aus
- change fail: wie häufig mache ich fehler in prod
- time to restore: zeit um fehler zu beheben
- availability: wie sehr ist mein zugriff gewährleistet
- die metriken sind wiedersprüchlich
- leadtime runter, deployment freq. hoch, könnte changefail erhöhen

## Error Budgets

- ![alt text](image-19.png)
- stabilste systeme sind die ohne änderungen
- ![alt text](image-21.png)
- ![alt text](image-22.png)
- ![alt text](image-23.png)

## Error Budgets not spent

- ![alt text](image-20.png)
- in praxis ist ein managment wichtig, dass das versteht
- wenn SLO's aufgebraucht sind, muss man irgendwo etwas einstellen z.b. features oder anderes

## SLOs and Upper Bound

- ![alt text](image-24.png)
- kann auch eine obere quelle sein, nicht nur untere
- kontinuierlich, fehlerquellen einfügen um zu schauen ob systeme verheben
- das nennt man chaos engineering

## Best practices for SLIs/SLOs

- ![alt text](image-25.png)
- definier einen SLO von unseren chatbots
- SLI kombinierbar mit SLO

# Operational Basics

## Basics of Operations

- ![alt text](image-26.png)
- how do you handle deploys?
  - alles auf dev, wenns läuft auf prod
  - übergabe via registry
  - buy software mit docker compose
  - dockerfile als übergabe
- How do you "operate" (handle the time between deploys)?
  - monitoring auf endpunkte
  - kunden monitoren
  - dokumentation (Wiki)

## Basics of Operations, IT System Management

- ![alt text](image-27.png)

## Paradigm Switch to Products

- ![alt text](image-28.png)
- zentralisiertes changemanagement grosses thema in itsm
- change monitoring aufsetzen
- incident management auch grosses thema in itsm

## Paradigm Switch to "release often, release early"

- ![alt text](image-29.png)
- eine kultur aufbauen, wo man fehler transparent behandelt

## Paradigm Switch to "you built it, you run it"

- ![alt text](image-30.png)
- dev in support einbinden

## Recap: Conways Law

- ![alt text](image-31.png)
- technische architektur bildet sich auf organisatorische architektur
- bei disjunkten teams, geht es langsamer bei fehler incidents

## API-Management

- ![alt text](image-32.png)
- es braucht zentrale schnittstellen, damit teams zusammearbeiten können

## Innersource and Shared Responsibility

- ![alt text](image-33.png)
- es braucht synergien
- betrieb ist bei einem team, aber alle können daran arbeiten

## Monitoring and Observability

- ![alt text](image-34.png)
- labels verwenden
- skalierbare technologien verwenden

## Changemgmt vs Changemonitoring

- ![alt text](image-35.png)
- es nimmt changes war

## Continuous, Automatic Deployment

- ![alt text](image-36.png)
- alles was man 1-2 mal pro quartal macht => weg automatisieren
- only source of truth machen

## Deploys might be part of a bigger game

- ![alt text](image-37.png)

## Recap: Dev/Prod Parity, 12factor

- ![alt text](image-38.png)
- team vollständig verantwortung innerhalb des teams

## Recap: Websphere Deployment

- ![alt text](image-39.png)
- manuelle übergänge verhindern

## Staging and Namespaces

- ![alt text](image-40.png)
- einfachste weg auf kubernetes

## Incident Management by ITIL

- ![alt text](image-41.png)
- wenn viele tickets zum gleichen Thema kommen, wird es ein major incident
- major incident, beudeutet, eine person kümmert sich direkt um den incident
- verantwortung sollte bei den product shippern liegen

## Incidents managed by DevOps

- ![alt text](image-42.png)
- kommunikationskanäle überlegen die auch ausfallen können

## Summary

- ![alt text](image-43.png)
