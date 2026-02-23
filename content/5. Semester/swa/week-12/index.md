+++
title = "Week 12"
date = 2025-12-02
[taxonomies]
authors = ["fatlum"]
tags = ["swa"]
+++

# Software Architecture – Week 10

## Layer Pattern

- strukturiert software in schichten
- jede schicht hat eine spezifische verantwortung
- schichten kommunizieren nur mit benachbarten schichten
- reduziert kopplung zwischen komponenten

### Presentation Layer

- oberste schicht
- benutzerinteraktion
- UI-komponenten, controllers, views
- empfängt eingaben, zeigt ausgaben
- ruft application layer auf

### Application Layer

- orchestriert use cases
- koordiniert domain layer und infrastructure layer
- enthält anwendungslogik, nicht domain-logik
- use case services, application services
- keine geschäftslogik, nur koordination

### Domain Layer

- kern der anwendung
- enthält geschäftslogik
- entities, value objects, domain services
- unabhängig von technischen details
- repository interfaces definiert hier

### Infrastructure Layer

- technische implementierungen
- datenbankzugriff, externe APIs
- repository implementierungen
- messaging, logging, persistence
- unterstützt domain und application layer

## MVC

-
