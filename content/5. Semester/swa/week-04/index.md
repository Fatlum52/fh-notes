+++
title = "Week 04"
date = 2025-10-07
[taxonomies]
authors = ["fatlum"]
tags = ["swa"]
+++

## Software Architecture – Week 04

### Rückblick letzte Woche

**Architecture Constraints**

- Constraints wirken **direkt** auf die Architektur (z. B. Budget, Zeit, Skills, Regulatorik, vorgegebene Technologien).
- Sie **begrenzen den Lösungsraum** und erzwingen bestimmte Entscheidungen (z. B. Cloud-Vorgabe → bestimmte Managed Services).

**What is a Use Case?**

- Ein **Use Case** beschreibt **eine Interaktion** zwischen **Akteur** (z. B. User, externes System) und **System**, um einen **geschäftlichen Nutzen** zu erzielen.
- Typischer Aufbau: **Akteure**, **Vorbedingungen**, **Trigger**, **Hauptablauf (Happy Path)**, **Alternativ-/Fehlerpfade**, **Nachbedingungen**.
- Ziel: **Funktionale** Anforderungen **klar, testbar und nachverfolgbar** festhalten.

**Quality Attribute Scenarios**

- Nicht-funktionale Anforderungen präzise machen mit einem **Szenario-Template**:
  - **Source** (wer/was löst es aus),
  - **Stimulus** (Ereignis),
  - **Environment** (Betriebszustand),
  - **Artifact** (betroffener Teil),
  - **Response** (Reaktion),
  - **Response Measure** (messbares Kriterium, z. B. *p95 < 200 ms*).
- So werden **Qualitätsziele testbar** (Performance, Security, Availability, Modifiability, Usability, …).

**Warum „Architecture Significance“ bestimmen?**

- Fokus auf **entscheidende Architekturfragen** statt auf „Kosmetik“.
- **Kosten des Änderungsaufwands** früh sichtbar machen (Cost of Change).
- **Trade-offs** bewusst adressieren und **Risiken** (Neuheit, Volatilität) steuern.

**Warum „Architecture Approach“ als Methode?**

- **Direkte Traceability**: Von **Bedingungen/Anforderungen** zur **Lösungsskizze** und den **entscheidenden Designentscheidungen**.
- **Teil-Lösungen (Microarchitectures)**: Komplexe Systeme in **anschauliche Segmente** zerlegen (z. B. *AuthN/AuthZ*, *Reporting*, *Integration SAP*).
- **Wiederverwendung & Konsistenz**: Ansätze sind dokumentierte **Bausteine**, die man **wiederverwenden** und **weiterentwickeln** kann.

---

## Architecture Significance

**Kernidee**

- Architektur = **Menge bedeutender Designentscheidungen**, wobei „bedeutend“ über die **Kosten einer späteren Änderung** gemessen wird.
- Nicht jede Anforderung ist architekturrelevant. **Signifikant** sind Anforderungen, die zu **weitreichenden** Entscheidungen führen.

**Pragmatische Heuristik (Kurzfassung)**

- **Impact-Breite**: Beeinflusst die Bedingung **viele** Architekturentscheidungen gleichzeitig?
- **Stakeholder-Gewicht**: Kommt sie von **Business-kritischen** Stakeholdern?
- **Non-Functional**: Betrifft sie **Qualitätsattribute** (z. B. Availability, Security, Performance)?
- **Neuheit**: Haben wir **wenig Erfahrung** damit?
- **Volatilität**: Ändert sich das **oft** (→ hohe Anforderungen an **Modifiability**)?
- **Konfliktgrad**: **Trade-offs** nötig (z. B. Performance vs. Security)?
- **Strategische Relevanz**: Trägt sie **sichtbar** zur **Unternehmensstrategie** bei?

**Mini-Checkliste (für die Übung)**

1. **Bedingung** kurz in 1–2 Sätzen notieren.  
2. **Signifikanz** entlang der Heuristik einstufen (niedrig/mittel/hoch; 1–5).  
3. **Skizze** der **groben Komponenten** (nur Boxen & Pfeile denken).  
4. **Ein Komponentendetail** vertiefen (welche **Ansätze** kommen infrage?).  
5. **Reversibilität**: Was wäre **teuer/schwierig** rückgängig zu machen?

**Beispiele (Intuition)**

- *„24/7 hochverfügbar“* → **hoch** (betrifft Deployment-Topologie, Redundanz, LB, Observability).
- *„Logo oben links“* → **niedrig** (reiner UI-Aspekt).
- *„GDPR-konform“* → **hoch** (Datenhaltung, Prozesse, Logging, Verschlüsselung).
- *„Hinter SAP integrieren“* → **hoch** (Integrationsarchitektur, Datenflüsse, Verträge).

---

## Architecture Conditions (kurz & knackig)

**Was sind „Conditions“?**  

- **Requirements** (funktional & nicht-funktional), **Constraints** (harte Fakten) und **Assumptions** (Annahmen/Unsicherheiten).
- Gute Conditions sind **korrekt** (Stakeholder-validiert), **machbar**, **eindeutig** und **verifizierbar**.

**Wie erfassen?**

- **Use Cases** für **funktional**.  
- **Quality Attribute Scenarios** für **nicht-funktional, Constraints, Annahmen**.

---

## Architecture Approach (Zusammenfassung)

**Definition**

- Ein **Architecture Approach** ist eine **Teil-Lösung** (Microarchitecture), die **konkret** zeigt, **wie** eine oder mehrere **Conditions** umgesetzt werden.

**Was gehört rein?**

- **Referenz auf die Conditions** (Use Cases / QAS),  
- **Reaktionsprinzip** (welches Verhalten/Lösungsidee),  
- **Bausteine** (funktional, informationsbezogen, operativ),  
- **entscheidende Architekturentscheidungen** (z. B. *JAAS vs. eigener Provider*, *DB-Replikation vs. Synchronjobs*, *Sync vs. Async*).

**Nutzen**

- **Nachvollziehbarkeit** von **WHY → HOW**,
- **Diskussionsgrundlage** für Trade-offs,
- **Wiederverwendbare Bausteine** für ähnliche Anforderungen.

---

## Kompakte Zusammenfassung (für schnelle Prüfungsvorbereitung)

- **Use Cases** klären **WAS** das System tun soll; **QAS** machen **Qualität messbar**.  
- **Signifikanz** priorisiert unsere Zeit: konzentriere dich auf Punkte mit **hohem Änderungsrisiko/-preis**.  
- **Heuristik** (Impact, Stakeholder, NFR, Neuheit, Volatilität, Konflikt, Strategie) hilft, „wichtig vs. unwichtig“ zu trennen.  
- **Architecture Approaches** liefern **konkrete, nachvollziehbare** Teil-Lösungen und verbinden **Bedingungen ↔ Entscheidungen**.  
- Outcome: **gerichtete Architekturarbeit**, weniger „Nice-to-have“, mehr **entscheidende** Entscheidungen sauber dokumentiert.
