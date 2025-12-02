+++
title = "Final Test Zusammenfassung"
date = 2025-12-02
[taxonomies]
authors = ["fatlum"]
tags = ["swa"]
+++

# Final Test Zusammenfassung

## Prüfungsformat

1. **3 Fragen zu Architecture Condition, Significance, Approach** (3 x 2P = 6P)
   - Bedeutungen/Unterschiede/Beispiele

2. **6 Multiple Choice Fragen zu Architecture Methodology** (6 x 0.5P = 3P)

3. **Pseudo-Code für Klassen und Interfaces schreiben** (6P)
   - UML-Diagramm gegeben, Pseudo-Code schreiben

4. **Aufgaben zu Pattern und Pattern Language** (3P + 6P + 9P = 18P)
   - Multiple Choice
   - 6 Beschreibungen gegeben, Pattern herausfinden
   - 3 Patterns gegeben, beschreiben und Beispiele geben

5. **Logical View, Klassen und Objekte, Development View / UML erstellen** (4P + 2P + 4P = 10P)
   - Analog zur Zwischenprüfung, anderer Use Case
   - **Kletterer im Kletterpark**: Kletterrouten, Aufwärmbereich, Warteschlangen, Zufallsgenerator für Dauer, Ausgang mit Melden der Aufenthaltsdauer

---

## 1. Architecture Conditions, Significance, Approach (6P)

### Architecture Conditions

**Definition**: Conditions als motivatoren für architektur. Architecture conditions sind kräfte, auf die die architektur reagieren muss. System von kräften, die architektur ausbalancieren muss.

**Anforderungen**:

- **Correct**: nur stakeholder können das beurteilen
- **Feasible**: muss mit verfügbaren mitteln realisierbar sein
- **Unambiguous**: nur eine interpretation möglich
- **Verifiable**: muss verifizierbar sein

**Types of Conditions**:

- **Requirements**: wünsche einer organisation
  - **Functional Requirements**: existenzielle bedürfnisse, grund für system-existenz
  - **Non-Functional Requirements**: nicht existentiell, aber essentiell (wie system funktioniert)
- **Constraints**: faktische einschränkungen, die nicht umgangen werden können (zeit, skills, budget)
- **Assumptions**: bekannte unsicherheiten (known unknowns), wahrscheinlich zukünftige bedingungen

**Capturing**:

- **Use Cases**: für functional requirements
- **Quality Attribute Scenarios**: für non-functional requirements, constraints, assumptions

### Architecture Significance

**Definition (Grady Booch)**: "Architecture is the set of significant design decisions that shape a system, where significant is measured by cost of change"

Eine requirement ist significant, wenn das design schwer zu ändern/abbauen/anpassen ist, sollte die requirement sich ändern.

**Heuristik zur Bestimmung**:

1. **Number of impacts**: anzahl der architektur-entscheidungen die nötig sind
2. **Stakeholder importance**: wichtigkeit der stakeholder (business > technical)
3. **Non-functionality**: non-functional conditions haben oft große auswirkungen
4. **Novelty**: grad der ungewöhnlichkeit/neuheit
5. **Volatility**: wahrscheinlichkeit dass condition sich ändert
6. **Degree of conflict**: konflikte mit anderen conditions, trade-offs nötig
7. **Degree of strategic orientation**: beitrag zu strategischen zielen

**Beispiele für Architecture-Significant Requirements**:

- System muss 24/7 hochverfügbar sein
- System muss GDPR-konform sein
- System muss in SAP integriert werden
- System muss cloud-native sein
- System muss multi-client fähig sein
- System muss real-time requirements erfüllen
- System muss machine learning unterstützen

### Architecture Approach

**Definition**: Teil einer gesamten architektur. Jeder approach adressiert eine teilmenge der conditions eines problems. Aus sicht des gesamtdesigns: partial solution. Auch genannt: solution design segments, microarchitectures.

**Eigenschaften**:

- wird mit gleichen methoden geplant/designed/beschrieben wie gesamte architektur
- implementiert eine oder mehrere conditions
- für functional requirement: design das use case realisiert
- für non-functional requirement: spezifiziert wie quality attribute scenario realisiert wird
- ermöglicht traceability zwischen conditions und decisions

**Beschreibt**:

