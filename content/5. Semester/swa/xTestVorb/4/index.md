+++
title = "4 Architecture Conditions, Significance, Approach"
date = 2025-12-02
[taxonomies]
authors = ["fatlum"]
tags = ["swa"]
+++

# Architecture Conditions, Significance, Approach

## Architecture Conditions

### Definition

- conditions als motivatoren für architektur
- architecture conditions sind kräfte, auf die die architektur reagieren muss
- system von kräften, die architektur ausbalancieren muss
- solution adressiert problem durch absorption der conditions

### Anforderungen an Conditions

- **Correct**: nur stakeholder können das beurteilen
- **Feasible**: muss mit verfügbaren mitteln realisierbar sein
- **Unambiguous**: nur eine interpretation möglich
- **Verifiable**: muss verifizierbar sein

### Types of Conditions

- **Requirements**: wünsche einer organisation
  - **Functional Requirements**: existenzielle bedürfnisse, grund für system-existenz
  - **Non-Functional Requirements**: nicht existentiell, aber essentiell (wie system funktioniert)
- **Constraints**: faktische einschränkungen, die nicht umgangen werden können
  - beispiel: zeit, skills, budget
- **Assumptions**: bekannte unsicherheiten (known unknowns)
  - wahrscheinlich (aber nicht notwendig) zukünftige bedingungen
  - entscheidungen basierend auf assumptions müssen eher revidiert werden

### Capturing Conditions

- **Use Cases**: für functional requirements
- **Quality Attribute Scenarios**: für non-functional requirements, constraints, assumptions

## Architecture Significance

### Definition (Grady Booch)

"Architecture is the set of significant design decisions that shape a system, where significant is measured by cost of change"

- eine requirement ist significant, wenn das design schwer zu ändern/abbauen/anpassen ist, sollte die requirement sich ändern

### Heuristik zur Bestimmung

- **Number of impacts**: anzahl der architektur-entscheidungen die nötig sind
- **Stakeholder importance**: wichtigkeit der stakeholder (business > technical)
- **Non-functionality**: non-functional conditions haben oft große auswirkungen
- **Novelty**: grad der ungewöhnlichkeit/neuheit
- **Volatility**: wahrscheinlichkeit dass condition sich ändert
- **Degree of conflict**: konflikte mit anderen conditions, trade-offs nötig
- **Degree of strategic orientation**: beitrag zu strategischen zielen

### Beispiele für Architecture-Significant Requirements

- system muss 24/7 hochverfügbar sein
- system muss GDPR-konform sein
- system muss in SAP integriert werden
- system muss cloud-native sein
- system muss multi-client fähig sein
- system muss real-time requirements erfüllen
- system muss machine learning unterstützen

### Requirements die zunächst nicht significant erscheinen

- modifiability in UI (z.B. "spezialisten sollen UI-felder anpassen können")
- internationalization (z.B. "texte in deutsch und englisch")
- mobile use (z.B. "app soll auf tablets funktionieren")
- role and rights model (z.B. "admin und user rechte")
- export function (z.B. "daten exportierbar als CSV")
- reporting/statistics (z.B. "reporting-modul")

## Architecture Approach

### Definition

- teil einer gesamten architektur
- jeder approach adressiert eine teilmenge der conditions eines problems
- aus sicht des gesamtdesigns: partial solution
- partial solutions werden zur gesamten architektur kombiniert
- auch genannt: solution design segments, microarchitectures

### Eigenschaften

- wird mit gleichen methoden geplant/designed/beschrieben wie gesamte architektur
- implementiert eine oder mehrere conditions
- für functional requirement: design das use case realisiert
- für non-functional requirement: spezifiziert wie quality attribute scenario realisiert wird
- ermöglicht traceability zwischen conditions und decisions

### Beispiel: Authentication Approach

- requirement: benutzer sollen authentifiziert werden
- constraint: benutzer-basis existiert bereits in LDAP
- approach beschreibt:
  - impact (force) auf system
  - desired response (behavior)
  - architecture building blocks (statisch und dynamisch)
  - architecture decisions

