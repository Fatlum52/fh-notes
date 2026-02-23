+++
title = "Week 03"
date = 2025-09-29
[taxonomies]
authors = ["fatlum"]
tags = ["webcl"]
+++

### Punkte
6

## Fragen
- week03/presentationModel/presentationModel.js, zeile: 20
  - wieso übergibt man einfach nicht null?
---

## CSS

- man kann custom propertys setzen: an disem Beispiel ist es eine für eine size
- diese sind dann im css-file global verfügbar
```css
@property --size {
  syntax: "<length>";
    inherits: false;
    initial-value: 10px;
}
```
---

- ein quadrat, oder textfield oder könnte man wie folgt stylen:
- es ist immer breite zu höhe -> breite / höhe
```css
.myTextfield {
  width: 100px;
    aspect-ratio: 1 / 1;
}
```
---

- ein dreieck machen:
- im polygon(...) einfach beliebig viele punkte rein machen 
```css
.myTriangle {
    background-color: blue;
  width: 100px;
    aspect-ratio: 1 / 1;
    clip-path: polygon(
            0     0, 
            100%  0,
            50%   100%,
        );
}
```
---

***strict mode***
- kein js machen, wie man es nicht machen sollte
- zum beispiel, nicht ausversehen eine variable im global anlegen
---


