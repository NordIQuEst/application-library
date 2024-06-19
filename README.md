---
orphan: true
---
# NordIQuEst Application Library

## Build the docs

The documentation for this page uses [sphinx](https://www.sphinx-doc.org/en/master/) and [sphinx book theme](https://sphinx-book-theme.readthedocs.io/en/latest/index.html).

Setup python environment

```
conda create -y -n sphinx python=3.12
conda activate sphinx
pip install -r requirements.txt
```

Build the docs from root directory

```
sphinx-build -b html .  build/html
```

View with firefox for example

```
firefox build/html/index.html
```
