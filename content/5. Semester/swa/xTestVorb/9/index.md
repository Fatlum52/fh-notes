+++
title = "9 Microservices"
date = 2025-12-02
[taxonomies]
authors = ["fatlum"]
tags = ["swa"]
+++

# Microservices

## Motivation

- **NICHT** ein trend, sondern antwort auf reale organisationale und technische scaling-probleme
- traditionelle monolithen: zentrale einfachheit, aber tight coupling, limited modifiability, deployment inflexibility, slow scaling
- microservices ermöglichen:
  - independent deployment
  - team ownership
  - autonomous pipelines
  - fine-grained scalability
  - improved modularization & decoupling
  - reuse across applications

## Definition

- microservice ist eigener deployment unit
- largely self-contained
- kann in verschiedenen application contexts wiederverwendet werden
- prinzipien bleiben gleich (modularity, abstraction, SoC, explicit interfaces), aber werden weiter getrieben

## Key Patterns

### API Gateway

- einziger eintrittspunkt
- routing, authentication, load balancing

### Service Registry

- services registrieren und finden sich gegenseitig

### Messaging

- asynchrone kommunikation zwischen services

### Hexagonal Architecture

- ports and adapters pattern
- trennung von business logic und infrastructure

## Persistence Patterns

### Database per Service

- jede service hat eigene datenbank
- keine shared database

### Event Sourcing

- speichert events statt zustand
- rebuild state by replaying events

### Change Data Capture (CDC)

- capture changes in database
- propagate to other services

### Saga Pattern

- verwaltet verteilte transaktionen
- koordiniert mehrere services

## Security

- **Firewall Proxy**: schützt services
- **RBAC**: role-based access control
- **XACML**: extensible access control markup language

## Organizational Impact

- team-autonomie
- unabhängige entwicklung
- schnelleres deployment
- bessere skalierung

