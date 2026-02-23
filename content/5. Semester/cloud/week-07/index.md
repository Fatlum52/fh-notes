+++
title = "Week 07"
date = 2025-10-31
[taxonomies]
authors = ["fatlum"]
tags = ["cloud"]
+++

[Drehbuch](https://sgi.pages.fhnw.ch/moduluebersicht/cloud/drehbuch.html)  
[Aufgaben](https://spd.pages.fhnw.ch/module/cloud/platforms_site_generated/cloud-reports/hs25/index.html)

Abgabe zweites Projekt: **30.10.2025**

---

# K7 Large Scale Container Orchestration (Kubernetes)

## What is Container Orchestration?

- ![image.png](image.png)
- ressourcen die wir haben optimal nutzen
- scale-in von clustern kommt es zum zug

## What is Kubernetes?

- ![image-1.png](image-1.png)
- opensource system für autoamtisches deployment, scale und management
- internes projekt das veröffentlich wurde von google
- sie haben es veröffnetlich, weil andere auch am entwickeln waren und damit man besser mit anderen firmen zu arbeiten kann

## Kubernetes Distributions

- ![image-2.png](image-2.png)
- verschiedene kubernetes anbieter/unterstützer

## Cloud Native Computing Foundation (CNCF)

- ![image-3.png](image-3.png)
- auf dieser seite sieht man zertifizierte kubernetes distributionen
- das ecosystem drum herum, die kubernetes tool sind

## Kubernetes Objects: Record of intent

- ![image-4.png](image-4.png)
- statt container laufen lassen, ebschreiben wie er laufen soll, wo und wie er aussieht
- deklarativ, wie soll container laufen, wo etc.

## Kubernetes Objects: Pod

- ![image-5.png](image-5.png)
- kleinste einheit die eman erstellen kann ist ein pod
- pod ist zusammenschluss von einem oder mehreren containern
- in der regel ein pod ein container

## Kubernetes Objects

- ![image-6.png](image-6.png)

## Persistent Storage for Kubernetes Objects: etcd

- ![image-7.png](image-7.png)
- das herzstück von kubernetes
- etcd muss man selber encrypten bevor man etwas darin speichert

## Kubernetes Cluster Architecture

- ![image-9.png](image-9.png)
- später brauchen wir einen controller
- keine gute idee direkt mit etcd arbeiten, sprich ich kann dort schreiben was ich will, egal ob korrekt oder nicht
- ![image-11.png](image-11.png)

## Kubernetes API Server

- ![image-8.png](image-8.png)
- kubectl ist ein tool
- kubectl schaut, dass alles korrekt ist
- der kube api server schreibt dann in ectd
- kubectl kommuniziert mit dem kubeapiserver
- und dann läuft alles über kubeapiserver
- kubectl create pod -> einen pod kreieren
- kubectl apply -f pod.yml -> erstellt einen pod
  - dieser wurde dann am ende des tages in etcd geschrieben

## Kubernetes Worker Node

- ![image-10.png](image-10.png)
- container in den pods sollen auf nodes laufen
- in kubelet-config steht der runtime-endpoint
- kubelet, kubeproxy und containerd laufen auf einem node
- kubelet um container zu starten innerhalb eines nodes
- änderungen am pod.yml dann über kubectl apply ändern
- k9s für ein tui (terminal user interface, ein gui für terminal)
- kubernetes the hardway -> tutorial auf github
- kubeproxy ersetzen mit Cilium ein produkt von eBPF

## Kubernetes Scheduler

- ![image-12.png](image-12.png)
- statt pod an node von hand zuweisen, benutze ich scheduler

## Kubernetes Controllers

- ![image-13.png](image-13.png)
- node controller der sagt wie geht es den verschiedene nodes

## Kubernetes Controller Pattern

- ![image-14.png](image-14.png)
- alle controller arbeiten nach diesem prinzip

## Workload Objects

- ![image-15.png](image-15.png)
- mit replica-set kann man mehrere pods erstellen
- wenn ich pod update will, gibt es deployment controller der nach und nach pods update
- daemon-set controller kann sagen, sagen welche pods auf welchen nodes ein sollen, unbedingt oder was auch immer
  - vorallem bei infra sachen
- alle blauen boxen sind kubernetes objecte
- pods sind immutable

## Workload Objects: Deployment

- ![image-16.png](image-16.png)
- desired state = record of intend

## Ganze Kubernetes Architekur

- ![image-17.png](image-17.png)
- mehr ist kubernetes nicht
- alle features die dazu kommen, kommen dank diesem controller pattern
- 1 node kann bis zu 250 pods haben und somit container

## Summarizing Questions

- ![image-18.png](image-18.png)
-
