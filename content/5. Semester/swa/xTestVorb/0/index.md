+++
title = "0 Einführung und Grundlagen"
date = 2025-12-02
[taxonomies]
authors = ["fatlum"]
tags = ["swa"]
+++

# Einführung und Grundlagen

## Introduction (0.1)

### Lernansatz

- **Vorbereitung zu Hause**: slide sets durcharbeiten
- **Im Unterricht**: gemeinsame anwendung des gelernten
- **Instruction documents**: enthalten fragen und aufgaben
- **ChatGPT erlaubt**: zur hilfe beim lernen zu hause

### Lernkonzept

1. **Entdecken**: neue aspekte verstehen, in kurzzeitgedächtnis speichern
2. **Erinnern**: von kurz- zu langzeitgedächtnis, learning tasks
3. **Anwenden**: praktische übungen, case studies, gruppenarbeit

### Wichtige Hinweise

- preparation ≠ durch slides scrollen
- tasks und fragen in instruction documents sind essentiell
- fragen stellen, auch in vorbereitungsphase
- ziel: teilnahme im unterricht, nicht perfektes verständnis
- bei fehlern produktiv lernen

## Design Patterns Catalogue (0.2)

### Wichtige Patterns

#### Creational Patterns

- **Abstract Factory**: erstellt familien verwandter objekte

#### Structural Patterns

- **Adapter**: macht inkompatible interfaces kompatibel
  - problem: zwei komponenten müssen zusammenarbeiten trotz inkompatibler interfaces
  - solution: wrapper um adaptee, implementiert target interface
  - uses: JDBC drivers, interface converters
- **Facade**: vereinfachte schnittstelle zu komplexem subsystem
  - problem: komplexe subsystems überwältigen clients
  - solution: single high-level interface
  - uses: API gateways, persistence libraries
- **Proxy**: kontrolliert zugriff transparent
  - problem: zugriff muss kontrolliert oder erweitert werden
  - solution: proxy implementiert subject interface, fügt behavior hinzu
  - uses: virtual proxies, RMI stubs, AOP interceptors

#### Behavioral Patterns

- **Command**: kapselt action als objekt
  - problem: method calls müssen delayed, queued, oder undone werden
  - solution: encapsulate action in command object mit execute()
  - uses: GUI buttons, transactional job queues
- **Strategy**: familie austauschbarer algorithmen
  - problem: mehrere algorithmen für eine aufgabe
  - solution: familie von strategies mit common interface
  - uses: sorting, payment algorithms
- **Observer (Publish-Subscribe)**: benachrichtigt abonnenten bei änderungen
  - problem: viele objekte brauchen automatische updates
  - solution: subjects maintain subscriber lists
  - uses: UI bindings, message brokers
- **Chain of Responsibility**: kette von handlern
  - problem: mehrere handler können request verarbeiten
  - solution: link handlers in chain, jeder verarbeitet oder gibt weiter
  - uses: servlet filters, exception chains
- **State**: zustand als objekt
  - problem: objekt verhalten ändert sich bei zustandsänderung
  - solution: zustand als objekt
- **Template Method**: skeleton algorithmus
  - problem: algorithmus-struktur bekannt, schritte variabel
  - solution: template method definiert skeleton, subklassen implementieren schritte
- **Decorator**: fügt funktionalität dynamisch hinzu
  - problem: funktionalität muss dynamisch hinzugefügt werden
  - solution: decorator umhüllt objekt

#### Architectural Patterns

- **Layers**: schichten-struktur
- **Model-View-Controller**: trennung von daten, präsentation, steuerung
- **Pipes and Filters**: datenverarbeitung durch filter-kette
- **Shared Repository**: zentraler daten-store
- **Microkernel**: stabiler core mit extensions

#### Weitere Patterns

- **DTO (Data Transfer Object)**: aggregiert daten für transfer
  - problem: viele fine-grained calls verursachen latency
  - solution: aggregate related data in serializable object
  - uses: REST/GraphQL payloads, EJBs
- **Event Sourcing**: speichert events statt zustand
  - problem: current-state persistence verliert audit information
  - solution: store every state-changing event, rebuild by replaying
  - uses: banking ledgers, Git, Kafka
- **Context Object**: kapselt kontextuelle information
  - problem: viele komponenten brauchen shared environment data
  - solution: encapsulate context in single object
  - uses: ServletContext, transaction contexts
- **Reflection**: system inspiziert eigene struktur zur laufzeit
  - problem: system muss eigene struktur zur laufzeit inspizieren/modifizieren
  - solution: represent classes/methods as meta-objects
  - uses: Java Reflection API, dependency injection

## Architecture Context (0.3)

### Enterprise & Domain vs. Solution & Software Architecture

- **Enterprise Architecture (EA)**: fokus auf alignment zwischen business strategy, processes, IT capabilities
- **Domain Architecture (DA)**: fokus auf spezifische business/technical domains
- beide operieren auf strategischer und cross-system ebene
- **Solution Architecture (SA)**: fokus auf architecture einer einzelnen solution
  - stellt sicher dass solution alle requirements erfüllt
  - balanciert business needs, technical feasibility, integration constraints
  - operiert auf project/solution delivery ebene
- **Software Architecture (SWA)**: subset von Solution Architecture
  - interne struktur der software
  - definiert wie komponenten strukturiert sind und interagieren

### Solution Architecture Komposition

- **Existing Parts**: funktionale/operational components bereits verfügbar
  - beispiel: integration APIs, message queues, authentication systems
- **Parts to be designed**: neue komponenten speziell für solution entwickelt
  - software architect fokussiert hierauf

### Software Architect Core Responsibilities

1. **Use Case Realizations**: komponenten und collaboration für funktionalität
2. **Quality Attribute Realizations**: non-functional requirements (performance, security, modifiability)
3. **Business Components (Domain Model)**: core domain logic und business components

