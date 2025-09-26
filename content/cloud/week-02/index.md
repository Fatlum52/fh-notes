+++
title = "Week 02"
date = 2025-09-26
[taxonomies]
authors = ["fatlum"]
tags = ["cloud"]
+++

## Virtualization

- **abstraction vs virtualization**
  - **abstraction**
    - tieferes Level verstecken
    - OS macht das oft
    - ein File ist eine Abstraktion von Storage-Blöcken
  - **virtualization**
    - virtuelle Repräsentation einer Ressource
    - nichts wird versteckt
    - volle Flexibilität über Speicher und andere Komponenten

***VM***
- **process virtual machine**
  - kein typischer Rechner
  - nutzt Intermediate Language, z. B. Java Bytecode
  - Bsp.: JVM
- **system virtual machine**
  - versucht die komplette Hardware zu „mimen“
  - Beispiele: Xen, KVM, VMware
- Fokus: **Type-1-Hypervisor**

***Anforderungen an Virtualisierung (Popek/Goldberg)***
- **Efficiency** – möglichst geringer Overhead, gute Performance
- **Resource Control (Safety)** – Isolation Guest↔Host und zwischen Guests
- **Equivalence** – gleiches Ergebnis mit und ohne VMM

***Hypervisor Type 1***
- Native
- Full-Virtualization mit Binary Translation
- Paravirtualization (OS-Assisted)
- Hardware-assisted Virtualization

***x86 Privilege Rings***
- 4 Ringe, Ring 0 am privilegiertesten
- nur höher privilegierter Code kann tiefer zugreifen
- Ring 0: Kernel/Hardware-Interaktion
- Vergleich:
  - **Bare-metal Setup**: App → OS → Hardware
  - **VM Setup**: App → **Guest OS** → **Hypervisor** → Hardware
- ![img.png](img.png)

***Full Virtualization using Binary Translation (Type I)***
- Kernel-Instruktionen werden umgeschrieben
- User-Level-Code läuft direkt
- + Gast-OS unverändert; hohe Performance
- − schwierig zu implementieren; Übersetzung kostet

***Paravirtualization (Type I)(PV)***
- Gast-Kernel nutzt Hypercalls zum kommunizieren mit Hypervisor statt direkt mit Hardware
- + weniger Overhead, einfacher zu implementieren
- − schlechtere Portabilität, Guest-OS-Modifikation nötig
- ![img_1.png](img_1.png)

***Hardware-assisted Virtualization (Type I) (HVM)***
- CPU-Erweiterungen (Intel VT-x, AMD-V)
- VMM läuft in Root-Mode
- privilegierte Instruktionen lösen Trap zum Hypervisor aus
- + schnell und heute Standard
- − IO-Virtualisierung braucht weiter Übersetzung
- ![img_2.png](img_2.png)

-------------------------------------- ab hier selber notizen gemacht

***Intel Virtualization Technology (VT-x)***
- VM control structure (VMCS) überprüft ob ein call previligiert ist 
- wenn ja, direkt zu CPU, wenn fertig, wieder direkt zu hardware

***Example: Amazon EC2***
- AMI brauchen HVM oder PV
- für CPU und memory -> HVM

***Example: KVM (Kernel Virtual Machine)***
- Einen hypervisor im Linuxkernel eingebaut
- der supported HVM und PV
- Zum KVM gibt es ein QEMU (Quick EMUlator)
- Which hypervisor type is KVM / QEMU?
  - KVM: Der Linux (Host OS) ist gleichzeitig auch Hypervisor -> Type 1 Hypervisor 
  - QEMU: ist emuliert und läuft auf hypervisor -> Type 2

***Xen***
- Xen läuft auf Hardware direkt
- Xen hat einen speziellen guest der spezielle aufgaben übernimmt
- Device Drivers sind PV, kommunizieren über bestimmte Schnittstelle

***Virtual Resources: CPU***
- CPU wird geshared durch time slicing
- Bei GPU auch space sclicing möglich
- kein mapping von virtual CPU und host CPU
- hyperthreading kann passieren
  - nicht schneller, aber einfacher zum planen
- wie viele CPU can be provison?:
  - (Threads x Cores) x Physical CPU = Number vCPU
- Ratios vCPU:CPU between 1:1-3:1 (computing intensive) to 6:1 (non computing)
- lscpu -> command zum schauene von CPU-Daten, virtualisierung etc.

***Virtual Resources: Memory***
- CPU, Cache, Memory, Disk
- je tiefer in die ebenen, umso langsamer
- am besten in CPU und dann absteigend 
- möglich wenig memory auf den guests auf unserer disk
- ![img_3.png](img_3.png)

***Virtual Memory: Ballooning***
- man manged das memory das man nicht braucht

***Virtual Memory: Overcommitment***
- nur aktiven memory ins host memory mappen
- memory von guests muss bekannt sein
- bsp.: wenn mein PC 16GB und ich habe 3 guesets, dann wären das 24GB, was nicht möglich ist
- guests requesten immer mehr memory als sie brauchen 
- in der cloud kostet virtual memory, heisst 

***Virtual Memory: Sharing***
- in der praxis nicht oft zu sehen in IaaS-umgebung
- wenn guests die ähnliche binaries haben, nur einmal im host memory laufen lassen
- ![img_4.png](img_4.png)
- ![img_5.png](img_5.png)
- wir werden ballooning implementieren

***Virtual Resources: Storage***
- disks sind blockstorage
- immer blockstorage für VM
- pribieren ausserhalb des compute clusters
  - ermöglicht bessere skalierung
- system für storage virtualiesirung
- system für ...     virtualisierung
- physisch ist network und storage nicht in gleichen network
- NIC (Network Interface Controller) → Storage Area Network (SAN) or Networked Attached Storage (NAS)
- ![img_6.png](img_6.png)

***Storage Types***
- ![img_7.png](img_7.png)

*** Thin vs Thick Provisioning***
- thick:
  - platz für guest
  - falls guest weniger bracuht, ist verschwendet platz
- thin:
  - nur so viel platz reserviere, wie guest braucht -> dynmaisch
  - wenn jeder guest ganzen platz braucht, gibt es problem

***Virtual Resources: Network***
- Network connection takes place via virtual network interface card
  (NIC):
  - keine direkte verbindung zum physischen NIC vom host
  - virtuelle switches zum trafficen von VM's zu NIC von host
  - VM-to-VM traffic stays on same host

***Fragen***
- Explain why Moore's Law is important regarding virtualization
- Describe the difference between
- Type1 and Type2 virtualization
- Hardware-assisted, Full, and Paravirtualization
- Why are the properties and requirments for virtualization also important for cloud computing?
- Which virtualization approach provides the best performance?
- Compute the number of vCPUs for a machine with 4 Quadcores and hyperthreading enabled
- What can be a problem with Balooning?
- What is thick provision? When should you use it?
- Why is generating backups with Snapshots only not a good idea?
- What is the primary advantage of using Open vSwitch (OVS) with VxLAN in a cloud environment?

