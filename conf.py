project = "NordIQuEst Application Library"
copyright = "2024, NordIQuEst"
author = "NordIQuEst"


show_authors = True

extensions = ["myst_nb", "sphinx.ext.mathjax", "sphinx_lesson", "sphinx.ext.githubpages",]

templates_path = ['_templates']
exclude_patterns = [
    "_build",
    "Thumbs.db",
    ".DS_Store",
    "jupyter_execute",
    "build",
]

source_suffix = {
    '.rst': 'restructuredtext',
    '.ipynb': 'myst-nb',
    '.md': 'myst-nb',
}

myst_enable_extensions = [
    "amsmath",
    "dollarmath",
]

suppress_warnings = ["myst.xref_missing", "myst.iref_ambiguous"]

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
    "show_navbar_depth": 2,  # https://sphinx-book-theme.readthedocs.io/en/stable/sections/sidebar-primary.html#control-the-depth-of-the-left-sidebar-lists-to-expand
}

# -- MathJax options ----------------------------------------------------------

# Here we configure MathJax, mostly to define LaTeX macros.
mathjax3_config = {
    'tex': {
        'macros': {
            'vr': r'\vec{r}',  # no arguments
            'ket': [r'\left| #1 \right\rangle', 1],  # one argument
            'bra': [r'\left| #1 \right\langle', 1],
            'iprod': [r'\left\langle #1 | #2 \right\rangle', 2],  # two arguments
        }
    }
}
