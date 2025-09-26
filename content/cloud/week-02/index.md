+++
title = "Week 02"
date = 2025-09-26
[taxonomies]
authors = ["fatlum"]
tags = ["cloud"]
+++

Drehbuch: https://sgi.pages.fhnw.ch/moduluebersicht/cloud/drehbuch.html  
aufgaben: https://spd.pages.fhnw.ch/module/cloud/platforms_site_generated/cloud-reports/hs25/index.html  

Abgabe erstes projekt: 09.10.2025
---
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
- genau anschauen, da wir es verwenden

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

## Form Virtualization to IaaS Platforms

***NIST Definition of Cloud Computing***
- Diese Cloud model hat 5 essezielle charakterisitken:
  - on-demand-self-service: Resources are provisioned automatically without human interaction
  - Broad network access: The cloud must be accessible via network
  - Resource pooling: Resources are shared among multiple customers → Virtualization
  - Rapid elasticity: Existing resource can be adapted to shrink and to increase dynamically
  - Measured service: All usage of the cloud is metered in a transparent matter to enable pay-as-you-go

***Example: OpenStack***
- eine virtuallisierungsplattform
- switchEngines baisert es auf openStack
- orchestrator muss selfService und API endpoints anbieten
- ein metric und billing system -> misst wie viel ressourcen wir gebraucht haben und stellt dies in rechnung
- ein selfservice portal -> ein gui um unsere instanzen zu erstellen
- bei kommerziellen lösungen gibt es einen enterprise tools integration -> für firmen zusätlziche tools wie secuirty und weiters
- ceilometer: monitorining system bei openStack
- nova: virtualiserung und compute
- neutron: für network
- cinder: für storage

***Example: OpenStack Architecure***
- controller node: managed alle services
- computer node: manged network agents und machines
- network node: komponenten wie DHCP
- Storage Node: Block and Object Storage

***Example: VMware vSphere / ESXi***
- sehr komplex, gängiger abieter
- VIM: manager der mehrere instanzen orchestriert
- ein cluster kann enorm gross werden, bis zu 40000 virtuelle maschinen 
- closed source produkt -> schwer für insights

***VIM (Virtual Infrastructure Manager)***
- was ist unterschied zwischen VIM und VMM -> Prüfungsfrage, unbedingt drin lassen
- managed templates die verwendet werden um eine prebuilt instanz 
- allocating und releasing virtuelle ressourcen
- ressourcen koordinieren wie replication, load balancer, failover system
- usage und security policies forced über einen lifecycle
- monitoring von physischen/virtuelle ressourcen
- failover system:
  - wenn etwas schiefgeht, wird eine node zur anderen übertragen, live
  - wärend sie läuft wird migriert

***Failover System***
- active-passive:
  - eine andere utilisation kleiner als 50%, die hälfte steht fast immer leer
- active-active:
  - heut meist alle so
  - mit tradeoff dass nicht alles überall verfügbar ist

***Example: Proxmox VE***
- eine plattform um virtuelle maschinen zum laufen
- basiert auf debian linux
- über webUI oder CLI zum managen
- ![img_8.png](img_8.png)

***Example: Proxmox VE Cluster Architecture***
- ![img_9.png](img_9.png)
- über webUI oder API kann man auf jede node zugreifen
- VM laufen auf QEMU

***Example: Proxmox VE Cluster Manager***
- pvecm (cluster manager)
- alle kommunikation läuft über pmxcfs file system
```shell
ls /etc/pve/nodes
```
- führt zur überischt alles nodes

```shell
ls /etc/pve/nodes/node01/qemu-server/101.conf
```
- alle infos über die vm die in diesem node läuft

```shell
ls /etc/pve/nodes/node01/qemu-server
```
- zeigt alle vm's die auf diesem node laufen

- proxmoxUI auf port 8086 verfügbar
- starkes pw für den root user -> sehr gefährlich
- auf guest eingeloggt, die auf diesem host läuft
- kann eine node in die andere migrieren über UI
- über UI auf proxmox proxy, diese wiederum kommunizierne über filesystem
- auf gitlab gibt es ein tutorial -> sehr aufmerksam durchlesen 

