# **NordIQuEst Application Library**

Welcome to the NordIQuEst Application Library.

## Run the examples

Each example folder has its own `requirements.txt`, and the pinned versions differ
between folders. Create a separate virtual environment per folder and follow the
**Setup** section on that example's page; it states which Python versions work.
The `requirements.txt` in the repository root is only for building the docs (below).

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
