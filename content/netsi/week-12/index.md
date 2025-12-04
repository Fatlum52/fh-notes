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
- 

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

##