- impact (force) auf system
- desired response (behavior)
- architecture building blocks (statisch und dynamisch)
- architecture decisions

### Unterschiede

- **Conditions**: was sind die rahmenbedingungen (requirements, constraints, assumptions)
- **Significance**: welche conditions sind wichtig (cost of change, impacts, volatility)
- **Approach**: wie adressieren wir conditions (partial solution, design segments)

---

## 2. Architecture Methodology (3P - Multiple Choice)

### Was ist Architecture Methodology

- strukturierte vorgehensweise zur entwickelung von software-architektur
- systematisch leitet anstrengungen und aktivitäten zu definierten zielen
- spezifiziert validen zustands- und transitions-raum
- erhöht systematizität und wiederholbarkeit

### Wichtige Aspekte

- **Method**: systematisches, schrittweises verfahren
- jeder schritt spezifiziert: benötigte information, generierte information, verantwortliche rolle
- **Methodology**: tiefe struktur der methode und komplementäre bausteine
- erleichtert diskussionen über angemessenheit von designs

### Vorgehen bei Architecture Methodology

1. **Requirements analysieren**
2. **Architecture conditions identifizieren und refinieren**
   - innerhalb der gegebenen conditions, die architecture-significant identifizieren
3. **Solution architecture entwickeln**
   - design entwickeln um architecture conditions zu adressieren
   - traceability sicherstellen
4. **Iterativ verfeinern**

### Framework Adaptation

- frameworks müssen an kontext angepasst werden
- art der anwendung: relevante von irrelevanten teilen unterscheiden
- voraussetzung: ziele müssen klar sein
- verschiedene typen von architecture methodologies:
  - Solution Architecture Development (z.B. Unified Process, TOGAF, ArchiMate)
  - Enterprise and Domain Architecture Elaboration (z.B. TOGAF, Zachman)
  - Reference Architecture Elaboration
  - Architecture Assessment Methodology (z.B. ATAM)

---

## 3. Pseudo-Code für UML (6P)

### Wichtige UML-Elemente für Pseudo-Code

#### Klasse

```pseudo
class ClassName {
    - attribute1: Type
    - attribute2: Type
    + method1(param: Type): ReturnType
    + method2(): void
}
```

#### Interface

```pseudo
interface InterfaceName {
    + method1(param: Type): ReturnType
    + method2(): void
}
```

#### Vererbung

```pseudo
class SubClass extends SuperClass {
    // erbt alle methoden und attribute von SuperClass
}
```

#### Implementierung

```pseudo
class ClassName implements InterfaceName {
    // muss alle methoden von InterfaceName implementieren
}
```

#### Assoziationen

- **Komposition** (diamant, ausgefüllt): starke besitz-beziehung
- **Aggregation** (diamant, leer): schwache besitz-beziehung
- **Assoziation** (linie): allgemeine beziehung
- **Abhängigkeit** (gestrichelte linie): verwendet, aber nicht besitzt

#### Beispiel

```pseudo
class Order {
    - orderId: String
    - date: Date
    - items: List<OrderItem>
    
    + addItem(item: OrderItem): void
    + calculateTotal(): Money
    + getOrderId(): String
}

class OrderItem {
    - quantity: int
    - product: Product
    
    + getQuantity(): int
    + getProduct(): Product
}

interface OrderRepository {
    + save(order: Order): void
    + findById(id: String): Order
}

class DatabaseOrderRepository implements OrderRepository {
    - connection: DatabaseConnection
    
    + save(order: Order): void {
        // speichere order in datenbank
    }
    
    + findById(id: String): Order {
        // lade order aus datenbank
    }
}
```

---

## 4. Patterns und Pattern Language (18P)

### Pattern Definition

**Pattern Triad**:

- **Context**: kontext in dem pattern angewendet wird
- **Problem**: wiederkehrendes problem
- **Solution**: bewährte lösung

**Pattern Attribute**:

- Name
- Also known as (synonyme)
- Type (creational, structural, behavioral, architectural)
- Problem
- Context
- Forces
- Proposed Solution
- Consequences
- Related Patterns
- Known uses

### Pattern Language

- sammlung von zusammenhängenden patterns
- patterns bauen aufeinander auf
- gemeinsame terminologie
- ermöglicht komplexe probleme zu lösen durch kombination mehrerer patterns

