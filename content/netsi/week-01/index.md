+++
title = "Week 01"
date = 2025-09-18
[taxonomies]
authors = ["fatlum"]
tags = ["netsi"]
+++

# Intro

## Ziele
- fundament für schutz von netzen
- klassische netzsicherheit wie firewalls
- moderne ansätze wie SD-WAN, zero trust etc. 
- projekte und labs nutzen um konzepte und automatisierung praxisnah zu lernen

## Vorlesungsstruktur
- 2 Teile: Klassisch und Modern
- Klassischer Teil:
  - 1 Prüfung
- Moderner Teil:
  - 1 Prüfung
- Projektarbeit mit 2 Testaten: 
  - Müssen präsentiert werden um zu bestehen und um weiter zu machen
  - Laufende Dokumentation muss gemacht werden 

## Kapitel 1
***Klassische Netzsicherheit***
***Netzzugangskontrolle***:
- sicherheit:
  - mehrere switches
  - firewall und router hersteller nicht gleich sein, weil sonst angriff durch kommen könnte
  - firewall: verschiede modi:
    - kann NAT sein, router,
    - transparent, also nicht sichtbar
  - horizontaler angriff möglich, wenn nicht kann er layer 2 angriffe machen 
  - zugriff kontrollieren
  - layer 2 abwehren
  - horizontales/lateral angriff abwehren
  - monitoring stärken
***Moderne Netzwerksecurity***
  - SD-WAN nutzen
  - Software Defined WAN
  - wird von cloud dienstleister angeboten
  - hat verrschiedene vorteile:
    - Datenverkehrt wird optimiert
    - anbieter analysiert verkehr
    - intelligen: nur wenn wirklich internes gebruacht wird, erst dann greif man auf netz von standord an
    - wenn öffentliches gesearcht wird, bsp: google, dann geht es nicht über server von ziel standord, auch wenn vpn
    - agent wird auf client installiert der alles untersucht
  - nachteil:
    - es ist immernoch eine cloud
    - diese könnte gehackt oder geleakt werden
  - cloud based ansatz ist am gewinne, für mehr einblicke was für daten von MT und weiters
- NAC = Network access control
***Netzwerksicherheit lücken***
- ungeschützer lan port
  - DNS spoofing
  - gibt sich als std. gateway aus
  - arp spoofing
- ***MAC-based NAC reicht nicht***
- mac-adressen laufen im broadcast und arp-verkehr mit und lasen sich passiv mitschneiden
- ip link set dev eth0 <MAC> klont die adresse in sekunden, ohne krypto prüfung
- aktuelle os rotieren die private mac-adresse
***NAC-Lösung***
- 802.1X switches und wlan controller agieren als authenticator am Acess-Edge
- RADIUS policy sever übernimmt auth und accounting (AAA) für ports und admin login
- identity stores AD/LDAP liefer benutzer, gruppen und geräte attribute
- Posture-/MDM-Systeme ergänzen
  Compliance-Daten und stoßen Remediation
  an
- ***lifecycle einer 802.1X-Sitzung***
  - port im unauth. state akzieptiert nur EAPOL
  - supplicant meldet sich beim Authenticator an und startet EAP aushandlung
  - authenticator kapselt 
  - Entscheidung (Accept/Reject) bestimmt VLAN-Zuordnung und ACLs

## IEEE 802.1X im Detail
- EAPOL steht für Extensible Authentication Protocol over LAN
- Rollenmodell:
  - supplicant: endgerät mit EAP-Client
  - authenticator: switchport oder wlan AP, kontrolliert link
  - authenticator server: RADIUS, entscheidet über über zugang und attribute
  - kommunikation erfolgt über EAPOL (Layer 2)
- Portzustände und Steuerung:
  - unauthorisiert: nur EAPOL erlaubt, datenverkehrt geblockt
  - autorisiert: nach erfol. authentisierung, voller datenpfad
  - reautenthifizierung: 
    - zykklisch oder
    - ereignisbaiser: geänderte credential etc. 
  - MAB (MAC authentication bypass): als fallback für geräte ohne supplicant
  - wenn client 802.1X nicht unterstützt, immernoch besser MAB einzzschalten als garnichts
- EAP-Verfahren:
  - EAP-TLS: beidseitige zertifikate
***Architektur***
  - AAA-Grundlagen:
    - Authentication: wer bist du?
    - authorization: was darf du? ableitung von zugriffen etc.
    - accounting: was hst du getan? protokollierung von sitzungbeginn
    - AAA bildet basis für nachvollziehbare und steuerbare netzwerkzugriffe
  - AAA mit RADIUS:
    - authentication, credentials prüfung via backend
    - authorization zweiung von VLAM, ACL, QoS-Profil
    - Accounting, Sitzungstart, ende, 
  - RADIUS grundprinzip
    - ist request/response modell
    - nutzdaten in AVP (attribvute value pair)
    - shared secret schützt integrität, tls-variante(RadSec) für transportverschlüsselung
    - erweiterbar durch Vendor specific attribures (VSA)
  - RADIUS-Attribute: tunnel-type 
    - tunnel-medium-type
    - tunnel-private-group-id = VLAN ID
    - filter-id = verweist auf ACL oder policy set auf switch
    - session-timeout = startet reauthorisierung nach bestimmter zeit
  - RADIUS active/standby:
    - in eine richtung synchronisieren
    - wenn nicht meldet, direkt bei server melden
  - anderer ansatz statt activr/Standby: RADIUS server auf CEF hosten
  - Policy design guidelines:
    - kategorien: nutzer, gerätetypen, standord, tageszeit
    - start mit wenig policies und kontrolliertes wachstum
    - konflikte mit prio oder bedingten ausdrückten auflösen
    - doku der entscheidungsbäume für betrieb und audit
