+++
title = "Week 01"
date = 2025-09-18
[taxonomies]
authors = ["fatlum"]
tags = ["netsi"]
+++

# Intro

## Ziele
- Fundament für Schutz von Campus-, DC- und Cloud-Netzen
- Klassische Netzsicherheit: 802.1X, Firewalls, AAA, LAN-Härtung
- Moderne Ansätze: SD-WAN, SASE/SSE, Zero Trust
- Projekte und Labs → Betriebskonzepte & Automatisierung praxisnah lernen

## Vorlesungsstruktur
- 14 Termine: Mischung aus Vorlesung, Labs, Projektarbeit
- 2 Teile: Klassisch und Modern
  - Klassisch: 1 Prüfung (Woche 7)
  - Modern: 1 Prüfung (Termin TBD)
- Projektarbeit mit 2 Testaten:
  - Klassik-Testat (Woche 6), Modern-Testat (Woche 13)
  - Präsentationspflicht für Zulassung
- Laufende Dokumentation und pünktliche Abgaben Pflicht

---

# Kapitel 1

## Klassische Netzsicherheit
### Netz-Zugangskontrolle (NAC)
- Zugriff kontrollieren: nur verifizierte User/Geräte
- Layer-2-Angriffe abwehren (Rogue Devices, VLAN-Hopping, ARP/DHCP-Spoofing)
- Lateral Movement begrenzen: dynamische VLANs, ACLs, Segmentierung
- Compliance sichern (Policies für Gäste/BYOD)
- Monitoring stärken: zentrale Auth/Policy-Protokollierung

### Schwächen MAC-based NAC
- MACs im Klartext im Broadcast/ARP → leicht klonbar (`ip link set dev eth0 ...`)
- OS rotieren private MACs → Whitelists unzuverlässig
- Lösung: 802.1X mit Zertifikaten/EAP-TLS → nachweisbare Identität

### Kernkomponenten NAC
- 802.1X-fähige Switches & WLAN-Controller = Authenticator
- RADIUS-Policy-Server übernimmt AAA (Auth, AuthZ, Accounting)
- Identity Stores: AD/LDAP
- Posture-/MDM-Systeme für Compliance

### Lifecycle 802.1X
1. Port unauthorized → nur EAPOL
2. Supplicant startet EAP
3. Authenticator kapselt EAP in RADIUS → Server
4. Decision = VLAN/ACL-Zuordnung

---

## IEEE 802.1X im Detail
- Rollenmodell: Supplicant (Endgerät), Authenticator (Switch/AP), RADIUS (Server)
- Kommunikation: EAPOL (Layer 2, EtherType 0x888E)
- Portzustände: unauthorized (nur EAPOL), authorized (nach Auth)
- Reauth: zyklisch oder ereignisbasiert (Link-Down, VLAN-Wechsel)
- Fallback: MAB (MAC Authentication Bypass)

### EAP-Verfahren
- **EAP-TLS**: beidseitige Zertifikate, höchste Sicherheit
- **EAP-PEAP**: TLS-Tunnel, innen MSCHAPv2 (häufig für User)
- **EAP-TTLS**: generischer Tunnel für Legacy-Auth
- **EAP-FAST**: Cisco-Variante mit PAC

### Ablauf EAP-TLS
1. EAPOL-Start → Identity → RADIUS Request
2. RADIUS präsentiert Zertifikat, TLS-Handshake
3. Client-Zertifikat wird geprüft
4. Access-Accept mit VLAN/ACL-Attributen → Port authorized

---

## AAA & RADIUS
### Grundlagen
- **Authentication**: Wer bist du? (Credentials, Zertifikate, Tokens)
- **Authorization**: Was darfst du? (VLAN, ACL, QoS)
- **Accounting**: Was hast du getan? (Start, Ende, Volumen)

### RADIUS
- UDP (1812/1813), Request/Response, AVPs
- Shared Secret, RadSec (TLS) für Transport
- Erweiterbar durch VSA (Vendor Specific Attributes)

