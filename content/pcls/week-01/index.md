+++
title = "Week 01"
date = 2025-09-16
[taxonomies]
authors = ["fatlum"]
tags = ["pcls"]
+++

***Drehbuch: https://sgi.pages.fhnw.ch/moduluebersicht/pcls/drehbuch.html***
***Gitrepo: https://gitlab.fhnw.ch/spd/module/pcls/***
***Assessments / Assignments: https://spd.pages.fhnw.ch/module/pcls/tutorials/assignments/public-cloud-services/hs25/index.html***
***Report: https://gitlab.fhnw.ch/spd/module/pcls/tutorials/assignments/-/blob/main/modules/assessments/pages/…***
***Switch Engines: https://engines.switch.ch/***
***AWS: https://fhnw.awsapps.com/start/#/?tab=accounts***
***Azure: https://portal.azure.com***
---

## Relevante Links
- Assignments: https://spd.pages.fhnw.ch/module/pcls/tutorials/assignments/public-cloud-services/hs25/index.html
- O’Reilly-Literatur: https://learning.oreilly.com/playlists/a27d30d7-f139-4476-9c3a-e0abeb0f89da/
- GitLab Repo: https://gitlab.fhnw.ch/spd/module/pcls

---

## Prüfung / Note
- 2 × 25% → Projekt (Migrationen)
- 1 schriftliche Prüfung → 50%
    - Termin: Montag, 16.12.2026, 12:15h (Moodle mit Campla, Closed Book)
    - Dauer: 60 min
    - Inhalte: Konzepte, Multiple Choice, auch Vorlesungsnotizen und praktische Teile

---

## Projects
- Laufende Applikation von einem Cloud-Anbieter zum anderen migrieren
    - Migration 1: **IaaS (SwitchEngines) → PaaS (ECS/AWS)**
    - Migration 2: **PaaS (ECS/AWS) → FaaS (Azure)**
- Artifacts pro Migration:
    - IaC (Infrastructure as Code)
    - Kurzes Screencast (max. 5 Min)
    - Plattform selber lauffähig
    - Kurzer Report (3 Punkte)
- Deadlines für Artefakte:
    - KW42 und KW48, Sonntag 23:59h
    - Kurze Fragerunde zu den Artefakten in der darauffolgenden Vorlesung
- Gruppenarbeit: genau 3 Personen
- Accounts werden bereitgestellt (Switch, AWS, Azure), inkl. DNS-Integration

---

# Frontalunterricht

## Cloud Grundlagen (NIST Definition)
Eigenschaften einer „echten“ Cloud:
- Broad Network Access → über Ethernet erreichbar
- On-Demand Self-Service → Ressourcen selbst bestellen/entfernen
- Resource Pooling → geteilte Ressourcen
- Rapid Elasticity → schnelle Skalierung
- Measured Service → nutzungsbasiert abgerechnet (Pay-as-you-go):contentReference[oaicite:0]{index=0}

---

## Cloud Deployment Models
- **Private Cloud**
    - Exklusiv für eine Organisation, oft innerhalb Firewall
    - Kann durch Dritte gemanaged werden
    - Skaliert weniger gut als Public Cloud, oft kein „echtes“ Cloud-Modell
- **Public Cloud**
    - Allgemeine Nutzung, multi-tenant
    - Keine volle Datenkontrolle → Confidential Computing als Thema
- **Community Cloud**
    - Für Organisationen mit geteilten Anforderungen (z.B. Staat, Universität)
- **Hybrid Cloud**
    - Kombination aus Public & Private
    - In Realität selten, meist Multi-Cloud + On-Prem kombiniert
- **Holy Grail (Hybrid/Multi-Cloud)**
    - Kombination mehrerer Clouds (AWS, Azure, Google, Private)
    - Seamless Integration → legacy + cloud-native Apps zusammen nutzbar:contentReference[oaicite:1]{index=1}

---

## Services (as-a-Service Modelle)
Abstraktionsstufen: **IaaS > PaaS > SaaS**
- Je weiter links → mehr Verantwortung beim Kunden
- Je weiter rechts → mehr Standardisierung und geringere Flexibilität

