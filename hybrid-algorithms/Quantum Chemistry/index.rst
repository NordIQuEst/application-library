Quantum Chemistry
==================

Download the :download:`requirements.txt <requirements.txt>`

Setup
-----

Requires Python 3.9–3.12 (the pinned ``numpy==1.26.4`` and ``scipy==1.13.1`` have no wheels for newer versions; tested with Python 3.9 and 3.12).

.. code-block:: sh

   python3.12 -m venv .venv  # or any Python 3.9–3.12
   source .venv/bin/activate
   pip install -r requirements.txt

Then open the notebooks in Jupyter, e.g. with ``pip install jupyterlab && jupyter lab``.
See :doc:`Installation` for a conda alternative.

.. toctree::
   :maxdepth: 2

   Installation.md
   Theory.md
   VQE.ipynb
