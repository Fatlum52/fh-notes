+++
title = "Week 02"
date = 2025-09-23
[taxonomies]
authors = ["fatlum"]
tags = ["swa"]
+++

# Software Architecture – Week 02

## Fragen von Menti

### Modell
- Ein Modell repräsentiert immer etwas Reales oder Abstraktes.
- Modelle vereinfachen die Realität, um Systeme besser verstehen, kommunizieren und entwerfen zu können.

### View Model
- **Viewpoint**: entspricht einer Klasse (definiert, wie man ein System betrachtet).
- **View**: ist eine Instanz des Viewpoints (konkrete Sicht auf das System).
- **View-Model** = Sichtenmodell → kombiniert verschiedene Views zu einem Gesamtmodell.

---

### Frage: *How do View Models support the process of designing software architecture?*
- Das **Kruchten 4+1 View Model** unterstützt die Architekturarbeit.
- Es legt die Reihenfolge gewisser Prozesse und Perspektiven fest.
- Beiträge in verschiedenen Phasen:
  - frühes Testen der Architektur „auf Papier“
  - Stabilität durch konsistente Abbildungen
  - Reduzierung von Implementierungskosten
- Architektur wird so iterativ entworfen, durch Szenarien abgesichert und auf Konsistenz geprüft.

---

### Frage: *Name the 5 viewpoints of the Kruchten 4+1 View Model*
1. **Logical View**
2. **Development View**
3. **Process View**
4. **Physical View**
5. **Scenarios (Use Cases)**

---

### Frage: *Why does the View Model refer to 4+1 viewpoints and not 5?*
- Unterschied: **Scenarios** sind keine Lösungsbeschreibung, sondern erfassen Problemstellungen und konkrete Anwendungsfälle.
- **Use Cases** sind generisch, **Szenarien** sind Instanzen davon.
- Szenarien „kleben“ die anderen Views zusammen:
  - zeigen, wie die Building Blocks orchestriert werden
  - geben Hinweise, wie Architekturbausteine angeordnet werden
  - sichern Konsistenz aller Views ab

---

### Frage: *What does the low representational gap require from a good software design?*
- Fachlichkeit und Software-Repräsentation sollen **nahe beieinander** liegen.
- OOP ist ein Beispiel: Realität lässt sich gut in Klassen und Objekte modellieren.
- **Gute Namenskonventionen** und ein enger Bezug zur Fachdomäne sind entscheidend.

---

## Aufgabe: Gaming Platform (Iteration #1)

### Szenario
- Eine **Gaming Plattform** soll entworfen werden:
  - Spieler registrieren sich mit Name, Account, Passwort, Rolle (Player, Admin, Provider).
  - Login mit Account und Passwort.
  - Spiele müssen von Admins hinzugefügt werden, bevor sie im Katalog erscheinen.
  - Spieler können Spiele in **Favoriten** aufnehmen.
  - Spiele werden simuliert: Gewinner, Dauer (1–100 min) und Score (1–100 Punkte) werden zufällig bestimmt.
  - Ergebnisse landen in einer **Highscore-Liste**.
  - Zunächst: **3 Spiele** (Schach, Tic Tac Toe, Vier gewinnt).
- Umsetzungsschritte: Use Cases → Szenarien → Logical View → Development View → Java-Code.

---

### Logical View
- Realisierung durch **UML-Sequenzdiagramme**:
  - zeigen, wie Objekte im Szenario interagieren.
  - Bsp.: `Register User`, `Login`, `Select Game`, `Launch Game`, `View High Score`.
- Sequenzdiagramme sichern die Konsistenz zwischen Use Cases und Objekten.

---

### Development View
- Abgeleitet aus den Sequenzdiagrammen:
  - Sequenz-Titel → Klassen in Java.
  - Ergebnis: Klassendiagramm (Analysemodell).
- Danach Übergang zum Systemdesign:
  - Analysemodell wird um technische Details erweitert.
  - Schnittstellen zwischen Klassen klar definiert.

---

### Process View
- Betrachtet die **laufenden Programme/Prozesse**:
  - Gibt es mehrere eigenständige Prozesse?
  - Anforderungen an Parallelität, Synchronisation, Kommunikation.
- Beispiel: unterschiedliche Services (User-Management, Game-Engine, Highscore-Service).
- Prozesse laufen auf dem **Physical View**.

---

### Physical View
- Physische Verteilung (Deployment):
  - Wo laufen die einzelnen Prozesse?
  - Wie werden sie auf Hardware/Knoten verteilt?
  - Welche Ressourcen (z.B. Server, Container) werden benötigt?

---

### Verbindung der Views
- **Logical, Development, Process und Physical View** werden in einem Szenario konsistent zusammengedacht.
- Szenario-Driven Design:
  - Schrittweise von Szenarien → Logical View → Development View → Prozess & Deployment.
  - Endgültig Umsetzung in Java.

---

### Umsetzung in Java
- Entwicklung in mehreren Iterationen:
  - Interfaces definieren, damit Klassen lose gekoppelt bleiben.
  - Objekte werden in einer **Composer-Klasse** instanziert und verbunden.
- Beispiel-Szenario in der `Client`-Klasse:
  1. Drei User registrieren und einloggen.
  2. Drei Spiele instanziieren und hinzufügen.
  3. Favoritenlisten füllen und Spiele starten.
  4. Highscore-Listen anzeigen.

---

## Visualisierung

### 4+1 View Model (Kruchten)
![4+1 View Model](https://upload.wikimedia.org/wikipedia/commons/7/7b/4%2B1_View_Model.png)

### Beispiel UML-Sequenzdiagramm
```plantuml
@startuml
actor Player
Player -> Platform: login(username, password)
Platform -> Session: createSession()
Session --> Platform: success
Platform --> Player: loginSuccess
@enduml
