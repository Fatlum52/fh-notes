+++
title = "Week 04"
date = 2025-10-09
[taxonomies]
authors = ["fatlum"]
tags = ["netsi"]
+++

## Lab

- step 1:
  - laptop mit router verbinden
  - über consolen kabel (mikro usb) mit laptop verwinden
  - terminal öffnen und unter ls - la /dev/tty.* schauen welche geräte neu hinzu kommen bei verbindung
  - mit diesme verbinden
  - danach ist man im router
- step 2:
  - terminal konfiguriert und namen gegeben
- step 3:
  - ins interface gig0/0 gehen
  - anschalten -> no shutdown
  - danach neues vlan anlegen:
    - gig0/0.10
    - description "managment VLAN 10 - Basel"
    - encapsulation dot1q
