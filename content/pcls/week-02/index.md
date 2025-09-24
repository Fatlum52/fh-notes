+++
title = "Week 02"
date = 2025-09-23
[taxonomies]
authors = ["fatlum"]
tags = ["pcls"]
+++

***Drehbuch: [Modulübersicht PCLS – Drehbuch](https://sgi.pages.fhnw.ch/moduluebersicht/pcls/drehbuch.html)***  
***Gitrepo: [spd/module/pcls (GitLab)](https://gitlab.fhnw.ch/spd/module/pcls/)***  
***Assessments / Assignments: [Public Cloud Services – HS25](https://spd.pages.fhnw.ch/module/pcls/tutorials/assignments/public-cloud-services/hs25/index.html)***  
***Report: [Assessments Pages (Ordneransicht)](https://gitlab.fhnw.ch/spd/module/pcls/tutorials/assignments/-/tree/main/modules/assessments/pages/)***  
***Switch Engines: [engines.switch.ch](https://engines.switch.ch/)***  
***AWS: [FHNW AWS-SSO Portal](https://fhnw.awsapps.com/start/#/?tab=accounts)***  
***Azure: [Azure Portal](https://portal.azure.com)***  
***O’Reilly: [O’Reilly-Literatur (Playlist)](https://learning.oreilly.com/playlists/a27d30d7-f139-4476-9c3a-e0abeb0f89da/)***

---

# Frontalunterricht

## Legal Aspects
### Legal aspects to secure the service/data
- zahlt man → man ist Kunde
- zahlt man nichts → man ist Produkt
- mit Bezahlung: betrifft primär **IT-Sicherheit**

**CIA Triad**:contentReference[oaicite:0]{index=0}:
- **Confidentiality**: wer liest meine Daten / wer greift auf meinen Service zu?
- **Availability**: sind meine Daten und Services verfügbar? (SLA’s)
- **Integrity**: ist mein Service kompromittiert oder verändert?
  - Cloud-Anbieter dürfen Daten **nicht** verändern, ausser aus Sicherheitsgründen (z.B. wenn ein Kundensystem gehackt wird).

---

### Levels von Legal Aspects
- **Regulationen / Verträge zwischen Firmen**
  - **Cyber Resilience Act (CRA)**:contentReference[oaicite:1]{index=1}:
    - alle Produkte mit digitalen Elementen in der EU müssen Cybersecurity nachweisen
    - Anforderungen nachvollziehbar dokumentieren
    - jede Verwundbarkeit muss gemeldet werden
    - Support über gesamte Lebensdauer
  - **Data Protection**:
    - Cloud Provider garantieren Datenschutz
- **Regulationen gegen staatliche Institutionen**
  - **CLOUD Act**:contentReference[oaicite:2]{index=2}:
    - US CSP müssen Daten weltweit aufbewahren und an US-Behörden herausgeben (auf Anfrage)
    - unabhängig vom Speicherort
    - Hyperscaler (AWS, Azure) zeigen Transparenz-Reports
- **Private Cloud**:
  - oft auf Hardware aus USA oder China
  - Hersteller haben über Support/Service potenziell Zugriff
  - keine technische Garantie für „unbefugten Access“

---

### Zusammenfassung
- Legal Aspects sind schwer zu bestimmen → verschiedene Levels (Storage, Service, Location, Public vs. Private Cloud).
- Private Cloud bietet **keine absolute Sicherheit** gegen Zugriff.
- Hyperscaler stellen Transparenzberichte bereit.

---

## IaaS

### Product Class:contentReference[oaicite:3]{index=3}
- **Virtual Computing** auf Basis von **AMI (Amazon Machine Image)** oder **Azure Machine Image**
- **CPU/RAM**: feste Instanztypen mit definierten Setups
- **Disks**: extra Produkt, flexibel erweiterbar
- **Netzwerk**: externes Interface, Subnet-Management
- **Skalierung** möglich
- **Tags, Tags, Tags**: Labels zur Organisation (wichtig in Cloud-Welt)
- Zugriff: **SSH Public/Private Key**
- **Security Note**: IP-Ranges werden nach unerfahrenen Usern gescannt

---

### Templates
- **Grundidee**: Image/Template als Startpunkt für VM (wie Docker-Image)
- **AMI**:
  - basiert auf existierender EC2-Instanz
  - ermöglicht Golden Image (einmal bauen, mehrfach starten)
- **Packer**:
  - Tool von Hashicorp
  - erstellt automatisiert Golden Images
  - wird in Pipelines integriert
- **Cloud-Init**:
  - Settings beim Booten (Netzwerk, User, Vendor, Metadaten)
  - z.B. automatisches Anlegen von Usern + SSH-Keys

---

### Unterschiede zu Switch Engines
- **Templates**:
  - AWS: über AMI / Marketplace
  - Switch Engines: nur CLI-Download
- **Lifecycle**:
  - AWS: `pending → running → stopping/stopped → terminated`
  - Switch: „Stop“ entspricht **shelve**
- **Ähnlichkeiten**:
  - cloud-init funktioniert
  - SSH beim ersten Start
  - self-service: Provisionierung, Imaging, Deletion

---

### Block Storage & Instance Classes
- AWS: EBS-Volumes als Blockstorage, flexibel attach/detach
- Verschiedene CPU/RAM-Kombis möglich
- Switch Engines: weniger Vielfalt

---

### Optimizing Costs:contentReference[oaicite:4]{index=4}
- **Warum teuer?**
  - flexibel, kein Vendor-Lock, erfüllen SLAs
- **Optimierung**:
  - **Free Tier**: Einstieg
  - **On-Demand**: Start/Stop bei Bedarf
  - **Reserved Instances**: bis 40–50% günstiger (für statische Workloads über Jahre)
  - **Spot Instances**: Restkapazitäten versteigert → riskant, da weggenommen werden kann
  - **Saving Plans**: langfristige Vertragsmodelle
  - **Azure Hybrid Benefit**: Vorteil für Windows-Lizenzen → Vendor Lock-in
- **Architekturen**:
  - Workload richtig verteilen
  - Monitoring + Orchestrator für Event-gesteuertes Skalieren
  - Software-basierter Load Balancer

---

### Zusammenfassung
- IaaS = Hauptgrund für Cloud-Nutzung
- Einfaches, bekanntes Produkt
- Bei richtiger Nutzung: günstig, skalierbar, zuverlässig
- **Billing treibt Architekturentscheidungen**
- **IaC** (Infrastructure as Code) für Setup/Maintenance essenziell

---

## Optional Tutorials
- **AWS (EC2)**: [AWS Academy Modul 6](https://awsacademy.instructure.com/courses/137586/modules)
- **Azure**: [Compute & Networking Services](https://learn.microsoft.com/de-de/training/modules/describe-azure-compute-networking-services/)

---

## Vorbereitung
- **IaC** über Provisionierung lernen
- **Packer** und **Cloud-Init** üben
