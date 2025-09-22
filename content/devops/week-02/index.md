+++
title = "Week 02"
date = 2025-09-22
[taxonomies]
authors = ["fatlum"]
tags = ["devops"]
+++

# Frontalunterricht
- convention over configuration

- problem mit folgender architektur:
- ![img.png](img.png)
- problem: 
  - keine resilizen zwischen modulen
  - nicht verfügbar und skalierbar
  - einzelne services in den modules kann man nicht verändern, man muss alles grösser machen
  - wenn ich ein neues feature hinzufügen will, z.b. in catalog, dann muss ich API und database ändern
  - sehr starke abhängigkeiten zwischen den micro services 'modules'
  - änderungen schlagen stark auf die database
- conways law:
  - überall zu sehen
  - eine organisation ist aufgeteilt in strukturen, diese strukturen finden sich in der architecture wieder
  - frontend-team für frontend, backend-team für backend ...
- Lösung:
  - teams nach produkt ausrichten, bedeutet: team 'ordering' macht alles was es dazu braucht, hat diesbezüglich auch eigene database
  - team soll end-to-end selbst verantworten
- 12factor Grundidee:
  - 12factor-App ist eine Methologie
- codebase:
  - sprich alles in Version control (git), alles was wichtig ist, sprich configs, sourcecode, icons, stylesheet etc.
  - nicht in git: alles was generiert wird, node_modules, generated docs, generated testdata
  - monorepo vs polyrepo:
    - monorepo:
      - ganzes service architektur in ein repo
      - nachteil: repo wird riesengross
    - polyrepo:
      - jeder service, eigenes repo
      - dann arbeitet man mit dependencies
- convetional commits;
  - immer ein prefix
  - zum versionieren und filtern etc
  - bsp:
        <type>optional scope: <description>
        optional body
        optional footer(s)
- gitlab-handling:
  - reviews:
    - merge requests, pull requests
    - template for issues, reference to git
  - builds:
    - can be brach/tag aware
    - kann branches brauchen
  - force:
    - für rebase muss man forcen
    - um flasche daten raus zu nehmen, brauch es einen force
- branching:
  - ein branch bei git ist ein label von einem commit
  - nicht zu viele branches machen
  - strategien:
    - trink based: immer auf dem mainstream
    - gitflow branching: mit verschiedenen branches, dann in main pushen
  - releasing:
    - semVer:
      - bedeutet, meine software ist ausgebraucht
      - major: API cghanges
      - minor: zusätzliche funktionalität
      - patch: bug fixes
    - calVer:
      - YYYY.MM.DD: Full date (e.g., 2021.03.22) indicating the exact release day
      - YYYY.MM: Year and month (e.g., 2021.03) for monthly releases
  - was ist ein release:
    - maven:
      - identifiziert bei fixen versionen
      - alle releases sind stable
      - für CD brauche -"SNAPSHOT"-suffix
    - Docker /OCI:
      - identifiziert mit tags, hash
      - unqiue mit NAME:TAG@HASH
      - name:tag kann überschrieben werden
      - keine gefahr trasitive dependecies kapput zu machen, images sind self-contained
      - für CD: use latest