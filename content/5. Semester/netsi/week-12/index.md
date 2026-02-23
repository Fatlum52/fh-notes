+++
title = "Week 12"
date = 2025-12-04
[taxonomies]
authors = ["fatlum"]
tags = ["netsi"]
+++

# K5 Kritische Schutzmassnahmen für Netzwerke

## CIA

- ![alt text](image.png)

## Defense in Depth

- ![alt text](image-1.png)

## Secure by Design

- ![alt text](image-2.png)

## Least Privilege

- ![alt text](image-3.png)

## Kerckhoffs Prinzip

- ![alt text](image-4.png)
- keinen geheimen algo entwickeln
- immer auf mathamtisch nachweisbare kryptologie bestehen

## Zero Trust

- ![alt text](image-5.png)

## KISS - Keep It Simple, Stupid

- ![alt text](image-6.png)
- fussing = random daten die man auf hardware schisst
  - dann beoachten was passiert, unvorhersehbares verhalten erzwingen

## Weitere Prinzipien

- ![alt text](image-7.png)

## Angriffsvekoren

- nmap ports anschauen
- robotx.txt => ein crawler der sagt was du darfst und nicht auf einer webseite

## Welche Informationen findet man über Unternehmen?

- ![alt text](image-8.png)

## Welche Angriffsvektoren ergeben sich daraus?

- ![alt text](image-9.png)

## Fokus auf technische Angriffsvektoren

- ![alt text](image-10.png)

## Web Application and API Protection (WAAP)

- Exponierte Systeme probieren zu fixen

## Was ist WAAP System?

- ![alt text](image-11.png)
- client/user terminieren auf waap firewall
- erster schritt um an backend server zu kommen:
  - inside out verbindung aufbaut
  - whois

## Unterschied: Firewall vs. WAAP

- ![alt text](image-12.png)

## Typische Angriffsklassen

- ![alt text](image-13.png)

## Stärken und Grenzen

- ![alt text](image-14.png)

## Moderne WAAPs im Enterprise-Umfeld

- ![alt text](image-15.png)
- gibt zwei arten L4, und L7

## Filterung von AI Crawler

- ![alt text](image-16.png)

## Besser: Inside Out Verbindungen

- ![alt text](image-17.png)

## Bedeutung von E-Mail-Sicherheit

- ![alt text](image-18.png)

## Entitäten im Mail Ökosystem

- ![alt text](image-19.png)
- MTA = GW um email zu email schreiben
- POSTFIX ist MTA implementierung
- MDA kommuniziert mit MDA

## Wichtige Schutzmechanismen (Überblick)

- ![alt text](image-20.png)

## Port Übersicht

- ![alt text](image-21.png)
- DMARC sehr wichtig beim aufsetzen der Email umgebung

## SPF, DKIM, DMARC, DANE (Identitätsprüfung)

- ![alt text](image-22.png)
- ![alt text](image-23.png)

## Wir bauen Domain-Authentication mit SPF, DKIM & DMARC

- SPF:
  - text record
  - ->all
- DKIM:
  - pubk + dkim.domain
- DMARC:
  - act + ... = R (reject), A (allow), Q (quarantäne)
- dmarcian

## Verschlüsselung

- ![alt text](image-24.png)
- ![alt text](image-25.png)

## Open Relay

- ![alt text](image-26.png)

## Open Relay Test

- ![alt text](image-27.png)

## Angriffe: DNS-Spoofing / DNS-Cache-Poisoning / Man-in-the-Middle

- ![alt text](image-28.png)
- dnssec zum dns absichern
- dns antworten kryptographisch absichern

## Lösung: DNSSEC

- ![alt text](image-29.png)

## Tool: DNSVIZ & Verisign Labs

- ![alt text](image-30.png)

## Wieso ist DNSSEC gerade für Mailing wichtig?

- ![alt text](image-31.png)

## DNS Zonentransfers

- ![alt text](image-32.png)
- für verteilung der dns server auf der ganzen welt
- dns resolver time sehr wichtig
- zonentransfer ist ein protokoll
  - mit CLI den gesamten inhalt des DNS ausgeben, um in dann irgendwo anders nach zu bilden

## DNS Tunneling

- ![alt text](image-33.png)
- dns ist intern erlaubt, aufgrund des captive portal
- txt records anfragen und abfragen kann mit dns
- encapulsieren eine tcp session und sende sie an dns server
- mit tunneling ganze session über dns nach aussen bringen

## DNS Security

- ![alt text](image-34.png)

## Vulnerability Management: Ziel & Grundidee

- ![alt text](image-35.png)

## Vulnerability Management: Prozess

- ![alt text](image-36.png)

