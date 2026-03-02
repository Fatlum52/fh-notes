+++
title = "Week 02"
date = 2026-03-02
[taxonomies]
authors = ["fatlum"]
tags = ["cysL"]
+++

---

## Attacken

### Billion Laughs

### ZIP Bomb

### Fork Bomb

### Smashing the Stack

### Overflow-Attacken

- Stack Overflow
- Heap Overflow

- Format String Attacks
  - In Buffer rein schreiben obwohl man das nicht darf

- Integer Overflow
  - Wenn man Ausserhalb des Zahlen bereichs kommt

### Metasploit Framework (msf)

- wird verwendet um schadsoftware zu machen
- ansammlung von skripten und exploits die man verwenden kann
- typischerweise uralte exploits da drin

### Angriffsszenarien

- Lokale HW
- Lokale Ausführung ("EXE" Ausführen)
- Netzwerkdienste
- Ein Netzwerksocket-Client oder dessen Plugins
- OIC ausbrechen ist viel einfacher als VM
- uralte racecondition in Linux Kernel, mit ch root kann man da easi ausbrechen

### Detektion

- Malware-Scanner
  - Pattern matching
  - behavioural detection
  - statistical detection
- HW features
  - DEP
  - NX
- OS features
  - ASLR
- Applikationsfeatures
  - Canaries
  - Kleine Files zwischen Hauptfiles, wenn eine Applikation malware hat, diese Canaries verändert wird
    und man so weiss, dass Malware vorhanden ist
