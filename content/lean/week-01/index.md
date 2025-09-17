+++
title = "Week 01"
date = 2025-09-16
[taxonomies]
authors = ["fatlum"]
tags = ["lean"]
+++

# EID – Überblick & Workflow
---
## Überblick
Eine EID (External Interface Description) ist eine SGr-konforme XML-Datei, die mehrere Elemente umfasst:

- ein Interface (z. B. REST, MQTT, Bus/Modbus),
- ein oder mehrere Functional Profiles,
- und darin ein oder mehrere Datenpunkte.

Alle diese Teile gehören in eine gültige, SGr-konforme XML-Datei.
Die Schwierigkeit liegt vor allem in der korrekten Erstellung und in der Validierung.

Workflow (in unserer Software)

Auswahl beim Start:

EID erstellen, EID öffnen oder EID bearbeiten.

Wenn „Erstellen“ gewählt wird:

Interface auswählen
Beispiel (pseudomäßig als XML dargestellt):