## Bausteine eines VM-Programms

- ![alt text](image-37.png)

## Vulnerability Management – Stärken & Schwächen

- ![alt text](image-38.png)

## CNAPP – Cloud Native Application Protection Platform

- ![alt text](image-39.png)

## Bausteine einer CNAPP Plattform

- ![alt text](image-40.png)
- wissen was CNAPP ist für prüfung

## CNAPP – Stärken und Schwächen

- ![alt text](image-41.png)

## Vergleich von CNAPP & XDR

- ![alt text](image-42.png)

## Endpoint Management – Ziel & Grundidee

- ![alt text](image-43.png)

## Endpoint Management – Kernaufgaben

- ![alt text](image-44.png)
- was für funktionen sind enabled

## Clients vs. Server – Unterschiede im Endpoint Management

- ![alt text](image-45.png)

## Endpoint Management – Herausforderungen

- ![alt text](image-46.png)

## Begriffe: PAM vs. PEM

- ![alt text](image-47.png)

## PAM: Ziel & Kernfunktionen

- ![alt text](image-48.png)

## PEM: Ziel & Kernfunktionen

- ![alt text](image-49.png)

## Vergleich von PAM & PEM

- ![alt text](image-50.png)

## Kontext: Kill Chain & Deception

- ![alt text](image-51.png)

## Was ist ein Honeypot?

- ![alt text](image-52.png)

## Decoys & Deception Objects

- ![alt text](image-53.png)

## Deployment Arten

- ![alt text](image-54.png)

## Tularosa Studie (2018)

- ![alt text](image-55.png)

## Nutzen & Grenzen von Honeypots/Decoys

- ![alt text](image-56.png)

## IDS (Intrusion Detection System) & IPS (Intrusion Prevention System)

## Historischer Kontext & Grundbegriffe

- ![alt text](image-57.png)

## Network Detection & Response (NDR)

- ![alt text](image-58.png)
- sämtlichen traffci spiegelt man dahin
- ndr schauen sich timings an
- ndr kann nicht auf layer 7 schauen, nur bis layer 4

## Motivation für NDR

- ![alt text](image-59.png)
- merkwürdiges traffic erkennen
- ndr kann angeschlossen werden an SOA
- ziel von ndr, dass man früh erkennt, wenn sich jemand schon im netz ist

## Funktionsprinzip von NDR

- ![alt text](image-60.png)

## Was kann NDR erkennen?

- ![alt text](image-61.png)

## Grenzen und Herausforderungen von NDR

- ![alt text](image-62.png)
- alles ohne layer 7 inspection ist nicht gut
- ndr sind nicht günstig
- hohen integrationsaufwand
- muss sie in andere tools integrieren z.b SIEM
- in public cloud wenig anfang, also mehr eine on-prem lösung
- DLP ist schwierigistes thema
- DLP = data loss prevention
- DLP über SSE lösen
- SSE = Security Service Edge
- ohne layer 7 macht DLP keinen sinn

# EDR (Endpoint Detection & Response)

## EDR Evolution

- ![alt text](image-63.png)
- es geht auch im die response
- wenn ich festelle, dass client infiziert ist, kann man den von netz weg nehmen
  - den alert an SIEM senden
  - reactions auslösen

## EDR: Ziel & Grundidee

- ![alt text](image-64.png)

## EDR Features: Sichtbarkeit & Erkennung

- ![alt text](image-65.png)
- EDR führt sandbox nicht mehr lokal aus
  - cloud sandboxing
- sandboxing ist cpu intensiv

## EDR Features: Prävention & Hardening

- ![alt text](image-66.png)
- eher die retro, also was passiert nachdem man virus/angriff erkannt hat

## EDR Stärken, Grenzen & Einordnung

- ![alt text](image-67.png)
- EDR eher auf std. client und server ausgelegt
- EDR sieht was client und rechner machen -> Datenschutz

## EDR Erweiterung & Ausblick

- ![alt text](image-68.png)
- x steht für universall
- proxy und handy mit einbinden

## Vergleich NDR und EDR

- ![alt text](image-69.png)

# SIEM (Security Information and Event Management)

## SIEM: Ziel & Grundidee

- ![alt text](image-70.png)
- was für muster von angriffen man in den logs erkennt
- logs korrelieren, nennt man das
- logs normalisieren, zum am SIEM erklären, was da steht
- SIEM zentralisiert alle logs
- korrelationen werden AI unterstützt
- SOC = Security Operations Center
- SOC auf basis von SIEM machen

## SIEM: Datenquellen & Architektur

- ![alt text](image-71.png)
- alles im unternehmen
- alles was L7 inspizieren kann ist wertvoll

