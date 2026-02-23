+++
title = "Week 05"
date = 2025-10-14
[taxonomies]
authors = ["fatlum"]
tags = ["swa"]
+++

## Software Architecture – Week 05

### Architecture Methodology

**Definition und Ziel**

- Eine **Methodology** beschreibt einen **systematischen Prozess**, um Architekturziele zu erreichen.  
  Sie legt fest:
  - **Zustände und Übergänge** (State & Transition Space),
  - **Rollen, Eingaben und Ausgaben** jeder Aktivität,
  - und fördert **Wiederholbarkeit** und **Nachvollziehbarkeit**.
- Ziel ist es, **Struktur**, **Konsistenz** und **Governance** in Architekturentscheidungen zu bringen und „Re-Invention“ zu vermeiden.

**Typen von Architektur-Methodologien**

- **Solution Architecture Development** – z. B. *Unified Process*, *TOGAF*, *ArchiMate*  
- **Enterprise/Domain Architecture Development** – z. B. *TOGAF*, *Zachman*  
- **Reference Architecture Development** – z. B. *Pattern*- oder *Roadmap-Methodologien*  
- **Architecture Assessment** – z. B. *ATAM (Architecture Tradeoff Analysis Method)*  

**Kernnutzen**

- Erhöht **Systematik** und **Reproduzierbarkeit** von Architekturarbeit.  
- Fördert **Ausrichtung** zwischen Teams und **Wiederverwendung** von bewährten Strukturen.  
- Beantwortet die Fragen **„Why – What – Who – When – How“** für alle Architekturzustände und Übergänge.

---

### Framework Adaptation

**Warum Anpassung wichtig ist**

- Frameworks wie **TOGAF ADM** sind **generische Werkzeuge**, keine fertigen Lösungen.  
- Fehlannahme: Frameworks seien **Selbstzweck** – tatsächlich müssen sie auf **Unternehmensziele** zugeschnitten werden.  
- Eine sinnvolle Anwendung erfordert **Kontextverständnis** und **Zielklarheit**.

**Vorgehen bei der Anpassung**

1. **Zieldefinition:**  
   Kläre, was der spezifische Nutzen von Architektur in deiner Organisation ist (z. B. Kostenreduktion, Effizienzsteigerung, Compliance).
2. **Stakeholderanalyse:**  
   Wer profitiert? (Business, IT, Portfolio-Management)  
   Wie und wann ist der Nutzen messbar (kurz-, mittel-, langfristig)?
3. **Kosten-Nutzen-Bewertung:**  
   Aufwand zur Framework-Einführung und -Anpassung bestimmen.
4. **Anpassung auf mehreren Ebenen:**  
   Frameworks müssen je nach **Enterprise-, Domain- und Solution-Ebene** unterschiedlich konkretisiert werden.

**Grundprinzip:**  
> „You need to know where you want to go before choosing the path.“  
Erst wenn der **Zweck** von Architektur klar ist, kann ein Framework sinnvoll angepasst werden.

---

### Architecture Process (nach TOGAF ADM)

**Ziel:**  
Ein strukturierter, iterativer Prozess, der die Entwicklung, Planung und Steuerung von Architekturen über alle Ebenen hinweg ermöglicht.

**Phasen des Architekturprozesses**

1. **Transparency:**  
   Erfassen und Pflegen des *As-Is*-Zustands (Business, IT-Landschaft, Daten, Prozesse).  
2. **Analysis:**  
   Identifikation von **Lücken, Redundanzen, Risiken** und **Chancen** (z. B. durch Technologie-Trends).  
3. **Design (EA Design):**  
   Ableiten der **Target Architecture** auf Basis von Business- und IT-Anforderungen.  
4. **Planning:**  
   Erstellung einer **Architecture Roadmap** und Abstimmung im **Portfolio-Management**.  
5. **Governance:**  
   Definition von **Guardrails** (Richtlinien, Standards, regulatorische Vorgaben).  
6. **Requirements Management:**  
   Zentrale Steuerung, um alle Architekturentscheidungen mit den ursprünglichen Anforderungen abzugleichen.

**Iterative Zyklen (TOGAF-ADM-Prinzip):**

- **Context Cycle:** Aufbau der Architektur-Organisation und Definition des Scopes.  
- **Delivery Cycle:** Entwicklung von *Baseline → Target Architecture*.  
- **Transition Planning:** Planung von Umsetzung & Migration.  
- **Governance Cycle:** Steuerung & Überwachung der Änderungen.