### Wichtige Patterns für Prüfung

#### Creational Patterns

**Factory Method**:

- erstellt objekte ohne genaue klasse zu spezifizieren
- abstrakte methode zur objekt-erstellung
- subklassen implementieren erstellung

**Abstract Factory**:

- erstellt familien verwandter objekte
- mehrere factory-methoden für verschiedene produkt-typen

**Builder**:

- konstruiert komplexe objekte schrittweise
- trennt konstruktion von repräsentation

**Singleton**:

- stellt sicher, dass nur eine instanz existiert
- globaler zugriffspunkt

#### Structural Patterns

**Adapter**:

- problem: zwei komponenten müssen zusammenarbeiten trotz inkompatibler interfaces
- solution: wrapper um adaptee, implementiert target interface
- uses: JDBC drivers, interface converters

**Decorator**:

- problem: funktionalität muss dynamisch hinzugefügt werden
- solution: wrap components in decorators, implementiert gleiche interface
- uses: stream I/O filters, GUI features

**Facade**:

- problem: komplexe subsystems überwältigen clients
- solution: single high-level interface
- uses: API gateways, persistence libraries

**Proxy**:

- problem: zugriff muss kontrolliert oder erweitert werden
- solution: proxy implementiert subject interface, fügt behavior hinzu
- uses: virtual proxies, RMI stubs, AOP interceptors

#### Behavioral Patterns

**Strategy**:

- problem: mehrere algorithmen für eine aufgabe
- solution: familie von strategies mit common interface
- uses: sorting, payment algorithms

**Observer (Publish-Subscribe)**:

- problem: viele objekte brauchen automatische updates
- solution: subjects maintain subscriber lists
- uses: UI bindings, message brokers

**Command**:

- problem: method calls müssen delayed, queued, oder undone werden
- solution: encapsulate action in command object mit execute()
- uses: GUI buttons, transactional job queues

**Template Method**:

- problem: teile eines algorithmus variieren, aber struktur ist fest
- solution: template method definiert skeleton, subklassen implementieren schritte
- uses: parsing frameworks, batch job templates

**State**:

- problem: objekt verhalten ändert sich bei zustandsänderung
- solution: zustand als objekt
- uses: TCP connection states, vending machines

**Chain of Responsibility**:

- problem: mehrere handler können request verarbeiten
- solution: link handlers in chain, jeder verarbeitet oder gibt weiter
- uses: servlet filters, exception chains

#### Architectural Patterns

**Layers**:

- problem: mixing presentation, business, und technical logic verursacht rigidity
- solution: struktur in stacked layers, jede nutzt services der unteren
- uses: 3-tier web apps, OSI stack

**Model-View-Controller (MVC)**:

- problem: tight coupling zwischen UI und business logic
- solution: divide in Model (data), View (presentation), Controller (input coordination)
- uses: web frameworks, GUI toolkits

**Pipes and Filters**:

- problem: daten müssen serie von transformationen durchlaufen
- solution: struktur als filters verbunden durch pipes
- uses: UNIX pipelines, ETL systems

**Shared Repository**:

- problem: mehrere komponenten brauchen shared access zu konsistenten daten
- solution: zentraler daten-store über definierte interfaces
- uses: compilers, data hubs, version control systems

**Microkernel**:

- problem: systeme müssen leicht erweiterbar sein ohne stabilen core zu beeinflussen
- solution: minimal core mit basic services und extension points, plug-ins fügen funktionalität hinzu
- uses: Eclipse, JBoss, Mach kernel

**Reflection**:

- problem: system muss eigene struktur zur laufzeit inspizieren/modifizieren
- solution: represent classes/methods as meta-objects
- uses: Java Reflection API, dependency injection

### Pattern Identifikation - Tipps

- **Problem lesen**: was ist das wiederkehrende problem?
- **Context erkennen**: in welchem kontext tritt problem auf?
- **Solution analysieren**: wie wird problem gelöst?
- **Forces beachten**: welche kräfte müssen balanciert werden?
- **Consequences prüfen**: was sind vor- und nachteile?

---

## 5. Logical View, Development View, UML (10P)

### Logical View

- zeigt logische struktur des systems
- klassen, interfaces, beziehungen
- unabhängig von deployment
- fokus auf funktionalität

