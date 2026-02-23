+++
title = "Week 04 – Netz-Lab (konzeptionell)"
date = 2025-10-09
[taxonomies]
authors = ["fatlum"]
tags = ["netsi"]
+++

## Zielbild

Ein kleines Campus-Setup mit **Router-on-a-Stick**:

- Ein **Router** verbindet mehrere **VLANs** via **Subinterfaces** (Trunk zum Switch).
- Ein **Layer-2-Switch** segmentiert in **VLAN 10/20/30/40** (z. B. Management, Clients, Guests, Server).
- Optional: **Internet-Uplink** mit NAT, **AAA/RADIUS** für zentrale Authentisierung, **ACLs** als Grundschutz.

---

## 1) Physische & serielle Verbindung

- **Physisch:** Laptop per **Console-Kabel** (Micro-USB/USB-Serial) an den Router.
- **Seriell identifizieren:** Prüfen, welches serielle Device nach dem Einstecken erscheint.
- **Konsolenzugriff:** Mit einem Terminalprogramm verbinden (Seriell, 9600 bps üblich).
- **Ziel:** Router-Prompt erreichen, um Basiskonfiguration durchzuführen.

---

## 2) Basis-Setup & Betriebsfähigkeit

- **Hostname & Domain:** Eindeutige Namen vergeben (z. B. `R1`, `lab.local`), um spätere SSH-Keys konsistent zu halten.
- **Komfort:** Konsolen-Logging synchronisieren, Timeouts sinnvoll setzen.
- **SSH aktivieren:** RSA-Schlüssel erzeugen, **SSH v2** erzwingen (remote-Administrierbarkeit).
- **Banner & Persistenz:** MOTD/Legal-Banner definieren, Konfiguration speichern.
- **Ergebnis:** Gerät ist stabil administrierbar und für weitere Schritte vorbereitet.

---

## 3) Logische Segmentierung (VLAN-Design)

- **VLANs definieren:**
  - **VLAN 10 – Management** (Switch-Mgmt, Admin-Hosts)
  - **VLAN 20 – Clients**
  - **VLAN 30 – Guests**
  - **VLAN 40 – Server** (z. B. RADIUS)
- **Adressierung (Beispiel):**
  - Je VLAN ein eigenes /24 mit Gateway .1 (z. B. 10.10.10.0/24 → GW 10.10.10.1)
- **Ziel:** Klare Trennung der Domänen für Sicherheit und Wartbarkeit.

---

## 4) Switch-Konzept

- **VLAN-Anlage:** VLANs im Switch anlegen und sinnvoll benennen.
- **Trunk zum Router:** Ein Uplink-Port als **Trunk** konfigurieren, **erlaubte VLANs** einschränken (nur 10/20/30/40).
- **Access-Ports:** Endgeräte-Ports fest einem VLAN zuweisen (**Port-basierte Mitgliedschaft**).
- **Edge-Sicherheit:** `portfast` auf Edge-Ports, BPDUGuard aktivieren, um Fehlverkabelungen zu entschärfen.
- **Ziel:** L2-Segmentierung steht; der Router kann per Trunk auf alle VLANs zugreifen.

---

## 5) Router-on-a-Stick (L3-Konzept)

- **Subinterfaces pro VLAN:** Auf dem Router für jedes VLAN ein **Subinterface** am Trunk-Port einplanen (`Gi0/0.X`).
- **Tagging:** Jedes Subinterface nutzt die **802.1Q-VLAN-ID** des entsprechenden VLANs.
- **Gateway-IPs:** Je Subinterface die `.1` des jeweiligen Netzes als **Default-Gateway** der Endgeräte vorsehen.
- **Ziel:** **Inter-VLAN-Routing** zentralisiert auf dem Router.

---

## 6) IP-Vergabe & Basis-Dienste

- **IP-Vergabe:**
  - Entweder **statisch** pro Endgerät (Management/Server)
  - oder **DHCP** pro VLAN (Clients/Guests) – z. B. DHCP-Server im Server-VLAN oder am Router.