**Zusammenspiel der Ebenen**

- **Enterprise Architecture**: strategische Gesamtsicht, übergreifende Strukturen.  
- **Domain Architecture**: Segment- oder Bereichssicht (z. B. Banking, Retail).  
- **Solution Architecture**: konkrete Lösungen und Software-Designs.  

Alle drei Ebenen sind **prozessual und inhaltlich miteinander verknüpft** und spiegeln sich in den View-Modellen wider.

---

### Architecture Mandate

**Definition**

- Ein **Architecture Mandate** ist eine **formale Vereinbarung** über **Erwartungen, Ziele und Verpflichtungen** innerhalb eines Architektur-Engagements.  
- Es dient als **„Definition of Done“** für Architekturarbeit.

**Nutzen**

- Verhindert **Unklarheiten** über Scope, Deliverables und Verantwortung.  
- Fördert eine **gemeinsame Erwartungshaltung** aller Beteiligten.  
- Unterstützt Architekten, während eines Projekts regelmäßig zu prüfen, ob die gesetzten Ziele erreicht sind.

**Zentrale Idee**

- Mandate sind **Reflexionswerkzeuge**: Sie zwingen dazu, Probleme **reif** zu verstehen, bevor man Lösungen plant.  
- Sie begleiten Projekte als **Messlatte** („Yardstick“) für Fortschritt und Zielerreichung.

---

### Solution Architecture Methodology

**Ziel**

- Standardisierung der **Entwicklung** und **Beschreibung** von Lösungsarchitekturen.  
- Kombination aus:
  - **Development Process** → beschreibt Aktivitäten und Verantwortlichkeiten  
  - **View Model** → beschreibt, welche Informationen aus welchen Blickwinkeln dokumentiert werden

**Charakteristika**

- **Ganzheitlich:** betrachtet Problem aus mehreren Dimensionen (Business, Technik, Organisation).  
- **Iterativ & evolutionär:** Lösungen entwickeln sich über mehrere Zyklen.  
- **Inkrementell:** alle Views werden parallel und schrittweise verfeinert.

**Kernschritte**

1. **Architecture Context bestimmen:**  
   Analyse von **Inbound-** (Einflüsse aus Umfeld) und **Outbound-Dependencies** (Auswirkungen auf Umfeld).
2. **Architecture Conditions definieren & verfeinern:**  
   Identifiziere **architektur-signifikante** Bedingungen, die das Design wesentlich prägen.
3. **Alternativen entwickeln & bewerten:**  
   Mehrere Lösungsansätze anhand klarer Metriken vergleichen und die beste Variante auswählen.
4. **Solution Architecture ausarbeiten:**  
   Entwicklung eines konsistenten, nachvollziehbaren Designs mit klarer Traceability.
5. **Solution Architecture validieren:**  
   Überprüfen nach jeder Iteration, ob Ziel und Mandat erfüllt sind.

**Problem-to-Solution-Pfad**

Problem Statement → System Analysis → System Architecture → System Implementation

**Beispielmethodik: OpenUP**

- **OpenUP** (Eclipse Process Framework) ist eine **leichtgewichtige, iterative** Methodologie,  
  die Entwicklung, Architektur und Validierung eng verzahnt.  
- Unterstützt agile Prinzipien bei gleichzeitiger formaler Nachvollziehbarkeit.

---

### Kompakte Zusammenfassung (für Prüfung & Anwendung)

- **Frameworks** sind **Werkzeuge**, keine Ziele – sie müssen **angepasst** werden.  
- **TOGAF ADM** bietet einen **zyklischen Prozess** über *Transparency → Analysis → Design → Planning → Governance*.  
- **Architecture Mandate** definieren **Erwartungen und Erfolgskriterien**.  
- **Solution Architecture Methodology** beschreibt **iterative, nachvollziehbare** Entwicklungsschritte von **Problem zu Lösung**.  
- **Enterprise–Domain–Solution** sind **Ebenen** eines gemeinsamen Architekturprozesses – verbunden durch gemeinsame Artefakte und Repositories.

→ Ergebnis: Ein kohärenter, iterativer, kontextangepasster Architekturprozess,
der Struktur, Nachvollziehbarkeit und Qualität in der Lösungsentwicklung sicherstellt.
