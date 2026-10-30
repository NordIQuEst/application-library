Variational Quantum Eigensolver (VQE) Tutorial
==============================================

Download the :download:`requirements.txt <requirements.txt>`

Setup
-----

Requires Python 3.10–3.12 (``cirq-core==1.4.0`` needs ``numpy<2``, which has no wheels for newer versions; tested with Python 3.12).

.. code-block:: sh

   python3.12 -m venv .venv
   source .venv/bin/activate
   pip install -r requirements.txt

Then open the notebooks in Jupyter, e.g. with ``pip install jupyterlab && jupyter lab``.

.. toctree::
   :maxdepth: 2

   vqe-h2-cirq.ipynb
   vqe-h2-qiskit.ipynb
