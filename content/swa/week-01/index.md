+++
title = "Week 01"
date = 2025-09-16
[taxonomies]
authors = ["fatlum"]
tags = ["swa"]
+++

# Software Architecture – Basic Terms and Concepts

---

## System
- **Teleologische Ansicht (Black-Box)**:
  - Fokus auf Verhalten, Ziele und Zweck eines Systems.
  - Man betrachtet das System von außen → was liefert es?
- **Ontologische Ansicht (White-Box)**:
  - Fokus auf Aufbau und innere Struktur eines Systems.
  - Wir nutzen diese Ansicht, wenn wir verstehen wollen, wie das System intern zusammengesetzt ist.

### Views
- **Static View**:
  - Zeigt Basisbeziehungen zwischen Building Blocks.
  - Überblick über Bausteine zur Design-Time.
- **Dynamic View**:
  - Zeigt, wie die Komponenten miteinander arbeiten und interagieren (zur Run-Time).

---

## Building Blocks (Bausteine)
- Können unterschiedliche Typen haben: Applikation, Daten, Technologie.
- **Technische Systeme**: bestehen ausschließlich aus technischen Bausteinen.
- **Sozio-Technische Systeme**: Kombination aus Menschen, Prozessen und technischen Systemen.
- **Socio Building Blocks**:
  - Zeigen zwischenmenschliche Aspekte.
  - Beziehungen zwischen Menschen, Verantwortungen, Rollen und Positionen.

---

## Architecture Disciplines (Architektur-Disziplinen)
- Drei zentrale Disziplinen, unterscheiden sich v.a. in Granularität und Betrachtungshorizont.
- Jedes Unternehmen arbeitet mit allen drei Disziplinen.

### Enterprise Architecture
- Fokus: gesamtes Unternehmen (System of Systems).
- Aufgaben:
  - Sicherstellen, dass IT-Landschaft strategische Prioritäten unterstützt (Global Optimum).
  - Alignment und Integration von Domain- und Solution-Architektur.
  - Identifikation von Redundanzen, Lücken, Konsolidierungsmöglichkeiten.
  - Strategische Roadmaps, Policies und Methoden bereitstellen.

### Domain Architecture
- Fokus: eine Domäne (z.B. Geschäftsbereich wie Generics, Vaccines, Pharma bei Novartis).
- Aufgaben:
  - Überblick und Transparenz schaffen.
  - Architektur-Pläne (As-Is / To-Be), Standards und Roadmaps pflegen.
  - Unterstützt Entscheidungen, welche Systeme verändert werden müssen.

### Solution Architecture
- Fokus: eine konkrete Lösung innerhalb einer Domäne (z.B. eine Anwendung oder ein Anwendungspaket).
- Aufgaben:
  - „Do it right“ – konkrete Umsetzung nach Vorgaben.
  - Lösung entwickelt/transformiert, um ein Problem zu adressieren.
  - Effiziente und effektive Lösungsgestaltung (Local Optimum).
  - Qualitätseigenschaften wie Security, Performance, Modifiability sicherstellen.

**Analogie** (Stadt Basel):
- Enterprise Architect = Stadtplaner (Gesamtstadt).
- Domain Architect = Quartierplaner (Stadtteil).
- Solution Architect = Architekt für einzelnes Gebäude.

---

## System Architecture
- Jedes System (Auto, Kirche, IT-System) hat eine inhärente Architektur.
- Architektur definiert:
  - Struktur und Anordnung der Bausteine (Whole–Part).
  - Statische Beziehungen (Design-Time).
  - Dynamische Beziehungen (zur Laufzeit).
  - Prinzipien und Guidelines, die das Design und die Evolution steuern.

### Evolution
- Systeme und ihre Architekturen verändern sich über die Zeit.
- **Kosten der Änderung** → entscheidend, ob es ein Architekturthema ist.
- Große Systeme verlieren mit wachsender Funktionalität oft an Agilität → deshalb braucht es einen **Evolution Corridor**, um gezielt Änderungen zu steuern.

### Architecture View Models (Krüger-Modell, „4+1 Views“)
Beispiel Stadt Aarau:
- **Reality**: echtes Foto → Realität.
- **Map View**: Schwarz-Weiß-Karte mit Gebäuden, Straßen, etc.
- **Public Transport View**: zeigt ÖV-Linien und Haltestellen.
- **Population Density View**: zeigt Einwohnerdichte.
- **Buffer Zones**: zeigt Erreichbarkeit der Haltestellen.
- Erkenntnis: **Kombination mehrerer Sichten** ergibt ein vollständiges Architekturmodell.

---

## Software Architecture
- Unterschiedliche Definitionen, aber Kernelemente:
  - Softwarearchitektur ist **die Gesamtheit signifikanter Designentscheidungen** (Booch).
  - Signifikant = Änderungen sind teuer.
  - Architektur ist Blaupause für System & Projekt.
  - Träger von Systemqualitäten (Performance, Security, Modifiability).
  - Frühzeitige Risikoidentifikation und -behandlung.

### SEI-Definition (Carnegie Mellon)
> „Software architecture is a depiction of the system that aids in understanding how the system will behave. It serves as a blueprint for the system and the project, defining responsibilities. Architecture is the primary carrier of qualities such as performance, modifiability, security, and enables early analysis to ensure an acceptable design.“

### Martin Fowler („Who needs an architect?“)
- Architektur = geteiltes Verständnis des Designs im Team.
- Beinhaltet Aufteilung in Komponenten und deren Schnittstellen.
- Architektur ist kein einmaliges Dokument, sondern ein lebendiges, geteiltes Modell.

### Ralph Johnson
- Software ist nicht durch Physik limitiert (wie Gebäude), sondern durch Menschen (Imagination, Organisation, Design).

### Conway’s Law
- „Organisationen designen Systeme, die die Kommunikationsstrukturen der Organisation widerspiegeln.“

---

## Zusammenfassung
- **System**: Teleologisch (Black-Box) vs. Ontologisch (White-Box).
- **Building Blocks**: technisch, sozial oder kombiniert.
- **Architektur-Disziplinen**: Enterprise (strategisch), Domain (mittlere Granularität), Solution (konkret/operativ).
- **Systemarchitektur**: beschreibt Struktur, Dynamik und Evolution.
- **Softwarearchitektur**: fokussiert auf signifikante Designentscheidungen, Systemqualitäten und gemeinsame Verständnisse.  