### IaaS – Infrastructure as a Service
- Beispiele: SwitchEngines, AWS EC2, Azure VMs
- Use Cases: Legacy-Apps, HPC, Custom-Installationen
- **Pro**:
    - Keine Hardwarekosten, Housing/Power inkludiert
    - Blueprints für OS-Installationen
    - Disaster Recovery / Business Continuity auf OS-Level
    - Vertikale Skalierung möglich
    - Hohe Sicherheit (Monitoring, Audits)
    - Economy of Scale für Provider
- **Con**:
    - Teuerste Variante
    - Kapazitätsmanagement beim Kunden
    - Anpassung oft mit Neustart nötig
    - Kein einfaches horizontales Scaling (Storage-Abhängigkeit)
    - Betriebssystem & Patching Verantwortung Kunde:contentReference[oaicite:2]{index=2}

### PaaS – Platform as a Service
- Beispiele: AWS ECS, Azure App Services
- Use Cases: Deployment-Frameworks (Build, Test, Deploy, Update), Analytics, Auth, Workflow Engines
- **Pro**:
    - Kürzere Dev-Zyklen (Code → Production)
    - Integrierte Toolchains
    - Automatisches Scaling (v.a. horizontal)
    - OS-Lifecycle vom Provider gemanaged
    - Gute Eignung für Microservice-Architekturen
- **Con**:
    - Vendor Lock-in
    - Native Services günstiger als Cloud-agnostische (z.B. Kubernetes)
    - Steile Lernkurve, produktspezifisch
    - Sehr „opinionated“ (Anbieter diktiert Ökosystem):contentReference[oaicite:3]{index=3}

### SaaS – Software as a Service
- Beispiele: Office365, Google G-Suite, Atlassian, GitHub, ERP/CRM-Systeme
- **Pro**:
    - Direkte Nutzung, keine IT-Infrastruktur nötig
    - Fokus auf Business Value
    - Hohe Verfügbarkeit, Disaster Recovery inkl.
    - Skaliert mit Userzahl
- **Con**:
    - Vendor Lock-in, kaum Daten-Export
    - Kaum Anpassung an Workflows möglich
    - Kann teuer werden (fehlendes User-Lifecycle Mgmt)
    - Bei Outage → kompletter Service nicht verfügbar (z.B. Atlassian-Ausfall):contentReference[oaicite:4]{index=4}

---

## Vorteile von Public Cloud Infrastructures
- Schneller am Markt (Time-to-Market)
- Höhere Agilität (Shift Left: Deployment früh bedenken)
- Höhere Verfügbarkeit
- Einfachere Kapazitätsplanung
- Bessere Sicherheit & Compliance (Best Practices)
- Fokus auf Business statt Infrastruktur
- Pay-as-you-go Modelle, Reduktion eigener IT-Kosten:contentReference[oaicite:5]{index=5}

---

## OPEX vs CAPEX
- **CAPEX (Capital Expenditure)**
    - Investitionskosten (Hardware, Housing etc.)
    - Aktivierung im Budget, Kosten über Zeit abgeschrieben
- **OPEX (Operational Expenditure)**
    - Wiederkehrende Betriebskosten
    - Wirken sich direkt auf Gewinn/Verlust aus
- Trend: Unternehmen wollen OPEX (flexiblere Steuerung, variable Kosten):contentReference[oaicite:6]{index=6}

---

## Region & Availability Zones
- **Region**: geografischer Standort, besteht aus mehreren unabhängigen Rechenzentren
- **Availability Zone (AZ)**: ein einzelnes Rechenzentrum innerhalb einer Region
- Beispiel: AWS 34 Regionen, 108 Datacenter, 600+ Edge-Sites:contentReference[oaicite:7]{index=7}

---

## Technische Basis (für Projekte)
- **Programmiersprachen (Chatbot)**: Java (GraalVM/Quarkus), Python (Flask), Go (Gin)
- **IaC-Stack**: Git, Azure-CLI, AWS-CLI, Terraform (Tofu), Ansible
- **Plattformen**: GitLab, SwitchEngines, AWS, Azure, AKS:contentReference[oaicite:8]{index=8}