**Elemente**:

- Klassen mit attributen und methoden
- Interfaces
- Beziehungen: inheritance, implementation, association, composition, aggregation
- Stereotypes: `<<Entity>>`, `<<ValueObject>>`, `<<Aggregate>>`, `<<Repository>>`, `<<Service>>`, `<<Factory>>`

### Development View

- zeigt struktur aus entwickler-sicht
- packages, modules, komponenten
- code-organisation
- build-struktur

**Elemente**:

- Packages
- Module/Components
- Dependencies zwischen packages
- Interfaces zwischen komponenten

### Objektdiagramm

- zeigt instanzen zur laufzeit
- konkrete objekte mit werten
- beispiel: `order1:Order { orderId = "ORD-001", date = 2025-12-02 }`

### UML-Diagramme erstellen

#### Vollständiges Klassendiagramm mit Kardinalitäten

```bash
┌─────────────────────┐
│      Climber        │
├─────────────────────┤
│ - climberId: String │
│ - name: String      │
│ - entryTime: Time   │
│ - exitTime: Time    │
│ - status:           │
│   ClimberStatus     │
├─────────────────────┤
│ + enterPark()       │
│ + joinQueue()       │
│ + startRoute()      │
│ + exitPark()        │
│ + getDuration()     │
└─────────────────────┘
        │
        │ 0..1         ┌─────────────────────┐
        │              │      Route          │
        │              ├─────────────────────┤
        │              │ - routeId: String   │
        │              │ - name: String     │
        │              │ - difficulty:      │
        │              │   Difficulty       │
        │              ├─────────────────────┤
        │              │ + addToQueue()     │
        │              │ + serveNext()      │
        │              │ + calculateDuration()│
        │              │ + getQueueLength() │
        │              └─────────────────────┘
        │                      │
        │                      │ 1..1 (Komposition)
        │                      │
        │                      ▼
        │              ┌─────────────────────┐
        │              │       Queue         │
        │              ├─────────────────────┤
        │              │ - queueId: String  │
        │              │ - queueType:       │
        │              │   QueueType        │
        │              │ - waitingClimbers: │
        │              │   List<Climber>    │
        │              ├─────────────────────┤
        │              │ + add()            │
        │              │ + removeFirst()    │
        │              │ + getLength()      │
        │              │ + isEmpty()        │
        │              └─────────────────────┘
        │                      ▲
        │                      │
        │                      │ 0..*
        │                      │
        │              (Climber in Queue)
        │
        │ 0..1
        │
        ▼
┌─────────────────────┐
│    WarmUpArea       │
├─────────────────────┤
│ - areaId: String    │
│ - capacity: int     │
│ - currentClimbers:  │
│   List<Climber>     │
├─────────────────────┤
│ + enter()           │
│ + exit()            │
│ + calculateWarmUpTime()│
└─────────────────────┘
        ▲
        │
        │ 0..* (Climber im WarmUpArea)

┌─────────────────────┐
│   RandomGenerator   │
├─────────────────────┤
│ + generateRouteDuration()│
│ + generateWarmUpTime()   │
└─────────────────────┘
        ▲
        │
        │ <<uses>> (Dependency)
        │
        ├──────────────┐
        │              │
┌───────┴──────┐  ┌────┴──────────┐
│    Route     │  │  WarmUpArea   │
└──────────────┘  └───────────────┘

┌─────────────────────┐
│        Exit         │
├─────────────────────┤
│ + recordDuration()  │
└─────────────────────┘
        │
        │ 1..1 (Komposition)
        │
        ▼
┌─────────────────────┐
│ StatisticsCollector │
├─────────────────────┤
│ - durations:        │
│   List<Duration>    │
│ - queueLengths:     │
│   Map<Queue,        │
│   List<int>>        │
├─────────────────────┤
│ + recordDuration()  │
│ + recordQueueLength()│
│ + generateStatistics()│
└─────────────────────┘
        ▲
        │
        │ 0..* (sammelt von)
        │
        ├──────────────────┐
        │                  │
┌───────┴──────┐  ┌────────┴────────┐
│   Climber    │  │      Queue      │
└──────────────┘  └─────────────────┘

┌─────────────────────┐
│     QueueType       │
│      (enum)         │
├─────────────────────┤
│ ROUTE_QUEUE         │
│ EXIT_QUEUE          │
└─────────────────────┘
        ▲
        │
        │ (Queue verwendet QueueType)
        │
┌───────┴──────┐
│     Queue    │
└──────────────┘
```

