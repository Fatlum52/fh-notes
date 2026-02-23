+++
title = "Week 12"
date = 2025-12-02
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

# Network

## Cloud Connectivity

- ![alt text](image.png)
- kann eigenes zertifikat hinterlegen

## Cloud Connectivity – Challenges

- ![alt text](image-1.png)
- normale verbindungen können auch herasufordernd sein
- man kann encryption aufschalten

## Case Study: What is the latency of cloud access?

-

## Case Study: How much latency is there when accessing cloud infrastructures in

- ![alt text](image-2.png)
- umso weiter der punkt umso höher die latenz
- physik limitiert uns
- durch viel zahl an regionen, sollte man die region wählen, die am nächsten zum user ist

## Private networks in the cloud

## Networking in the Cloud: Virtual Networks & Subnets

- ![alt text](image-3.png)
- infra ist multi tenant ausgeelgt
- können einzelne logische netzwerke anlegen

## Virtual Networks & Subnets – Azure VNETs

- ![alt text](image-4.png)
- service der an region gebunden ist
- subnetze zum innerhalb von einer region ein netzwerk aufzubauen
- cloud aufpassen vor IP-kalkulation

## Virtual Networks & Subnets – AWS VPCs

- ![alt text](image-5.png)
- subnetze funktionieren bei aws anders
- ein subnetz ist availability zone spezifisch
- in aws gibt es ein default VPC
- auch hier werden gewissse ip's reserviert

## The need for network peerings

- ![alt text](image-6.png)
- eine menge von vpc sind erstmal logisch voneinander getrennt
- um kommunikation möglich zu machen, ohne selbes VPC kann man network peering verwenden
- provider spezifische lösung
- VPC's die man verbinden will, müssen unterschiendliche ranges haben
  - nicht überlappen
  - peering sind nicht umsonst, sobald traffic drüber läuft

## Network peerings (2)

- ![alt text](image-7.png)
- hub spoke umsetzen
- cloud mit on prem umgebung verschemelzen, nur einmal machen mit hub and spoke
- grosse autonomität für die teams
- peering geht nur innerhalb eines herstellers
  - vnet mit vnet oder vpc mit vpc

## Connect to private networks in the cloud

## Virtual Private Network – VPN

- ![alt text](image-8.png)
- on prem mit cloud verbinden durch VPN
- auf privaten ips unterwegs und verschlüsselung vorhanden

## Virtual Private Network – VPN – Azure VPN Gateway

- ![alt text](image-9.png)
- ein services deployen: vpn gateway
- site to site oder point to site verbindung
- es gibt static und dynamic routing
- über vpn gateway um zu on prem zu gelangen
- vpn gw sagen, dass er die netze kennt
- BGP dynmaisches protokoll das ermöglicht verbindung
- vpn gw geht über internet
  - frisst bandbreite
  - umso mehr bandbreite, umso grösseren gw muss man mieten

## Virtual Private Network – VPN – AWS Virtual Private Gateway

- ![alt text](image-10.png)
- gw an vpc anhängen
- vpn mit ipsec ist standard
- aws kennt auch andere optionen: transit gw
- man braucht dedicated routes

## VPN vs. dedicated connections

- ![alt text](image-11.png)
- immer einfachste und schnellste option
- dedizierte leitung muss man mieten, aufsetzen, einstellen
  - man kann aber garantierte ressourcen bekommen

## Azure Express Route

- ![alt text](image-12.png)
- on prem mit cloud verbinden
- diessmal über express route
- es muss eine leitung gezogen werden
- so hat man sichere dedizierte leitung mit garantierten durchsatz

## AWS Direct Connect

- ![alt text](image-13.png)
- bei aws heisst das ganze aws direct connect
- man kann aws produkte so routen
- dynmaisch erkennbar wo hin es muss
- wenn keine physkialische leitung vorhanden ist, kann man nicht verbinden
- diese direct connections sind vorallem für netzwerk konnektivität vorhanden
- endgerät identifizieren gehen sie nicht so weit, noch nicht

## Management of outbound traffic

- oberhalb war on prem zu cloud oder cloud zu on prem

## Gateways, NAT Gateway

- ![alt text](image-14.png)
- wenn vm public ip hat, kann sie direkt ins internet
- gibt es die nicht, braucht man einen gw
- viele verschiedene optionen, diese im griff behalten

## Gateways, NAT Gateway – Azure

