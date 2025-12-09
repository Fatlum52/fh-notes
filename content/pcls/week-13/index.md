+++
title = "Week 13"
date = 2025-12-09
[taxonomies]
authors = ["fatlum"]
tags = ["pcls"]
+++

[Drehbuch: Modulübersicht PCLS – Drehbuch](https://sgi.pages.fhnw.ch/moduluebersicht/pcls/drehbuch.html)  
[Gitrepo: spd/module/pcls (GitLab)](https://gitlab.fhnw.ch/spd/module/pcls/)  
[Assessments / Assignments: Public Cloud Services – HS25](https://spd.pages.fhnw.ch/module/pcls/tutorials/assignments/public-cloud-services/hs25/index.html)  
[Report: Assessments Pages (Ordneransicht)](https://gitlab.fhnw.ch/spd/module/pcls/tutorials/assignments/-/tree/main/modules/assessments/pages/)  
[Switch Engines](https://engines.switch.ch/) · [AWS SSO](https://fhnw.awsapps.com/start/#/?tab=accounts) · [Azure Portal](https://portal.azure.com) · [O’Reilly-Playlist](https://learning.oreilly.com/playlists/a27d30d7-f139-4476-9c3a-e0abeb0f89da/)

---

# Security

## Dangers

- wenn auf cloud, dann im internet
- selbst bei private cloud gibt es einen zugriff ins internet
- im internet viele risiken

## Foundational concepts

- um secuirty etwas expliziter kümmern

## Controlplane und Dataplanesecurity

- ![alt text](image.png)
- controlplane: security auf der cloud
- dataplane: securing cloud resources
- wenn maschine komisch läuft, innerhalb von 2 min weg vom netz
- hyperscaler reagieren extrem schnell
- wir sind verantwortlich um security, keine keys auf git pushen

## Controlplane

- ![alt text](image-1.png)
- was wir auf gui sehen, wenn wir ressourccen erstellen
- hinten dran steht eine REST API
- wir von cloudprovider gemanaged

## Dataplane

- ![alt text](image-2.png)
- S3 bucket erstellen -> controlplane
- die eigentliche berechtigung im bucket gesteurt von Dataplane

## Security principles in the cloud

- ![alt text](image-3.png)
- wenn berechtigung verteilt werden, nie einen admin geben der globale admin reche hat
- fein granular zugriffsrechte geben
- immer davon ausgehen, dass etwas brechen kann
- für backups sorgen
- zero trust: jeden request authorisieren
- just in time access: zugriff nur für bestimmte zeit
- defense in depth: bestandteil der entwicklung und des betriebs
- hollistisch betrachten

## Blast Radius

- ![alt text](image-4.png)
- auf account oder cloud platform
- was für ein impact schaffen wir, wenn etwas falsch läuft?
- blast radius kann auf andere services durch kaskadieren

## Zero Trust

- ![alt text](image-5.png)
- um blast radius einzuschränken, alles authentifizieren -> zero trust
- grundidee jeder zugriff wird gecheckt mit oauth oder sonstigem
- auth provider ist single point of failure
- identitiy provider -> sind für auth zuständig

## Identities

- ![alt text](image-6.png)
- an maschinen, services anbinden
- man kann functions berechtigen andere functions aus zu führen
- tokens auf verschiedene ebenen machen

## Authentication and authorization

- ![alt text](image-7.png)
- es sollte 2 faktoren geschützt sein
- authentication: wer bist du?
- authorization: was darfst du?

## Protocols: OAuth2 and OIDC

- ![alt text](image-8.png)
- oauth2 http basierender standard
  - es passieren redirects zu den auth-servers
- OICD ist erweitung von oauth2
  - erweitert um gewisse attribute

## RBAC = Role-Based Access Control – in Azure

- ![alt text](image-9.png)
- möglichkeit feingranulat zugriffsrechte geben
- in bestimmten txtformat regeln definieren, wem ich zugriff gebe
- dieses regeln gebe ich an bestimmten rollen
- role-based regeln sind statisch
- zuordnung zu rollen...

## RBAC = Role-Based Access Control – in AWS

- ![alt text](image-10.png)
- gepinnt auf entsprechende objkete, aktionen

## RBAC-Imposter: AWS Identity Access Management (IAM)

- ![alt text](image-11.png)
- IAM konkrekter service auf aws
- es gibt immer einen IAM-user nämlich der root user
- root user schnell weg schliessen

## Components of IAM

- ![alt text](image-12.png)
- pollicies sind einzelne permissions

## IAM – Policies / Permissions

- ![alt text](image-13.png)
- besteht aus json teil

## RBAC in AWS via IAM Roles (DEMO)

- ![alt text](image-14.png)
- diagramm anschauen, bezüglich was ist denied und was nicht
- einfacher günstiger backup service -> glacier
- IAM policy simulator um zu testen ob eine policy anschlägt
- implizites deny
- kommt in klausur
- eine bestimmte policy bearbeiten und lesen können

## Consider this IAM policy, then answer the questions as they are presented

- ![alt text](image-15.png)
  - greift auf iam service zu -> action
- ![alt text](image-16.png)
  - nein
  - siehe bei action -> welche ressource
  - dann bei effect ob deny odr allow
  - das zweite ist die bedinung
  - nicht von überall terminieren, muss in ip range sein
- ![alt text](image-17.png)
  - es erlaubt nicht, wegen deny am schluss
  - es macht nichts in erster linie
  - 2- man hätte vollen EC2 access
  - 3- yes
  - tipp für klausur:
    - diese policies nehmen und in simulator rein schmeissen und experimentieren

## ABAC = Attribute-Based Access Control - in Azure

- ![alt text](image-18.png)
- heisst wir arbeiten mit labels
- labels first citizens in cloud

## ABAC = Attribute-Based Access Control - in AWS

- ![alt text](image-19.png)

## Cloud services identities

- ![alt text](image-20.png)

## Cloud agnostic identities

- ![alt text](image-21.png)
- an source code identities anhängen
- workload als auth benutzen

## Application security

## Application security – OWASP Top 10

- ![alt text](image-22.png)
- es gibt typische vulnerability

## Web Application Firewall (WAF)

- ![alt text](image-23.png)
- loadbalancer hat WAF regeln schon eingebaut

## Web Application Firewall (WAF) – Core Rule Set (CRS)

- ![alt text](image-24.png)
- kann man mit eigenen regelsets erweitern
- da wo request in LB rein kommt, dort schon abklemmen

## Frameworks

## Security and compliance frameworks

- ![alt text](image-25.png)
- ![alt text](image-26.png)

## Security and compliance frameworks – Azure Policy

- ![alt text](image-27.png)
- kann man selber implementieren
- policies haben immer einen scope
- haben regeln die umgesetzt werden dürfen
- ![alt text](image-28.png)
- ![alt text](image-29.png)

## Demo, AWS SCPs

- ![alt text](image-30.png)

## Best practices

- ![alt text](image-31.png)
- immer 2-faktor machen, IMMER!!
- IaC erleichert die Aufgabe

## Excursion

- rest nicht mehr relevant für Prüfung

## Excursion: How the cloud is used in companies

- ![alt text](image-32.png)
- ![alt text](image-33.png)
- ![alt text](image-34.png)
- ![alt text](image-35.png)
- ![alt text](image-36.png)
- ![alt text](image-37.png)
- ![alt text](image-38.png)