#### Kardinalitäten erklärt

- **Route 1..1 ── Queue**: Jede Route hat genau eine Queue (Komposition)
- **Climber 0..1 ── Route**: Ein Climber kann aktuell auf 0 oder 1 Route sein
- **Queue 0..* ── Climber**: Eine Queue kann 0 bis viele Climber enthalten
- **Climber 0..1 ── WarmUpArea**: Ein Climber kann in 0 oder 1 WarmUpArea sein
- **WarmUpArea 0..* ── Climber**: Ein WarmUpArea kann 0 bis viele Climber enthalten
- **Exit 1..1 ── StatisticsCollector**: Exit hat genau einen StatisticsCollector (Komposition)
- **StatisticsCollector 0..* ── Climber**: Sammelt von 0 bis vielen Climber
- **StatisticsCollector 0..* ── Queue**: Sammelt von 0 bis vielen Queue

#### Sequenzdiagramm

```bash
Climber    Queue    Route    RandomGenerator    Exit
   │         │        │            │              │
   │──enter──>│        │            │              │
   │         │        │            │              │
   │         │──join──>│            │              │
   │         │        │            │              │
   │         │        │<--calc----│              │
   │         │        │            │              │
   │         │<--done--│            │              │
   │<--start--│        │            │              │
   │         │        │            │              │
   │──exit--->│        │            │              │
   │         │        │            │              │
   │         │        │            │              │
   │         │        │            │<--duration---│
```

---

## Beispiel: Kletterer im Kletterpark

### Szenario

Ein simulationsprogramm soll die essensausgabe im campus-restaurant simulieren, um statistische daten für optimierung zu ermitteln. Bei der simulation kommt es vor allem darauf an, die länge von warteschlangen an verschiedenen theken und die aufenthaltszeiten von gästen zu ermitteln.

**Analoges Szenario: Kletterer im Kletterpark**:

Das simulationsprogramm soll den betrieb eines kletterparks simulieren, um statistische daten für optimierung zu ermitteln. Bei der simulation kommt es vor allem darauf an, die länge von warteschlangen an verschiedenen kletterrouten und die aufenthaltszeiten von kletterern zu ermitteln.

### Ablaufszenario

1. **Kletterer A** betritt zu einer im voraus im simulationsplan festgelegten zeit den kletterpark, in dem sich bereits mehrere andere kletterer befinden können.

2. **Kletterer A** möchte die route "schwierig" klettern, begibt sich zur entsprechenden route und stellt sich dort in einer warteschlange an.

3. **Kletterer B** betritt zu einer im voraus im simulationsplan festgelegten zeit den kletterpark.

4. **Kletterer B** möchte sich im aufwärmbereich aufwärmen. Die dafür nötige zeit hängt nach einer noch zu bestimmenden formel von der anzahl der kletterer ab, die sich zur gleichen zeit im aufwärmbereich befinden.

5. An der route "schwierig" wird jeweils der erste kletterer in der warteschlange bedient und erhält nach einer für alle klettervorgänge festgelegten zeitspanne (berechnet durch zufallsgenerator) zugang zur route.

6. **Kletterer A** geht, nachdem er zugang zur route erhalten hat, zur route und beginnt zu klettern.

7. **Kletterer B** geht, nachdem er sich aufgewärmt hat, zur route "leicht" und stellt sich dort in der warteschlange an.

8. An der route wird jeweils der erste kletterer in der warteschlange um zugang gebeten.

9. Der klettervorgang nimmt eine (vom zufallsgenerator berechnete) zeit in anspruch. Anschließend verlassen die kletterer die route.

10. Jeder kletterer meldet beim verlassen des kletterparks die verweildauer (zeitspanne vom eintreten bis zum verlassen) an ein objekt, das diese werte sammelt. Die gesammelten werte werden am ende der simulation statistisch ausgewertet.

### Logical View - Klassen

#### Design-Entscheidung: Queue als wiederverwendbare Komponente

**Warum generische Queue besser ist**:

- **Wiederverwendbarkeit**: Queue kann für verschiedene Zwecke verwendet werden (Route, Exit, etc.)
- **Single Responsibility Principle**: Queue ist nur für Warteschlangen-Logik zuständig
- **Flexibilität**: Neue Queue-Typen können einfach hinzugefügt werden (z.B. Exit-Queue)
- **Loose Coupling**: Route hält Queue, aber Queue ist unabhängig von Route
- **Bessere Testbarkeit**: Queue kann isoliert getestet werden

**Alternative (Route hält Queue direkt)**: Würde zu starker Kopplung führen und Queue nicht wiederverwendbar machen.

#### Hauptklassen

```pseudo
class Climber {
    - climberId: String
    - name: String
    - entryTime: Time
    - exitTime: Time
    - currentRoute: Route
    - status: ClimberStatus
    
    + enterPark(): void
    + joinQueue(route: Route): void
    + startRoute(route: Route): void
    + exitPark(): void
    + getDuration(): Duration
}

class Route {
    - routeId: String
    - name: String
    - difficulty: Difficulty
    - queue: Queue  // Route hält eine Queue-Instanz (Komposition)
    - currentClimber: Climber
    
    + addToQueue(climber: Climber): void  // delegiert an queue.add()
    + serveNext(): Climber  // delegiert an queue.removeFirst()
    + calculateDuration(climber: Climber): Duration
    + getQueueLength(): int  // delegiert an queue.getLength()
}

class WarmUpArea {
    - areaId: String
    - currentClimbers: List<Climber>
    - capacity: int
    
    + enter(climber: Climber): void
    + exit(climber: Climber): void
    + calculateWarmUpTime(climber: Climber): Duration
}

class Queue {
    - queueId: String
    - queueType: QueueType
    - waitingClimbers: List<Climber>
    
    + add(climber: Climber): void
    + removeFirst(): Climber
    + getLength(): int
    + isEmpty(): boolean
    + getQueueType(): QueueType
}

enum QueueType {
    ROUTE_QUEUE
    EXIT_QUEUE
    // erweiterbar für zukünftige anforderungen
}

class RandomGenerator {
    + generateRouteDuration(route: Route, climber: Climber): Duration
    + generateWarmUpTime(climber: Climber, area: WarmUpArea): Duration
}

class Exit {
    - statisticsCollector: StatisticsCollector
    
    + recordDuration(climber: Climber): void
}

class StatisticsCollector {
    - durations: List<Duration>
    - queueLengths: Map<Queue, List<int>>
    
    + recordDuration(duration: Duration): void
    + recordQueueLength(queue: Queue, length: int): void
    + generateStatistics(): Statistics
}
```

### Development View - Packages

```bash
com.kletterpark
├── domain
│   ├── Climber
│   ├── Route
│   ├── WarmUpArea
│   └── Queue
├── infrastructure
│   ├── RandomGenerator
│   └── StatisticsCollector
└── application
    ├── Exit
    └── SimulationController
```

### Sequenzdiagramm - Kletterer durchläuft Park

#### Szenario 1: Kletterer A klettert Route "Schwierig"

```bash
Climber    Route    Queue    RandomGenerator    Exit    StatisticsCollector
   │         │        │            │             │            │
   │──enterPark()────>│            │             │            │
   │         │        │            │             │            │
   │──joinQueue(route)────────────>│             │            │
   │         │        │            │             │            │
   │         │        │──add(climber)───────────>│            │
   │         │        │            │             │            │
   │         │──serveNext()───────>│             │            │
   │         │        │            │             │            │
   │         │        │<──removeFirst()─────────│            │
   │         │        │            │             │            │
   │         │<──calculateDuration()─────────────│            │
   │         │        │            │             │            │
   │         │        │            │<──generateRouteDuration()│
   │         │        │            │             │            │
   │         │<──duration──────────│             │            │
   │         │        │            │             │            │
   │<──startRoute()───│            │             │            │
   │         │        │            │             │            │
   │[klettert route]  │            │             │            │
   │         │        │            │             │            │
   │──exitPark()─────────────────────────────────>│            │
   │         │        │            │             │            │
   │         │        │            │             │──recordDuration()──>│
   │         │        │            │             │            │
   │         │        │            │             │            │<──store()
```

