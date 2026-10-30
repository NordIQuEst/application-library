Quantum Walk
==================

This folder contains:

* `Classical Random Walk.ipynb <ClassicalRandomWalk.html>`_ - explains how to simulate classical random walks on a quantum computer
* `Quantum Random Walk.ipynb <QuantumRandomWalk.html>`_ - explains how to simulate quantum random walks on a quantum computer

Download the :download:`requirements.txt <requirements.txt>`

Setup
-----

Requires Python 3.10–3.12 (``qiskit-aer==0.14.2`` has no wheels for newer versions; tested with Python 3.12).

.. code-block:: sh

   python3.12 -m venv .venv
   source .venv/bin/activate
   pip install -r requirements.txt

Then open the notebooks in Jupyter, e.g. with ``pip install jupyterlab && jupyter lab``.

.. toctree::
   :maxdepth: 2

   ClassicalRandomWalk.ipynb
   QuantumRandomWalk.ipynb