- ![alt text](image-15.png)
- bei azure wenn man nichts tut und eine vm provisioniert, funktioniert das direkt, ins internet surfen
- auch wenn sie eine private hat, wird diese automatisch vom gw in public ip translated
- option um das einzuschränken:
  - mit load balancer, das er quasi alles translated und vm nicht direkt translated wird
  - mit NAT GW
  - filtern bei beiden optionen nicht möglich
- ![alt text](image-16.png)
- weitere möglichkeit über virtual appliance/firewall zu gehen

## Gateways, NAT Gateway – AWS

- ![alt text](image-17.png)
- hier kann man nicht direkt ins internet, wie bei azure
- um ins internet zu gehen, muss man ein vpc machen
- dem vpc sagen wir, wenn er 0.0.0.0 gehe will, soll er über router gehen

## Gateways, NAT Gateway – Egress Traffic Filtering

- ![alt text](image-18.png)
- zum daten nach aussen oder innen zu kontrollieren geht das mit NAT nicht (halbwegs)

## Gateways, NAT Gateway – Azure Firewall

- ![alt text](image-19.png)
- azure firwall ist ein service
- er bekommt public und private ip
- man konfigutiert, dass jeder traffic nach aussen über die firewall gehen
- firewall sitzt zwischen quelle und ziel
- kann auch pacet inspection machen
- clients müssen nicht selber proxy haben, sondern durch routing definiert man es muss über die firewall gehen

## Gateways, NAT Gateway – AWS Network Firewall

- ![alt text](image-20.png)
- selbes prinzip nur für aws
- mit policies kann man routing einstellen
- klassisches netzwerk mittel um egress traffic zu kontrollieren

## DNS in the cloud

## Recap: What is DNS?

- ![alt text](image-21.png)
- wir wollen für ip's namen haben
- damit es transportabel stabil bleibt

## Recap: What is DNS? - Hierarchy

- ![alt text](image-22.png)
- root, top level domain, second level domain, third level domain
- zone operator kümmern sich um die oberste ebene
- dns arbeitet unter port 53
- dns ist meistens recht offen
- dns funktioniert über records

## Recap: What is DNS? - Common RRs (Resource Records)

- ![alt text](image-23.png)
- ARecord: ich mappe domäne zu ip
- cname: von domäne auf eine andere domäne referenzieren
- text records: von einer domäne bekomme ich plain text
- mx: domain zeigt auf email service
- zone delegation: zone operator muss auf einen anderen dns server zeigen

## DNS in the cloud'

- ![alt text](image-24.png)
- public dns:
  - bin im public wifi, dann verwende ich public dns
- private dns:
  - löse namen im privaten netzwerk dns auf
- split dns:
  - namen können private oder öffentlich aufgelöst werden

## DNS in cloud networks

- ![alt text](image-25.png)
- wenn man bei azure nichts deifniert wird public dns verwenden
- von haus aus ist dns gemanaged
- man kann aber selber dns konfigurieren
  - wir haben einen service, diesen können wir anschliessen an vnet

## Private network integration of cloud services

## Network integration for cloud services

- ![alt text](image-26.png)
- drei verschiedene optionen
- verschiedene konzepte für in und outbund traffic
- client selber sein oder dein service (function) bezieht selber etwas
- ai foundry wird immer ein service sein, llm wird nie änderungen an meinen services machen

## Network integration for cloud services – public IPs and DNS

![alt text](image-27.png)

## Network integration for cloud services – public IPs and DNS with backbone

- ![alt text](image-28.png)
- alles was aus internet kommt, kann nicht an meine services
- nur client aus eigenem netz haben zugriff

## Network integration for cloud services – private IPs and DNS

- ![alt text](image-29.png)
- dns zone muss an vnet hängen
- alle drei optionen sind für inbound traffic, also von aussen zu unseren chatbots

## Network integration for cloud services – Cloud service to VPC/VNET

- ![alt text](image-30.png)
- vnet integration heisst das konzept
- ich gebe eine range an, wer darf auf db zugreifen oder nicht
- in aws heisst das private link
- man gibt an, welche ip (private) andere servics innerhalb des selben vnet ansprechen darf
- verbindung function app zu vnet

## Network segmentation

## Networksegmentation

- ![alt text](image-31.png)
- ein netzwerk trennt man, segmentieren
- user in einer zone, dmz in einer, und so weiter
- innerhalb einer zone freie kommunikation

## Microsegmentation

- ![alt text](image-32.png)
- eine zone hat einen grosses spreng radius
- ein loch im uboot, ganzes boot gehr runter
- mit mikro segmentierung, passiert das nicht
- ![alt text](image-33.png)
- links ist infra view
- innerhalb einer app ist rechts

## Microsegmentation, how? Microsegmentation, why?

