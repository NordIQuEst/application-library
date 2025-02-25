# **NordIQuEst Application Library**

Welcome to the NordIQuEst Application Library.

## Build the docs

The documentation for this page uses [sphinx](https://www.sphinx-doc.org/en/master/) and [sphinx book theme](https://sphinx-book-theme.readthedocs.io/en/latest/index.html).

Setup python environment

```bash
conda create -y -n sphinx python=3.12
conda activate sphinx
pip install -r requirements.txt
```

Build the docs from root directory

```bash
sphinx-build -b html . build/sphinx/html
```

⚠️ If you encounter the error `Could not import extension ...` , try to deactive and activate your environment again. ⚠️

View with firefox for example

```bash
firefox build/html/index.html
```
