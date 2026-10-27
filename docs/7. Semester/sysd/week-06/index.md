---
title: "Week 06"
---

# Week 06 - Queues and Pub / Sub

[Drehbuch](https://sgi.pages.fhnw.ch/moduluebersicht/2026hs/sysd/drehbuch.html)
[Aufgaben](https://spd.pages.fhnw.ch/module/sysd/assignments/system-design/index.html)

---

## Assessment 06

- concesus algo
  - ein algo für strong constistency
  - wird leader gewählt
- part02:
  - verschiedene db's an CAP theorem angeschaut
  - relationale db: CA, diese db's sind nicht partitions tolerant
    - sharding verwenden, hängt aber von schema ab
  - redis, mongodb etc. sind CP
- part03:
  - storage von der plattform nehmen
  - wir nehmen storage von azure
  - drei typen: disk, files, blob
  - disk: für filesysteme
- wir sollten persistenz implementieren:  
  - was gut bei cw: blob, append only

---

## Recap: Availability…

## Sequentiel Availabilty

- ![alt text](image.png)
- je länger die chain wird, umso kleiner wird die verfügbarkeit

## Parallel Availabilty

- ![alt text](image-1.png)
- verfügbarkeit hochschrauben durch parallel
- horizontal skalieren, für mehr verfügbarkeit

## Chaining of Availability

- ![alt text](image-2.png)

## What is the overall availability?

- ![alt text](image-3.png)
- A hochdrehen, versuchen wir
- berechnungen oben, wenn abhängigkeiten gleichzeitig da sind
- unsere app hat harte abhängigkeiten
- chatbot ist links
- cw ist mitte
- cw ist spf
- wir kommen auf 98% verfügbarkeit

## …and what can we do to keep the singleton functionality and increase (chatlog) availability?

- cw bleibt singelton
- was einbauen, bei bots für höhere A?
  - wir machen keine wartende request
  - wir machen etwas zum hinterlegen, z.b eine queue
  - kommunikation entkoppeln
  - die annahme oben basiert auf synchrone kommunikation

## What is important to be available in the chatbots- architecture?

- kein verlust von nachrichten
  - inbound / outbound
  - historie
- regelmässige updates
- unabhängigkeit der bots
- solche nicht funktionale anforderung...

## Synchronous Messaging Patterns

- ![alt text](image-4.png)
- wo typische synchrone kommunikation: überall wo geld im spiel ist
- banken apps oft starr weil alles synchron

## Asynchronous Messaging Patterns

- ![alt text](image-5.png)
- queue sind fifo
- publisher schickt was, und es dauert etwas bis geantwortet wird
- anderer nachteil, eine neue komponente

## Increasing Availability regarding Message Delivery / Handling

- ![alt text](image-6.png)

## Single Receiver Pattern

- ![alt text](image-7.png)
- ist point to point
- ist einfach
- sehr zuverlässig
- problemlos in eine richtung, wenn die andere offline ist
- nachteil: 4 message broker

## Multi Receiver Pattern

- ![alt text](image-8.png)
- bekannt als pub/sub-pattern
- anzahl messagebroker (MB) reduzieren
- eventbus pusht zu den sachen rechts
- problem: keine garantie das es ankommt
- skalierung über eventbus, egal ob ankommt odr nicht
- dieses pattern ist nicht geeignet für unsere app!

## Request-Reply Pattern

- ![alt text](image-9.png)
- immernoch p-2-p kommunikation
- garantiertes handling, also events kommen an
- das fühlt sich natürlich an
- zwei brokers zwischen zwei bots

## Knowing these patterns: Does it always increase availability? What is needed for the different architectures?

- wir haben kosten für MB für cw
- wir haben kosten für implementierung, für die queues, für die id handling
- das schlägt bis zum source code der bots durch

## Technical: Increasing Availability of Messaging

- ![alt text](image-10.png)
- mit der queue haben wir einen spof (single point of failure)
- wenn man mehrere revciver hat bietet sich sowas an
- z.b. bei der meldung von sbb, die müssen überall die meldung zeigen, auf dem handy, an den gleisen etc.
- mit diesme ansatz bracuhen wir ein queuesystem das ausfallsicher ist
- wenn messaging-system zusammenkracht, ist die ganze resilienz verloren

## NFA: Availability VS Performance

- ![alt text](image-11.png)
- verfügbarkeit und performance ist das spannungsfeld in das wir uns bewegen
- es gibt kein richtig odr falsch
- was ist mir aber wichtig
- schnell und irgend eine antwort -> performance

## FA: Delivery Guarantees

- ![alt text](image-12.png)

## Technology

- ![alt text](image-13.png)
- lösung des dozenten mit nuts
- wir können nutzen was wir wollen

## Overview about Technologies

- ![alt text](image-14.png)
- ![alt text](image-15.png)

## Apache Kafka

- ![alt text](image-16.png)
- kann komplex werden
- man kann replizieren und partitionieren
- kafka war da um msg-archi zu unterstützen

## What is the overall availability now?

- ![alt text](image-17.png)

## Wrap-up

- ![alt text](image-18.png)
- msg nicht für jeden use case
- bei vielen receivier ist es msg gut
- nicht dogmatisch pattern auswendig lernen
- msp wird ein case sein und wir müssen konzepte anwenden
- direkt am whiteboard anwenden dann

---

##  Assignement 07

- überlegen, wie können wir messaging einbauen
- sourcecode anpassung nötig (wahrscheinlich)