- ![alt text](image-34.png)
- um app mikro zu segmentieren, muss man sehr fein granular einstellen können
- how?
  - drei verschiedene optionen um mikrosegmentierung vorzunehmen
  - wenn man netzwerk lösung hat, diese kennt aber zum beispiel kubernetes, dann gibt es probleme
  - immer aufpassen, auf welchem stack man ist
- why?
  - kleine angriffsfläche bieten
  - wenn ein container/vm/service kompromitiert ist, soll es nicht zu anderen springen können

## Networksegmentation'

- ![alt text](image-35.png)
- jeder vm und jedem netz eine firewall geben
- team welche die anwendung betreut, weiss welcher service spricht mit wem
- funktiioniert nur mit IaC
  - weil so ist alles einheitlich und man sieht wer mit wem kommuniziert

## Networksegmentation in Azure

- ![alt text](image-36.png)
- NSG = network secuirty group = firewall wo man an vm attachen kann
- auf subnetz ein nsg selber drauf tun
- nsg kosten nichts
- nsg arbeitet auf ip ebene
- ASG = application security groups
- kann verschiedenen vm's verschiedene asg geben
- asg kategorien zum beispiel (web, db, etc.) kann man selber definieren
- definieren mit labels und annotations
- asg funktionieren nur auf vm's
- nsg kann man immer deployen, auf alles

## Networksegmentation in AWS

- ![alt text](image-37.png)
- bei aws nennt man das ACL
- zusätzlich kann man jeder instanz eine security groups hinzufügen

## Network pricing

- ![alt text](image-38.png)
- inbound kostenlos oder günstig
- outbund ist immer teurer
- von public zu einer vm ist gratis/günstig
- kommunikation zwischen kontinete ist teurer

## Networking - Summary

- ![alt text](image-39.png)

## Load balancing motivation

- ![alt text](image-40.png)
- systeme die man hat gut auslasten und keinen bottleneck erzeugen

## Load balancing concepts

- ![alt text](image-41.png)
- statisch:
  - round robin
    - stumpf und dumm
  - ip hash
- dynamisch:
  - least connection
    - man muss awarness haben
    - wer weniger zu tun hat, bekommt traffic
  - least response time
  - least bandwidth
- es gibt keinen holy grail
- es kommt auf den use case drauf an

## Load balancing – dynamic algorithms

- ![alt text](image-42.png)
- man kann gewichten und berechnet dann wer antwort liefern soll

## Load balancing – static algorithms

- ![alt text](image-43.png)

## Load balancing L3/4 vs L7

- ![alt text](image-44.png)
- auf layer 4 haben rein tcp udp traffic
- ![alt text](image-45.png)
- auf layer 7 sehen wir auch auf welche domain geht
- können so mehr granulieren, kontrollieren
- unterschied:
  - layer 7 LB ist ein reverse proxy
  - verbindung terminiert, und macht eine neue eigene verbindung L7
  - tls termination möglich bei L7 LB

## Load balancing services

## AWS load balancing

- ![alt text](image-46.png)
- application load balancer = L7 balancer bei aws
- aws hat classic varianten

## Azure load balancing

- ![alt text](image-47.png)
- application gateway ist regional
- globale load balancer für globale firmen
- front door machen wenn kunden in verschiedene kontinente sitzen
- traffic manager ist dns basiertes balancing
- front door läuft überall auf der welt und halt verschiedene eintrittspunkte in microsoft auf der ganzen welt
- dns anfragen können gecachet werden
- ![alt text](image-48.png)
- auswahl treffen gemäss obiges diagramm

## Load balancing use cases

## Load balancing – private und public use cases

- ![alt text](image-49.png)
- im private fall ist balancer nur über private netz erreichbar
- wenn ich lb provisionier, kann man sagen ob er eine private oder public ip bekommen soll
- intern layer 7 lb verwenden geht

## Load balancing – Global vs Regional

- ![alt text](image-50.png)
- traffic manager ist global
- wenn man domain auftruft, entscheidet traffic manager welche route nehmen
- cross region lb => traffic manager
- ![alt text](image-51.png)
- SKU = stock keeping units

## Load balancing additional features

## Load balancing

- ![alt text](image-52.png)
- wenn wir in l7 lb sind, können in traffic rein sehen
- lb kann static assests cachen und arbeitet so schneller

## Load balancing pricing

- ![alt text](image-53.png)
- je mehr rules ein lb hat, umso mehr zahlen wir

## Load Balancing – Summary

- ![alt text](image-54.png)
- wenn wir traffic aware sein wollen brauchen wir L7 LB
