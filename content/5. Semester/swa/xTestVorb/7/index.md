+++
title = "7 Component Orientation und Basic Architecture Concepts"
date = 2025-12-02
[taxonomies]
authors = ["fatlum"]
tags = ["swa"]
+++

# Component Orientation und Basic Architecture Concepts

## Component Orientation

### Warum Komponenten

- klassen allein reichen nicht für komplexe systeme
- komponenten sind **gröber granular** als klassen
- komponenten **composen viele klassen** zu größerem ganzen
- reduzierung von beziehungen zwischen teilen
- hohe innenbezüglichkeit (cohesion)
- lose aussenbezüglichkeit (coupling)

### Core Concepts

- komponenten machen capabilities über **dedicated interfaces** verfügbar
- providing component **exports** interfaces
- consuming component **imports** interfaces
- komponenten binden an **interfaces, nicht implementierungen**
- **component composition**: komponenten können selbst aus anderen komponenten bestehen

### Vorgehen bei Component Orientation

1. **identifiziere komponenten**: ähnliche klassen mit gemeinsamen responsibilities
2. **definiere responsibilities**: was macht jede komponente
3. **definiere interfaces**:
   - welche interfaces exportiert komponente (was bietet sie an)
   - welche interfaces importiert komponente (was braucht sie)
4. **analysiere interaktionen**: wer will was von wem
5. **validiere design**:
   - hat jede komponente klare business/technical responsibility?
   - ist daten-zugriff über well-formed interfaces möglich?
   - ist system einfach zu testen und erweitern?
   - gibt es unnötige dependencies?

### Beispiel: CandidateManagement Component

- **Responsibilities**:
  - registration neuer candidates und lifecycle management
  - management von profile information
  - status-änderungen
  - data storage
- **Exported Interfaces**:
  - `ICandidateService`: für änderungen
  - `ICandidateQueryService`: für read-only access
- **Imported Interfaces**:
  - `INotificationService`: von NotificationDelivery component

## Basic Architecture Concepts

### Classes & Objects

- **Objects**: haben identität, state, operations
- **Classes**: blueprints für ähnliche objekte
- kleinste units des object-oriented paradigm
- für viele überlegungen zu fine-grained

### Modules & Components

- development view braucht approach zum bundeln von klassen
- komponenten als architecture components
- abstrahieren von class-level design
- ermöglichen coarsere strukturierung

### Interface

- definiert vertrag zwischen komponenten
- trennung von interface und implementierung
- ermöglicht loose coupling

### Composition

- komponenten können aus anderen komponenten bestehen
- hierarchische strukturierung möglich