***Implementierungsschritte Implementierungsschritte***
    - projektphase:
      1. ist analyse, geräte inventar, 
      2. pilot: wenige switches, dedizierte VLAN, begrenzte benutzergruppe
      3. Rollout: Automatisierung via Templates, Change-Management beachten.
      4. Betrieb: Monitoring, Reporting, regelmäßige Policy-Reviews.
***Wireless NAC***
- WLAN ist authenticator
- PMK (Pairwise Master Key), bleibt im controller cache 
- 4-Way-Handshake: Supplicant- und
  AP-Nonces + PMK → PTK; Schritt 3
  überträgt den Group Temporal Key (GTK).
- Schlüsselhierarchie: PMK → PTK (Unicast) /
  GTK (Broadcast) → temporäre
  Sitzungsschlüssel im Access Point.
- roaming und sicherheit
  - 802.11r/FT konfigiert schnelle BSS-Transitions
  - PMKID-Cache reduziert RADIUS-Last bei Bewegung
  - WPA3-Enterprise mit 192-bit Suite B für sensible Netze; Protected Management
    Frames (PMF) Pflicht
  - Monitoring: EAP-Timer, Failure-Reasons im WLC/RADIUS prüfen, dediziertes
    WLAN-Logging

## Härtung von Netzwerkelementen
- Defense-in-Depth: Architektur
  - schutzebene für access, distribution und core festlegen 
  - segmentierung über firewalls, VRFs und dynmaische VKAN begrenzt laterale bewegung
  - Herstellerdiversität reduziert risiko für gemeinsame schwachstellen
- Prozess:
  - sicherheitsrichtilien der geschäftsleitung definieren Freigabe, reporting eskalation
  - regelmässige penetrationstest
  - incident-playbooks und übungen stellen sicher, dass Teams schnell reagieren
- Physicher Schutz: infrastruktur:
  - zutrittskontrollen für racks und technikräume inkl. protokollierung
  - video und umgebungsüberwachung frühzeitig alarmieren
  - kabelführungen und patchfelder dokumentieren, um manipulationen zu erkennen
- Physicher Schutz: infrastruktur:
  - renduntante stromversorung und klimatisierung 
  - ersatzhardware, konsolenadapter und doku
  - out-of-band-managementwege testen und in Incident-Playbooks hinterlegen
- lokale zugänge: dienste abschalten
  - verwaltungsdienste ohne verschlüsselung deaktivieren
  - konsolen nur für break-glass-szenarien freigeben und regelmässig prüfen
  - standardbanner setzen und zugriff protokollieren
- remote zugriff: netzwerksicht
  - SSH als std. Protokoll, legacy-Ports nur temporär freischalten
  - VTY-zugänge auf management-vlans einschränken und per ACL absichern 
  - session-timeouts und login-banner setzen um complicance-anforderungen zu erfüllen
- konfigs archivieren
  - Archivierung automatisieren:
  Konfigurations-Backups nach Changes und
  zeitgesteuert anstossen.
  - Sichere Ablage per SCP/SFTP in ein
  versioniertes Repository mit
  Zugriffskontrolle
  - Integritaet und Wiederherstellung testen:
  Checksummen pruefen und regelmaessig
  Restore-Proben durchfuehren
- Logging-Architektur:
  - Syslog-Quellen mit Severity-Filtern definieren und
  an dedizierte Server senden
  - Quelle via logging source-interface setzen,
  damit ACLs greifen.
  - Zeitnah Alerts für AAA-Fehlschläge und
    Config-Changes generieren
- Telemetry & SIEM:
  - SNMP v3 mit AuthPriv und rollenbasierten Views, keine Community-Strings.
  - Streaming Telemetry/NetFlow liefert Kontext für
  Anomalie-Erkennung.
  - SIEM-Korrelation für Authentisierung,
  Config-Drift und Performance-Alarme.
- Zeit-Synchronisation
  - NTP-Server redundant betreiben und mittels ntp
    authenticate absichern.
  - Log-Server als Referenz für alle Netzwerkgeräte
    definieren.
  - Zeitabweichungen überwachen (Syslog, SNMP),
    bevor Audit-Trails ungültig werden.
- Management-Netze:
  - Management-, Logging- und Monitoring-Verkehr in dedizierte VLANs/VRFs auslagern
  - ACLs und Firewalls lassen nur erforderliche Management-Protokolle passieren
  - OOB-Netze regelmäßig testen und mit MFA absichern