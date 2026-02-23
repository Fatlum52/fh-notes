+++
title = "Week 07"
date = 2025-10-28
[taxonomies]
authors = ["fatlum"]
tags = ["pcls"]
+++

[Drehbuch: Modulübersicht PCLS – Drehbuch](https://sgi.pages.fhnw.ch/moduluebersicht/pcls/drehbuch.html)  
[Gitrepo: spd/module/pcls (GitLab)](https://gitlab.fhnw.ch/spd/module/pcls/)  
[Assessments / Assignments: Public Cloud Services – HS25](https://spd.pages.fhnw.ch/module/pcls/tutorials/assignments/public-cloud-services/hs25/index.html)  
[Report: Assessments Pages (Ordneransicht)](https://gitlab.fhnw.ch/spd/module/pcls/tutorials/assignments/-/tree/main/modules/assessments/pages/)  
[Switch Engines](https://engines.switch.ch/) · [AWS SSO](https://fhnw.awsapps.com/start/#/?tab=accounts) · [Azure Portal](https://portal.azure.com) · [O’Reilly-Playlist](https://learning.oreilly.com/playlists/a27d30d7-f139-4476-9c3a-e0abeb0f89da/)

---

# K7 Function as a Service

## Motivation

- abstraktion in infra einbringen
- mehr verantwortung an provider geben
- mit faas auf spitze getrieben
- mehr um appli logik kümmern

## Function as a Service - Fundamentals

- ![image.png](image.png)
- on prem, alles in seiner verantwortung
  - racks bestücken, welche software
- function ordnet zwischen saas und paas ein
- weniger maintenance, weniger overhead um die lösung zu betreiben

## Function as a Service – Serverless

- ![image-1.png](image-1.png)
- keine mainteneace, upgrad etc.
- nicht kümmern wie viel server
- no cost without traffic
- wenn code nicht gebraucht wird, auch keine kosten
- fokus auf functions
- datenbanken geht auch serverless
  - kurzzeitig als function ausgeführt

## Function as a Service – Fundamentals

- ![image-2.png](image-2.png)
- functions sind code schnippsel
- müssen getriggert werden, durch events
- events können functions triggern
- können auch timeevent sein
- ![image-3.png](image-3.png)

## Function as a Service – Serverless Pipeline

- ![image-4.png](image-4.png)
- serverless im sinn von jemand anders hostet server
- um functions laufen zu lassen braucht es code
- runtime lauscht auf die funktion
- function instances, wenn keine bedingung da ist um sie zu fahren, werden sie offline genommen
- ein github webhook kann auch ein event sein

## Function as a Service – Serverless Pipeline with Tooling

- ![image-5.png](image-5.png)
- build wie buildpacks oder cloud build

## Function as a Service – Runtimes

- azure function unterstützen je nach langugae runtimes
- deployment wie docker container oder zip

## Azure Function Deployment Plans

- ![image-6.png](image-6.png)
- consumtion plan -> wenn nichts läuft, zahlt man nichts
- premium plans zum optimieren, cold-start etc.

## Function as a Service - Challenges

- kurzlebig, ragieren auf event, löschen sich wieder
- functions haben kein state, also speicher wird gelöscht
  - mit datenbanken, s3  kann man state handling
- coldstart ist grosses problem
  - wenn memory geladen werden müssen
- orchestrierung ist ein problem
- das gesamtkonkstrukt muss überwacht werden
- std. functions geht das nicht
  - durable oder set functions sind für das

## Function as a Service – Use Cases

- ![image-7.png](image-7.png)
- scheduled tasks:
  - alle 24h aufräum arbeiten in db machen?
  - funktion startet, räumt auf, löscht sich wieder
- streaming:
  - kafka von azure, einzelne events hineinlegen
  - stark parallelisieren
  - wenn kein event, passiert einfach nichts
- file processing:
- gemeinsam:
  - ein zentraler punkt wo alles jobs ausgeführt werden

## Function as a Service - Scenarios

- ![image-8.png](image-8.png)
- eine function könnte jede function machen
- orchestrierung mit fanning
- aufpassen wie gross functions sind, welche abhängigkeiten etc.
- nicht zu micro, also nicht zu viele functions machen
  - logisch kombinieren, mit sauberer architektur

## Service-Offerings, Tools und Solutions – Categories

- low-code plattformen: logic apps
- chatbots funktionisieren
- kubernetes basierte run time gibt es auch

## Service-Offerings, Tools und Solutions – Landscape

- ![image-9.png](image-9.png)

## Service-Offerings, Tools und Solutions – Technical Baseline

- ![image-10.png](image-10.png)
- als konsument gibt man code her und wie es funktioniert ist sache des providers
- aws firecracker: kleine vms und orechstriert die
- immer mehr abstraktion, das heisst immer mehr auf konzepte achten

## AWS Lambda in Comparison to Azure Functions

- native code hochladen
- hohen lock-in

## SDKs and Code-Integrations with Python on Azure

- ![image-11.png](image-11.png)
- wenn man die ausführt, wird die main ausgeführt
- ![image-12.png](image-12.png)
- azure erwartet eine functionApp in dem functions drin sind

## SDKs and Code-Integrations with Python on AWS

- die schnittstellen sind im pyhton anders
- files heissen anders

## SDKs and Code-Integrations with Python on Knative

- als container in kubernetes laufen lassen
- gibt genügend webframeworks

## Azure Functions Authentication and Authorization

- ![image-13.png](image-13.png)
- function für eine gewisse ip-range freigeben
- jeder function eine identität geben
- function kann über identität andere functions rein schreiben

## Azure Functions Networking

- ![image-14.png](image-14.png)
- public networking auf private umstellen
- das ist traffic der in die function einfliesst
- VNET integration um intern mit anderne functions kommunizieren
- untere kombination nutzen, obere nicht
- chatbots han private endpoint
- connecting-worlds hat public endpoint mit VNET integration

## Function as a Service – Walkthrough/Demo

- portal.azure.com
- function app suchen
- create
- flex consumption auswählen
- subscirption wo man ressourcen hat
- namen eingeben
- region auswählen
- runtime stack auswählen
- instance size -> 2GB
- weiter
- storage account wird auto erstellt
- networking:
  - public oder einschränken
  - cw public, chatbots private
- monitoring:
  - appllication insights
  - wie viel user sind aktiv, welche seite am meisten aufrufene etc.
- deploymet:
  - kann auf webhooks lauschen -> github, überwacht den branch
- authentication
- erstellen
- man kann eien queue anlegen

## SDKs and Code-Integrations – Links

- Native Python Azure Functions SDK:
<https://learn.microsoft.com/de-de/azure/azure-functions/functions-reference-python?tabs=get-started%2Casgi%2Capplication-level&pivots=python-mode-decorators>
- Fastapi Example: <https://learn.microsoft.com/en-us/samples/azure-samples/fastapi-on-azure-functions/fastapi-on-azure-functions/>
- Quarkus Example: <https://quarkus.io/guides/azure-functions>

## Error Handling

- ![image-15.png](image-15.png)
- kann execption werfen und der runtime sagen wie damit umgehen
- open telemetry verwenden
- func. runtime sammelt recht viel
- eigene metrics erfassen

## Durable Functions on Azure

- ![image-16.png](image-16.png)
- function die andere functions überwacht
- wenn prozess gestratet wird, werden die functions 3 mal ausgeführt, nachdem wie man gecoded hat
- status tracking wurde gestartet
- status von duarbel function ansehen
- wenn function host gestartet/gestoppt wird, bleibt zustand trotzdem

## Step Functions in AWS

- ![image-17.png](image-17.png)
- äquivalent zu durable functions von azure
- workflow werden via statemachine gemapped
- mehr als nur lambdas

## Local Development with Azure

- azure cli und vs-code plugins fürs debuggen

## Azure Functions Deployment Options

- vscode
- cli
- services-managed -> git push
- via CI/CD

## Function Deployment in Azure

- ![image-18.png](image-18.png)
- 4 ebenen
- mgmt. group schauen wir nicht an

## Deployment via Terraform in Azure oder BICEP

- ![image-19.png](image-19.png)
- ![image-20.png](image-20.png)
- ![image-21.png](image-21.png)
- ![image-22.png](image-22.png)

## Deployment via Infrastructure as Code in Azure

- ![image-26.png](image-26.png)

## Deployment via Code/CLI in AWS

- ![image-27.png](image-27.png)

## Cold Starts

- ![image-28.png](image-28.png)
- grosses problem bei faas
- kann warm functions dazu kaufen, dass die schon ready sind

## Azure Functions Pricing

- ![image-29.png](image-29.png)
- always ready aktivieren, heissen diese warm functions
- ich kann angeben, wie lange ich diese warm behalten will
- ab x sekunden, soll sie aus memory raus

## Restliche Folien

- ![image-30.png](image-30.png)
- ![image-31.png](image-31.png)
- ![image-32.png](image-32.png)
- ![image-33.png](image-33.png)
- ![image-34.png](image-34.png)
- ![image-35.png](image-35.png)

## Hausaufgaben

- angeben, wie die function sich die images holen sol von gitlab
  - via trigger