#### Szenario 2: Kletterer B nutzt WarmUpArea, dann Route "Leicht"

```bash
Climber    WarmUpArea    Route    Queue    RandomGenerator    Exit    StatisticsCollector
   │            │          │        │            │             │            │
   │──enterPark()──────────│        │            │             │            │
   │            │          │        │            │             │            │
   │──enter()──>│          │        │            │             │            │
   │            │          │        │            │             │            │
   │            │<──calculateWarmUpTime()────────│             │            │
   │            │          │        │            │             │            │
   │            │          │        │            │<──generateWarmUpTime()│
   │            │          │        │            │             │            │
   │            │<──duration────────│            │             │            │
   │            │          │        │            │             │            │
   │[wärmt sich auf]       │        │            │             │            │
   │            │          │        │            │             │            │
   │──exit()───>│          │        │            │             │            │
   │            │          │        │            │             │            │
   │──joinQueue(route)───────────────────────────>│            │             │
   │            │          │        │            │             │            │
   │            │          │        │──add(climber)───────────>│            │
   │            │          │        │            │             │            │
   │            │          │──serveNext()───────>│             │            │
   │            │          │        │            │             │            │
   │            │          │        │<──removeFirst()─────────│            │
   │            │          │        │            │             │            │
   │            │          │<──calculateDuration()────────────│            │
   │            │          │        │            │             │            │
   │            │          │        │            │<──generateRouteDuration()│
   │            │          │        │            │             │            │
   │            │          │<──duration─────────│             │            │
   │            │          │        │            │             │            │
   │<──startRoute()────────│        │            │             │            │
   │            │          │        │            │             │            │
   │[klettert route]       │        │            │             │            │
   │            │          │        │            │             │            │
   │──exitPark()──────────────────────────────────────────────>│            │
   │            │          │        │            │             │            │
   │            │          │        │            │             │──recordDuration()──>│
   │            │          │        │            │             │            │
   │            │          │        │            │             │            │<──store()
```

#### Hinweis

WarmUpArea ist kein aktiver Teilnehmer im Sequenzdiagramm, sondern ein Ort wo Climber sich aufhalten. Die Interaktionen sind:

- Climber betritt WarmUpArea (enter())
- WarmUpArea berechnet Aufwärmzeit (mit RandomGenerator)
- Climber verlässt WarmUpArea (exit())

### Objektdiagramm'

```bash
climber1:Climber {
    climberId = "C001"
    name = "Max"
    entryTime = 10:00
    exitTime = 11:30
    currentRoute = route1
}

route1:Route {
    routeId = "R001"
    name = "Schwierig"
    difficulty = HARD
    queue = queue1
}

queue1:Queue {
    queueId = "Q001"
    waitingClimbers = [climber1, climber2]
}
```

### Wichtige Aspekte für Prüfung

- **Klassen identifizieren**: aus szenario die wichtigsten entitäten extrahieren
- **Beziehungen modellieren**: welche klassen hängen zusammen?
- **Methoden definieren**: welche operationen sind nötig?
- **Stereotypes verwenden**: `<<Entity>>`, `<<ValueObject>>`, etc.
- **Packages strukturieren**: domain, infrastructure, application
- **Sequenzdiagramm**: interaktionen zwischen objekten zeigen
- **Objektdiagramm**: konkrete instanzen mit werten

---

## Zusammenfassung - Wichtigste Punkte

### Architecture Conditions, Significance, Approach

- **Conditions**: requirements, constraints, assumptions
- **Significance**: cost of change, 7 heuristiken
- **Approach**: partial solution, traceability

### Architecture Methodology

- systematische vorgehensweise
- conditions identifizieren und refinieren
- solution architecture entwickeln
- framework adaptation

### Patterns

- pattern triad: context, problem, solution
- creational, structural, behavioral, architectural
- pattern language: zusammenhängende patterns

### UML

- logical view: klassen, interfaces, beziehungen
- development view: packages, modules
- sequenzdiagramm: interaktionen
- objektdiagramm: instanzen

### Beispiel Kletterpark

- ähnlich wie restaurant-beispiel
- kletterer, routen, warteschlangen, aufwärmbereich
- zufallsgenerator für dauer
- ausgang mit statistikerfassung
