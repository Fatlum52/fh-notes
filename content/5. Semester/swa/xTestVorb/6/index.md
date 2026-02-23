+++
title = "6 Domain-Driven Design und Architecture Principles"
date = 2025-12-02
[taxonomies]
authors = ["fatlum"]
tags = ["swa"]
+++

# Domain-Driven Design und Architecture Principles

## Domain-Driven Design (DDD)

### Domain Model

- **Definition**: gemeinsame sprache für konsistente benennung und verständnis von begriffen, konzepten und beziehungen
- living working tool zur effizienzsteigerung der kommunikation
- iterativ entwickeln, nicht final und komplett
- **NICHT** technisches datenmodell oder solution design
- **NICHT** system-architektur oder implementierung
- ziel: missverständnisse vermeiden, communication fördern, ubiquitous language schaffen
- erster schritt zur transformation von requirements in nachhaltige software-architektur

### DDD Bausteine

#### Entity (Reference Objects)

- objekte die nicht durch properties, sondern durch **identität** definiert sind
- beispiel: person bleibt dieselbe person auch wenn properties sich ändern
- zwei personen sind unterschiedlich auch bei gleichen properties
- oft mit unique identifiers modelliert

#### Value Object

- objekte ohne konzeptuelle identität
- definiert **nur durch properties**
- meist immutable (wiederverwendbar, verteilbar)

#### Aggregate

- kombinationen von entities und value objects zu gemeinsamer transaktionaler einheit
- definiert genau eine entity als einzigen zugriff auf gesamtes aggregate (aggregate root)
- alle anderen entities/value objects dürfen nicht statisch von außen referenziert werden
- garantiert invariants des aggregates

#### Repository

- abstrahiert persistence und suche von business objects
- trennt technische infrastructure von business logic layer
- repositories sind teil des domain models (business logic layer)
- einzige die auf infrastructure layer zugreifen

#### Factory

- outsourcen der erstellung von domain objects zu factory objects
- nützlich wenn erstellung komplex ist oder austauschbar sein soll
- typische patterns: abstract factory, factory method, builder

#### Service Objects (Services)

- funktionalitäten die wichtiges konzept des domain models repräsentieren
- gehören konzeptionell zu mehreren objekten
- meist stateless, wiederverwendbare klassen ohne associations

#### Domain Events

- objekte die komplexe, dynamisch ändernde actions beschreiben
- verursachen actions oder changes in domain objects
- ermöglichen modellierung verteilter systeme

#### Modules (Packages)

- teilen domain model in funktionale (nicht technische) komponenten
- starke interne cohesion, niedrige kopplung zwischen modulen

#### Associations

- beziehungen zwischen objekten des domain models
- nicht nur statische referenzen, auch dynamische (z.B. durch SQL queries)

## Architecture Principles (SOLID)

### Single Responsibility Principle (SRP)

- eine klasse hat nur eine verantwortung
- nur ein grund für änderung
- beispiel: Invoice sollte nicht printInvoice() haben, sondern InvoicePrinter

### Open/Closed Principle (OCP)

- offen für erweiterung, geschlossen für modifikation
- erreicht durch inheritance oder delegation
- beispiel: Strategy Pattern, Decorator Pattern

### Liskov Substitution Principle (LSP)

- subklassen müssen basisklasse ersetzen können
- vertrag der basisklasse muss eingehalten werden
- beispiel: Penguin kann nicht Bird ersetzen wenn Bird fly() hat

### Interface Segregation Principle (ISP)

- clients sollten nicht von methoden abhängen die sie nicht nutzen
- viele spezifische interfaces statt ein großes

### Dependency Inversion Principle (DIP)

- high-level und low-level modules sollten von abstraktionen abhängen
- abhängigkeiten auf interfaces, nicht implementierungen
- dependency injection: dependencies von außen übergeben

