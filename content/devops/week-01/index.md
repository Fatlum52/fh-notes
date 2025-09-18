+++
title = "Week 01"
date = 2025-09-15
[taxonomies]
authors = ["fatlum"]
tags = ["devops"]
+++

# Intro

## Learning target
- Architektur berücksichtigen (Architekturentscheidungen, Framework-/Language-Choices)
- Build und Deployment
- Non-functional requirements, Capacity Management
- Availability definieren
- Basic Logging / Monitoring
- Applikation entwickeln und selber betreiben
- Verständnis für Operating Challenges beim Entwickeln

## Gruppenarbeit ganzes Semester
- Chatbot implementieren (LLM-basiert)
- Bauen, releasen und runnen auf Kubernetes-Cluster (Azure AKS)
- Fähigkeit, was gebaut wurde, zu deployen und für alle verfügbar machen
- Day-2-Operations: Es soll laufen, auch am nächsten Tag
  - **Constraints**
    - 3 Microservices
    - Chattende Chatbots
    - Kommunikation über URLs
    - Pro Person: andere Programmiersprache (z.B. Java/Quarkus, Python/Flask, Go/Gin)
- Message Broker wird vom Dozenten bereitgestellt → forken & anpassen

## Struktur Vorlesung
- Wöchentliche Hausarbeit
- Erste 45 min der Vorlesung: Besprechung alte Aufgabe
- Frontalunterricht Beginn: 09:00
- Slides & Materialien: [Intro-01 Folien](https://spd.pages.fhnw.ch/module/devops/templates/reports/devops-foundations/hs25/index.html)

## Wieso DevOps?
- Software nicht nur entwickeln, sondern auch betreiben
- Sauberes Arbeiten: konventionelle Commits (Prefix), z.B. `fix: GL-xxx lorem ipsum`
- Vorteil: Filtern von Commits möglich
- Grundidee: Coden → Builden → Testen → Deployen → Releasen → Monitoren
- Problem früher:
  - alles manuell, Releases bis zu 6 Monate
  - viele manuelle Interaktionen (Dateien kopieren, Feedback spät)
  - hohe Fehlerquelle, wenn Menschen manuell Prozesse durchführen

## Notengebung
- 25% Project Part 1
- 25% Project Part 2
- 50% Schriftliche Prüfung
- Projekt-Noten können bei ungleicher Arbeitsteilung individuell abweichen (Git-History wird geprüft)
- Deadlines: immer Sonntag 23:59h
- Schriftliche Prüfung: 15.12.2026, 18:15h (Campla/Moodle, Closed Book)

---

# Frontaler Unterricht

## Motivation 1: Break the Silos
- Devs wollen Änderungen, Features, schönes UI
- Ops wollen Stabilität, keine Änderungen → Prozesse sind starr und straightforward
- Früher: getrennte Silos → hohe Reibung
- DevOps bringt beide Seiten zusammen → Ziel: stabil UND veränderbar
- Wichtig: kultureller Impact, kaum messbar
- Ziel: so deployen, dass es läuft, und gleichzeitig Änderungen ermöglichen

## Motivation 2: Komplexität handeln
- Systeme heute sind sehr komplex → wir nutzen aber noch alte Konzepte (1980er)
- Versionskontrollen helfen, erste Komplexität zu managen
- Mehr Module in Dev (>20), weniger in Ops (<10) → Spannungsfeld
- DevOps: Brücke zwischen Dev und Ops

## Motivation 3: Technologie über Prozesse
- Basiert auf den Werten des **Agile Manifests**:
  - Individuals & Interactions > Processes & Tools
  - Working Software > Documentation
  - Customer Collaboration > Contract Negotiation
  - Responding to Change > Following a Plan
- Microservices = verteilte Systeme → Fehler selten isoliert
- Ein Fehler löst oft weitere aus
- MTTR (Mean Time To Repair) entscheidend, um Eskalationen zu verhindern

## Motivation 4: Flow beschleunigen
- Release-Zyklen:
  - 70er: 1–3 Jahre
  - 90er: 3–12 Monate
  - 00er: 2–12 Wochen
- Je kontinuierlicher Releases, desto kleiner das Risiko von Fehlern (kleine Steps)
- In diesem Kurs: viele kleine Steps → kontinuierliche Lieferung
- Wichtige Metriken:
  - Lead Time, Cycle Time, Lead Time for Changes
    - Kunde will Änderung → Team startet → Commit → Deployment
  - Deployment Frequency
  - Change Failure Rate (% der fehlgeschlagenen Deployments, die Hotfix/Rollback brauchen)

## Motivation 5: Reliability
- Zuverlässigkeit = wichtigstes Feature
- Kunden vertrauen nur stabilen Systemen → sonst nutzen sie es nicht
- Monitoring & Alerting: früh genug Fehler erkennen
- DORA-Metrics (Google SRE):
  - Lead Time
  - Deployment Frequency
  - Change Fail Rate
  - Time to Restore
  - Availability

---

# Wieso kommt DevOps?

## Driver 1: Cloud
- Cloud = Sourcecode
- Cloud = Automation
- Cloud = Shared Responsibility
- Cloud = Transparent
- Cloud = Scalable

## Driver 2: Isolation
- Deployments isolieren, überall lauffähig
- Architektur: Microservices → jeder Service macht eigenes Ding
- Früher: 20 Teams → 1 Jar File, heute: Container pro Service

## Driver 3: Automate everything / Remove Toil
- Größe von Rechenzentren steigt exponentiell
- Mehr Arbeit, gleich viele Leute
- Ziel: sich "weg automatisieren" → Automatismen entwickeln
- Automatisierung senkt MTTR und erhöht Skalierbarkeit

## Driver 4: Take Responsibility
- Was man deployt, soll zuverlässig sein
- DevOps = Verantwortung für den Betrieb übernehmen

## Driver 5: Kultur
- Wichtigste DevOps-Idee: **Wir bauen etwas zusammen**

---

# Wöchentliche Aufgaben
- Aufgaben: [Assignment 01](https://spd.pages.fhnw.ch/module/devops/templates/reports/devops-foundations/hs25/assignments/assignment01.html)
- Anforderungen:
  - Soll auf Linux-Cluster laufen
  - App via CI/CD baubar
  - Kommunikation über HTTP-Protokoll
  - Logging und Metriken integriert
  - Logs → stdout mit Timestamps (Logging-Framework)
  - Jedes Teammitglied: eigener Chatbot in anderer Programmiersprache

---

# Recap Questions (prüfungsrelevant)
1. Name and describe the 5 DORA metrics
2. Why is Cloud important for DevOps and why is DevOps important for Cloud?
3. Name and explain different targets classical Developer- and Operations-Teams have. Why do they have them?
4. Explain why containerization is important for DevOps.
5. Automation is the key for successful DevOps-Workflows. Why is scalability, ongoing with automation so important when it comes especially to deploying microservice architectures? Why is it important with respect to the lead time?
