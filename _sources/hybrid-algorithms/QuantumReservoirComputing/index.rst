Quantum Reservoir Computing
===========================

This folder contains:

* `Logistic map.ipynb <Logisticmap.html>`_ - explains how to use quantum computers to predict time series

Download the :download:`requirements.txt <requirements.txt>`

Setup
-----

Requires Python 3.10 or newer (tested with Python 3.14).

.. code-block:: sh

   python3 -m venv .venv
   source .venv/bin/activate
   pip install -r requirements.txt

Then open the notebooks in Jupyter, e.g. with ``pip install jupyterlab && jupyter lab``.

The notebook takes about 10–15 minutes to execute, mostly in the two quantum reservoirs.

.. toctree::
   :maxdepth: 2

   Logistic map.ipynb