### Attribute-Beispiele
- Tunnel-Type / Medium-Type / VLAN-ID
- Filter-Id → ACL
- Session-Timeout → Reauth
- VSA: Cisco dACL, Aruba Rollen, MS Quarantine

### Redundanz
- mehrere RADIUS-Server (Round-Robin, Active/Standby, VIP via VRRP)
- DB-Backend redundant (MySQL/LDAP Master-Master)
- Device-Profile syncen (z.B. Git & CI/CD)

---

## Policy Design & Implementierung
- Kategorien: Nutzerrolle, Gerät, Standort, Tageszeit
- Wenige Policies starten, kontrolliert wachsen
- Konflikte → Prioritäten oder bedingte Ausdrücke
- Entscheidungsbäume dokumentieren

### Projektphasen
1. Ist-Analyse (Inventar, Identity Stores, Segmente)
2. Pilot (wenige Switches, dediziertes VLAN)
3. Rollout (Automatisierung, Change-Management)
4. Betrieb (Monitoring, Reporting, Reviews)

---

## Wireless NAC
- WLAN-Controller = Authenticator, nutzt 802.11i 4-Way-Handshake
- Schlüssel:
  - PMK (aus MSK) im Cache
  - PTK (Unicast), GTK (Broadcast)
- Roaming: PMKID-Cache, OKC, 802.11r/FT
- Gast/BYOD: Captive Portal mit RADIUS Redirect
- WPA3-Enterprise (192-bit Suite B) mit PMF Pflicht
- Monitoring: EAP-Fehler, Key-Events, Session-Timer

---

## Monitoring & Troubleshooting
- `freeradius -X` Debug
- Switch: `show authentication sessions`
- Wireshark Filter: `eapol`
- Logs → SIEM-Korrelation (Splunk, Elastic)

---

# Härtung von Netzwerkelementen
### Defense-in-Depth
- Schutzebenen für Access, Distribution, Core
- Segmentierung (FW, VRFs, VLANs)
- Herstellerdiversität reduziert gemeinsame Schwachstellen

### Prozesse
- Security-Policies der GL definieren (Freigabe, Reporting, Eskalation)
- Penetrationstests & Architektur-Reviews
- Incident-Playbooks + Übungen für schnelle Reaktion

### Physischer Schutz
- Zutrittskontrollen, Video/Umgebungsüberwachung
- Redundante Strom/Klima, Ersatzhardware, OOB-Management
- Dokumentation von Kabeln/Patchfeldern

### Lokale Zugänge
- Unsichere Dienste (HTTP, Telnet) deaktivieren
- Konsolen nur für Break-Glass
- Standardbanner + Logging

### Remote Zugriff
- SSH Standard, VTY nur im Mgmt-VLAN, ACLs
- Session-Timeouts, Login-Banner

### Rollen & Privilegien
- Privilege Levels und Parser Views (Helpdesk, Ops, Security, Architekt)
- Rolleninfos über AAA oder AVPairs

### Betriebssystem
- Signierte Images, Secure Boot
- OS-Updates mit Rollback-Plan
- Integritätschecks (SHA256)

### Konfig-Management
- Automatisierte Backups nach Changes
- SCP/SFTP ins versionierte Repo
- Checksummen & Restore-Tests

### Logging
- Syslog mit Severity-Filtern → dedizierte Server
- Source-Interface setzen
- Alerts für AAA-Fehlschläge & Config-Changes

### Telemetry & SIEM
- SNMPv3 mit AuthPriv, keine Community-Strings
- Streaming Telemetry / NetFlow
- SIEM-Korrelation (Auth, Config-Drift, Performance)

### Zeit-Sync
- Redundante NTP-Server mit Auth
- Log-Server als Referenz
- Abweichungen überwachen

### Management-Netze
- Dedizierte VLANs/VRFs für Mgmt, Logging, Monitoring
- ACLs & Firewalls nur für notwendige Protokolle
- OOB-Netze testen, MFA absichern
