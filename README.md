# MkDocs Setup

## Setup

```bash
brew install mkdocs uv

# Material + 2-Leerzeichen-Listen ins Python von MkDocs installieren
PY=$(head -1 "$(realpath "$(which mkdocs)")" | sed 's/^#!//')
uv pip install --python "$PY" --break-system-packages mkdocs-material mdx_truly_sane_lists
```

## mkdocs.yml

```yaml
site_name: Meine Notizen
site_url: https://<user>.github.io/<repo>/

repo_url: https://github.com/<user>/<repo>
repo_name: <user>/<repo>

docs_dir: docs
site_dir: site

theme:
  name: material
  language: de
  features:
    - navigation.indexes   # index.md eines Ordners = Sektion selbst
    - navigation.top
    - content.code.copy
  palette:
    - scheme: default
      toggle:
        icon: material/brightness-7
        name: Dark Mode
    - scheme: slate
      toggle:
        icon: material/brightness-4
        name: Light Mode

plugins:
  - search

markdown_extensions:
  - admonition
  - tables
  - mdx_truly_sane_lists   # verschachtelte Listen mit 2 Leerzeichen
  - toc:
      permalink: true

exclude_docs: |
  .DS_Store
  *.py
```

## Nutzen

```bash
mkdocs serve       # lokal: http://127.0.0.1:8000
mkdocs gh-deploy   # auf GitHub Pages veröffentlichen
```

> Nach `brew upgrade mkdocs` die beiden `PY=`/`uv`-Zeilen erneut ausführen.
