project = "NordIQuEst Application Library"
copyright = "2024, NordIQuEst"
author = "NordIQuEst"


extensions = ["myst_nb"]

templates_path = ['_templates']
exclude_patterns = [
    "_build",
    "Thumbs.db",
    ".DS_Store",
    "jupyter_execute",
]

source_suffix = {
    '.rst': 'restructuredtext',
    '.txt': 'myst-nb',
    '.ipynb': 'myst-nb',
    '.md': 'myst-nb',
}

# https://myst-nb.readthedocs.io/en/latest/computation/execute.html
nb_execution_mode = "off"

html_theme = "sphinx_book_theme"
html_logo = "docs/_static/images/nq_logo2.png"
html_title = "NordIQuEst Application Library"
html_favicon = "docs/_static/images/favicon.png"
html_static_path = ['docs/_static']
html_theme_options = {
    "repository_url": "https://github.com/NordIQuEst/application-library",
    "use_repository_button": True,
}
