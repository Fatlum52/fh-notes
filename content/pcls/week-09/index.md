+++
title = "Week 09"
date = 2025-11-11
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

# Databases and Storage

## Recap Aufgabe

- Azure open-ai
- ein model deployen gpt4.1 mini
- azure openai sdk verwenden
- in roberta:
  - dependencie hinzufügen
  - azure open ai klasse importieren
  - dann instanzieren
  - client.chat.completion.create(...)
    - menge an message angeben
    - systemmessage mitgeben
  - response bekommt man zurück
- in eliza:
  - dependencie in pom file einfügen
  - damit hat man zugriff auf klassen
  - in eliza bei LLM service: implementation ausgetauscht

## Storage Concepts

- ![image.png](image.png)
- bei file können mehrere clients vorhanden sein
- block-storage:
  - disk an rechner anschliessen und nutzen
  - braucht ein file system
  - nicht über netzwerk ansprechbar
- blob storage
  - über API ansprechbar
  - allerelei dateien speichern (bilder, jsons, ...)
  - gibt extensions wie logs

## File Storage

- storage account erstellen wir in einer region
- danach kann man mit mehreren client und mehreren technologien darauf zugreifen
- mehrere clients + mehrere technologien
- ![image-1.png](image-1.png)

## File Storage - Pricing

- 3 key metriken
  - wie gross ist das share?
  - wie viel IOPS?
  - wie viel throughput?

## File Storage – AWS Elastic File System (EFS)

- ![image-2.png](image-2.png)
- file shares, einfach um über network erreichbar zu sein

## Block Storage

- ![image-3.png](image-3.png)
- disk kann man über mehrere availibility zone definieren
- block = disk
- disks werden an vms gehängt und dann läufts
- ![image-4.png](image-4.png)
- wichtige punkte für die auswahl:
  - latenz
  - IOPS
  - throughput

## Azure Managed Disk

- azure disk haben eigenen lifecycle unabhänig von VM
- snapshot von disk machen, mit snapshot command
- snapshot hat eigenen lifecycle
- wenn ich disk lösche, bleibt snapshort erhalten
- disk hängt an VM
- ![image-5.png](image-5.png)

## Block Storage – AWS Elastic Block Store (EBS)

- wenn ich eine disk nehmen mit viel IOPS und troughput, dann muss ich sicher gehen, dass meine VM das ab kann
- die vm kann limitationen haben
- ratsam prüfen, dass Disk und VM kompatibel sind

## Storage Products – Blob / Object Storage

- ![image-6.png](image-6.png)
- alle drei machen das selbe, nur anderer anbieter
- man redet von buckets

## Object / Blob Storage – Use Cases

- ![image-7.png](image-7.png)
- ![image-8.png](image-8.png)
- weiterer use case sind backups

## Azure Storage Account (ASA)

- ![image-9.png](image-9.png)
- im storage account kann man mehrere container mache, das sind die buckets
- da drin, dann daten ablegen
- was sie bringe, skalierbar
- S3 und Storage Acoount sind nur API's, hinten dran, wird es dann auf eine echte disk hinterlegt
- was sie bringen:
  - durability
  - scalability
  - security
  - availability: hochverfügbar
  - performance
- ASA muss unique benammselt sein
- ![image-11.png](image-11.png)
- Demo:
  - marketplace
  - storage account
  - region: suisse north
  - welchen type angeben
  - performance und rendundancy bestimmen
  - zone rendundant wählen
  - was wir haben wollen, https, http ...
  - anonymität einstellen
  - performance einstellen: hot, cool, cold

## Azure Storage Account - Redundancy

- ![image-12.png](image-12.png)

## Azure Storage Account - Concurrency

- ![image-13.png](image-13.png)

## Azure Storage Account – Lifecycle Policies

- ![image-14.png](image-14.png)
- ich kann regeln für die lifecycles festlegen
- bsp: nach 180 tagen sollst du es löschen
- umso mehr daten, umso mehr zahlen, deshalb bringt es, diese zu löschen

## Azure Storage Account – Access Tiering

- ![image-15.png](image-15.png)

## Azure Storage Account - Emulator

- dort kann man den storage lokal testen

## Azure Storage Account - Permissions

- objekte kann man anonym zugreibar machen
- wenn nicht anonym kann man steuern wer zugreifen kann
- man kann das mit SAAK = storage account access keys machen

## Azure Storage Account – Permissions for Blobs – Blob Access Level

- ![image-16.png](image-16.png)

## Azure Storage Account – Permissions for Blobs – Access Keys

- ![image-17.png](image-17.png)
- keys auf verschiedenen ebenen erstellen, für verschiedene zugriffe

## Azure Storage Account – Permissions for Blobs - EntraID

- ![image-18.png](image-18.png)
- mit entra kann man sage, was der user darf, wenn er sich einloggt
- azure entra ist praktisch

## Azure Storage Account – Dataimport

## Azure Storage Account – Pricing

- wir zahlen pro benutzen GB
- preis pro GB in cool oder cold wir günstiger
- zugriffe kosten
  - read operations pro zugriff

## Storage – Summary

- ![image-19.png](image-19.png)

# Datenbank

## Why Cloud Databases?

- ![image-20.png](image-20.png)

## CAP-Theorem

- ![image-21.png](image-21.png)

## Consistency

- alle nodes returnen die selben daten

## Availability

- alle nodes können antworten, ohne untereinander ab zu sprechen
- wenn sie keine verbindung haben, dann unterschiedliche date

## Partition Tolerance

- unterbrüche zwischen nodes
- was für daten geben sie zurück, wenn sie nicht mehr synchron sind

## Implications on distributed systems

- ![image-22.png](image-22.png)
- wir müssen uns entscheiden, welche zwei wir haben wollen

## Summary CAP

- Datenbanken funktionieren nach CAP

## Database Classification

- ![image-23.png](image-23.png)
- ![image-24.png](image-24.png)
- ![alt text](image-25.png)

## ACID vs BASE

- ![alt text](image-26.png)

## Relational Databases

- ![alt text](image-27.png)

## Hosting on Azure

- ![alt text](image-28.png)

## Azure Database for PostgreSQL Flexible Server

- ![alt text](image-29.png)

## Azure Cosmos DB for PostgreSQL

- ![alt text](image-30.png)
- es werden immer wieder services deprecated

## NoSQL Datenbanken

- ![alt text](image-31.png)
- nutzen wenn schwaches schema

## Eventual Consistency

- ![alt text](image-32.png)
- ![alt text](image-33.png)

## Cosmos DB No-SQL

- ![alt text](image-34.png)

## Cosmos DB - Pricing

- ![alt text](image-35.png)

## Cosmos DB – Postgres API

- ![alt text](image-36.png)

## Cosmos DB – SQL API

- ![alt text](image-37.png)

## Summary DB Services

- ![alt text](image-38.png)

## Demo: CosmosDB with Functions

-

## Databases - Summary

- ![alt text](image-39.png)