- **DNS/NTP/Logging:** Früh definieren, wohin die Clients zeigen (z. B. öffentliche DNS oder interner Resolver, NTP-Quelle, Syslog).
- **Ziel:** Endgeräte bekommen reproduzierbar IP-Konfiguration und Zeit/DNS.

---

## 7) Uplink/Internet & NAT (optional)

- **WAN-Interface:** Ein Interface für den Internet-Uplink (statisch/DHCP).
- **NAT/PAT-Policy:** Eine **Inside→Outside**-NAT-Strategie definieren (VLANs als „inside“, WAN als „outside“).
- **Routing:** Standardroute zum Provider/Uplink; prüfen, ob Upstream-Firewall/ACLs etwas blockt.
- **Ziel:** Interne Netze erreichen das Internet kontrolliert.

---

## 8) Minimal-Sicherheitsrichtlinien (ACL-Konzept)

- **Zonales Denken:** Was darf **Clients→Server**, was **Guests→intern**, was **Mgmt→alle**?
- **Prinzipien:**
  - **Least Privilege** (nur notwendige Ports/Protokolle erlauben).
  - Gäste **von internen Netzen trennen** (nur Internet).
- **Platzierung:** ACLs **nahe an der Quelle** (ingress) oder am Gateway-Subinterface – konsistent dokumentieren.
- **Ziel:** Grundschutz ohne Komplexitäts-Overkill, spätere Feintuning-Regeln möglich.

---

## 9) Zentrale Authentisierung (AAA/RADIUS) – optional empfohlen

- **RADIUS-Server im Server-VLAN:** z. B. FreeRADIUS (ggf. mit Web-UI).
- **Geräte als NAS hinterlegen:** Switch/Router als **RADIUS-Clients** mit Shared Secret.
- **AAA-Policy:** `login`/`enable` via RADIUS, **Fallback „local“** behalten, um Lockout zu vermeiden.
- **Ausbaustufe:** 802.1X für **Port-basierte Authentisierung** in Clients-/Mgmt-VLAN.
- **Ziel:** Einheitliche Accounts, zentrale Policies, Auditing.

---

## 10) Validierung & Betrieb

- **End-to-End-Tests pro VLAN:** IP erhalten, Gateway-Ping, DNS-Lookup, Internet-Zugriff, interner Zugriff gemäß Policy.
- **Trunk-Check:** Stimmt das VLAN-Tagging? Kommen Pakete in den richtigen Subinterfaces an?
- **Sichtbarkeit:** ARP-Tabellen, MAC-Adress-Tabellen, Routing-Tabellen prüfen (Plausibilität).
- **Monitoring/Logs:** Syslog/NTP sauber, ggf. SNMP/Telemetry aktivieren.
- **Dokumentation:** IP-Plan, VLAN-Matrix, Port-Zuordnung, ACL-Policies, RADIUS-Secrets (sicher), Change-Log.

---

## 11) Troubleshooting-Denke (kurz)

- **Physik zuerst:** Link-Status, Kabel, LEDs, Interface-Up/Down.
- **L2 dann L3:** VLAN-Zugehörigkeit, Trunk-Allowed-List, MAC-Tables → danach IP/Routes/ACLs.
- **Scope eingrenzen:** Einzelner Host → VLAN → Gateway → Uplink.
- **Ein Faktor pro Test ändern:** Reproduzierbar isolieren (z. B. ACL kurz loosen, dann wieder tighten).

---

## Ergebnis

Mit diesem Vorgehen hast du:

- Eine **sauber segmentierte L2/L3-Topologie**,
- klar definierte **Gateways und Policies**,
- optional **Internet** via NAT,
- bei Bedarf **AAA** zentral,
- und einen **prüfbaren, wartbaren** Aufbau, der sich in Übungen und Praxis gleich verhält.
