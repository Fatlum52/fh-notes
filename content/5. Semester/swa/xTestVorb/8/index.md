+++
title = "8 Architecture Patterns - From Mud to Structure"
date = 2025-12-02
[taxonomies]
authors = ["fatlum"]
tags = ["swa"]
+++

# Architecture Patterns - From Mud to Structure

## Layer Pattern

- **Problem**: komplexe systeme werden verworren wenn alle teile frei interagieren
- **Key building blocks**: layers (z.B. Presentation, Business Logic, Data Access), interfaces zwischen layers
- **Solution**: jede layer bietet services für layer darüber und nutzt services von layer darunter
- erzwingt klare dependency-richtung, versteckt interne details, ermöglicht unabhängige evolution

## Model-View-Controller (MVC)

- **Problem**: UI-code wird oft tight coupled mit business logic
- **Key building blocks**:
  - **Model**: domain data und business logic
  - **View**: visuelle repräsentation der model-daten
  - **Controller**: mediator handling user input und coordinating updates
- **Solution**: controller interpretiert user actions und updated model. model benachrichtigt views (oft via observer pattern)
- ermöglicht unabhängige modification von UI und logic

## Pipes and Filters

- **Problem**: applications die komplexe daten-transformationen durchführen mischen transformation logic und control flow
- **Key building blocks**:
  - **Filters**: unabhängige processing units die input zu output transformieren
  - **Pipes**: connectors die daten-streams zwischen filtern weitergeben
- **Solution**: jeder filter verarbeitet daten von upstream pipe und gibt output downstream weiter
- filter können neu angeordnet oder ersetzt werden ohne control structure zu ändern

## Shared Repository

- **Problem**: subsystems die große mengen gemeinsamer daten teilen müssen bauen eigene ad-hoc data exchange logic
- **Key building blocks**:
  - **Repository**: zentraler daten-store
  - **Subsystems/Components**: zugreifen über definiertes schema/interface
- **Solution**: alle komponenten lesen/schreiben zu common repository über standardisierte access interfaces
- konsistenz wird zentral sichergestellt

## Microkernel

- **Problem**: systeme mit stabilem core aber vielen variablen extensions
- **Key building blocks**:
  - **Microkernel**: minimal runtime, communication, management
  - **Internal servers**: core subsystems direkt vom kernel verwaltet
  - **External plug-ins/adapters**: application-spezifische extensions
- **Solution**: microkernel bietet basic mechanisms (service registration, communication)
- plug-ins erweitern funktionalität über well-defined extension points

## Reflection

- **Problem**: hochdynamische systeme müssen behavior/structure zur laufzeit anpassen ohne recompilation
- **Key building blocks**:
  - **Meta-level**: maintains representations von system structure und behavior (metadata)
  - **Base-level**: performs normal application logic using meta-level definitions
- **Solution**: base-level konsultiert oder modifiziert meta-level descriptions zur laufzeit
- ermöglicht self-inspection, self-adaptation, runtime reconfiguration

