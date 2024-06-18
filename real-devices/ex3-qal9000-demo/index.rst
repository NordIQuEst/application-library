ex3-qal9000 Demo
================

This is a demonstration done with QAL9000 and ex3 in November 2022. The demonstration can be viewed on youtube `here <https://www.youtube.com/watch?v=PP3F9pcZgL8>`_ . A blog post was written about the event `here <https://nordiquest.net/_posts/2022-12-13-Nordiquest_QC_Norway/>`_.

Download the :download:`requirements.txt <requirements.txt>`

.. toctree::
   :maxdepth: 1

   compute-bloch-frames.ipynb


Dependencies
------------

- `python +v3.8 <https://www.python.org/>`_
- `qiskit <https://github.com/Qiskit/qiskit>`_
- `tergite-qiskit-connector <https://test.pypi.org/project/tergite-qiskit-connector/>`_



Quick Start
-----------

- Ensure you have `anaconda/miniconda <https://docs.anaconda.com/free/miniconda/index.html>`_ installed. *You can also use an ordinary python installation*.
- Clone the repo and enter its root folder
- Create a conda environment::

	conda create -n qaldemo python=3.9

- Install dependencies::

	conda activate qaldemo
	pip install -r requirements.txt --extra-index-url https://test.pypi.org/simple

- Get an API token from `qal9000.se <https://qal9000.se>`_ if you don't have one.

**Note that you should be attached to a project on `qal9000.se <https://qal9000.se>`_ or `NordIQuEst Resource Allocator <https://access.nordiquest.net/>`_ before you can get an API token**

**It is also possible to use a qal9000 API running on a different URL. You will, however, have to set the ``QAL9000_API_URL`` environment variable.**

- Export the API token to your environment::

	export QAL9000_API_TOKEN=<your qal9000.se API token>

- If you have the ``QAL9000_BCC_URL`` (URL to the **B**ackend **C**ontrol **C**omputer), you can also export it in order to run ``demo_compute_qmc_frames.py``::

	export QAL9000_BCC_URL=<URL to the backend control computer>

- Run any of the scripts::

	python demo_compute_bloch_frames.py
	python demo_compute_qmc_frames.py
	python show_frames.py

Contributors
------------

- Axel Andersson (Chalmers)
- Martin Ahindura (Chalmers)

Links
-----

- :download:`LICENSE <LICENSE.txt>`