## SIEM Use-Cases

- ![alt text](image-72.png)

## SIEM: Stärken & Grenzen

- ![alt text](image-73.png)
- ist ein enterprise produkt
- SIEM konfiguriert man selber
- security analysten arbeiten mit SIEM
- verbraucht ressourcen -> CPU, Memory, GPU, Storage
- SIEM verarbeitet daten, erstellt dann einen neuen
- SIEM ist kern element von SOC

## SIEM im Zusammenspiel mit EDR, XDR & SOC

- ![alt text](image-74.png)

# SOAR - Security Orchestration, Automation & Response

## SOAR – Security Orchestration, Automation & Response

- ![alt text](image-75.png)
- aus gefilterten, bearbeiteten SIEM alerts dann mach SOAR
- also nutze ein SOAR-tool und spiele playbook xy aus
- in SOAR-tool wird ein alert von SIEM kategorigisiert
- anhand von kategorie, wird ein gewisses playbook ausgeführt

## Bausteine eines SOAR-Systems

- ![alt text](image-76.png)
- runbook in low-code definieren

## Beispiel: Phishing-Fall mit mehreren Systemen

- ![alt text](image-77.png)

## SOAR: Zusammenspiel mit SIEM, EDR, NDR & SOC

- ![alt text](image-78.png)

## Stärken und Schwächen von SOAR

- ![alt text](image-79.png)

# SOC (Security Operations Center)

## SOC: Ziel & Grundidee

- ![alt text](image-80.png)
- SOC ist eher prozessural ausgelegt

## Aufgaben eines SOC

- ![alt text](image-81.png)

## SOC: Rollen & Aufbau

- ![alt text](image-82.png)

## SOC: Betriebsmodelle

- ![alt text](image-83.png)

# Adversarial Exposure Validation (AEV)

## Worum geht es bei AEV?

- ![alt text](image-84.png)
- SASE lösung forwarded logs an SIEM
- da geht es darum, sein unternehmen kontinuierlich anzugreifen um zu schauen ob sicherheitskonzept standhält

## Wie funktioniert AEV?

- ![alt text](image-85.png)

## Stärken & Schwächen von AEV

- ![alt text](image-86.png)

## AEV im Kontext

- ![alt text](image-87.png)

## Exposure Validation vs Red-Teaming

- ![alt text](image-88.png)
- Red Team (Der Angriff)
- Blue Team (Die Verteidigung)

# Passwort Manager

## Enterprise Passwort-Manager: Features

- ![alt text](image-89.png)

# Backup

## Grundidee und KPIs (Key Performance Indicator)

- ![alt text](image-90.png)
- backups unbedingt testen, ob man sie auch recovern kann

## Klassische Backup-Konzepte

- ![alt text](image-91.png)

## Backup-Architekturen

- ![alt text](image-92.png)

## Moderne Backup- und Data-Protection-Plattformen

- ![alt text](image-93.png)
- unternehmensdaten liegen überall im intern verstreut
- forensiker finden die eigentliche malware mit SIEM
- wenn man datei findet, die für malware zuständig ist, kann man diese datei hashen, dann beim backup, alles backupen ausser die datei mit diesem hash
- backuplösungen sind so granular, man kann alles weiderherstellen bis auf die einte datenbank oder sogar ohne den einten eintrag in der datenbank
- DLP: grösser faktor, ist die menschliche klassifizierung
- backups sollen immutable sein
  - es gibt policies drauf, die geairtagged sind
- backups haben mit AI eine anomalie erkennung

## Backup Angriffe und Schutzkonzepte

- ![alt text](image-94.png)

# IaC (Infrastructure as Code)

## Infrastructure as Code – Konzept und Definition

- ![alt text](image-95.png)

## Vorteile und Nachteile von IaC

- ![alt text](image-96.png)

# Identity Protection

## Digitale Identität im Netzwerk

- ![alt text](image-97.png)

## Bedrohungen für digitale Identitäten

- ![alt text](image-98.png)

## Identity Protection: Schutz Mechanismen

- ![alt text](image-99.png)
- IDP sehen alles, also vorallem diese schützen
- Intrusion Detection & Prevention (IDP)

## Exkursion: Identity Proxy

- ![alt text](image-100.png)
- nicht nur die actions allow oder block?
- über einen identity proxy
- ![alt text](image-101.png)
- ![alt text](image-102.png)
- SSE lösung übernimmt IDP-lösung
- ermöglich BYOD für SaaS

# Strategie

## Infrastruktur smart vernetzen statt Feature-Zoo

- ![alt text](image-103.png)
- wichtig zu verstehen, was sind die konzepte und das es dich gibt
