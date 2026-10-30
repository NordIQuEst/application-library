# Installation instructions

Requires Python 3.9–3.12 (tested with Python 3.9 and 3.12).

## Instructions to Install the Necessary Packages in a Python Virtual Environment:

```
python3.12 -m venv .venv  # or any Python 3.9–3.12
source .venv/bin/activate
pip install -r requirements.txt
```

## Instructions to Install the Necessary Packages in a Conda Environment:

1. Make sure you have Anaconda or Miniconda installed on your system. If not, you can download it from [here](https://docs.conda.io/projects/conda/en/latest/user-guide/install/index.html).

2. Open a terminal or command prompt.

3. Create a new Conda environment named "qchem" with Python 3.12 (the pinned `numpy==1.26.4` and `scipy==1.13.1` only have wheels for Python 3.9–3.12):

   ```
   conda create -y -n qchem python=3.12
   ```

4. Activate the "qchem" environment:

   ```
   conda activate qchem
   ```

5. Install the necessary packages using `pip`:

   ```
   pip install -r requirements.txt
   ```

6. You've now successfully installed the required packages (PySCF, Qiskit, Qiskit Nature) within the "qchem" environment.

7. To deactivate the environment and return to your base environment, simply run:

   ```
   conda deactivate
   ```

Remember that this method uses `pip` to install the packages within a Conda environment. While Conda environments are typically managed with `conda` commands, using `pip` within a Conda environment can still work smoothly for many packages.

Feel free to replace "qchem" with your preferred environment name if you wish to name it differently. This process will ensure you have a Conda environment set up with the required packages for your quantum chemistry calculations.
