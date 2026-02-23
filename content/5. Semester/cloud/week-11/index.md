+++
title = "Week 11"
date = 2025-11-28
[taxonomies]
authors = ["fatlum"]
tags = ["cloud"]
+++

[Drehbuch](https://sgi.pages.fhnw.ch/moduluebersicht/cloud/drehbuch.html)  
[Aufgaben](https://spd.pages.fhnw.ch/module/cloud/platforms_site_generated/cloud-reports/hs25/index.html)

---

# K11

## info

- ![alt text](image.png)

## Why do we need Storage?

- ![alt text](image-3.png)
- Storage ist mit steigender bandbreite wichtiger

## Why Storage matters?

- ![alt text](image-1.png)
- IOPS wichtiger als bandbreite
- daten sind in der regel in nebeneinander liegende blöcken, deshalb bandbreite ok
- ![alt text](image-2.png)
- blocks sind dumm, keine infos, usermgmt, es stehen nur bits drin
- auf basis von blocks, baut man file systems
- displaying storage sind mit der cloud gekommen

## What is Storage?

- ![alt text](image-4.png)

## What is a Blockstorage?

- ![alt text](image-5.png)
- ist unterste ebene in disk storage

## Accessing Block Storage, iSCSI

- ![alt text](image-6.png)
- ![alt text](image-7.png)

## What is a Filestorage?

- ![alt text](image-8.png)
- dateien sind konsumierbar
- ![alt text](image-9.png)
- bei cgroups für systeme haben wir das filesystem verändert
- ![alt text](image-10.png)

## What is a Object Store?

- ![alt text](image-11.png)
- ist ein block, ohne referenz mit variabler länge
- mit http darauf zu greifen (get, post)
- ![alt text](image-12.png)
- ![alt text](image-13.png)
- für dateipattern wo man die dateien oft mutiert nicht so geeignet

## SAN, DAS, NAS

- ![alt text](image-14.png)
- SAN sieht man in rechenzentren
  - sind sehr teuer

## Example: Classical SAN

- ![alt text](image-15.png)
- haben keine logik
- sehr effizient, sehr teuer

## Mapping to storage kind

- ![alt text](image-16.png)

## Software defined Storage to the rescue

- ![alt text](image-17.png)
- storage virtualisieren
- storage als service definieren

## SDS-Example in practice: Ceph

- ![alt text](image-18.png)
- standard produkt wenn es um storage defined network geht

## Concrete Example of SDS, CEPH

- ![alt text](image-19.png)
- CEPH macht aus daten ein object

## OSDs

- ![alt text](image-20.png)

## Mapping Data to OSDs

- ![alt text](image-21.png)
- cluster map speichert welche information wo abgelegt ist

## CRUSH-Algorithm

- ![alt text](image-22.png)

## Modifying Disks

- ![alt text](image-23.png)

## CSI and K8s

- ![alt text](image-24.png)

## Ceph and K8s → Rook

- ![alt text](image-25.png)
- lokale disks der workernode werden als OSD's exportiert

## Summary

- ![alt text](image-26.png)

## Nächste plattform

- CEPH cluster bauen
- 10GB partition machen, sonst reicht es nicht
- 40BG disks machen und extern dran hängen (root)
- 1 monitor, 4 osd's
-
