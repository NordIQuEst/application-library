# Running Quantum programs on the Qiskit Simulator in eX3

## Creating / Loading the virtual environment
You can both create a virtual environment or use the prepared module environment to run quantum programs

You can simply use this command to load the Anaconda installed in eX3 for creating the virtual environment
```
module load anaconda3/x86_64/2022.05
conda create -n env python=3.11
conda activate env
pip install qiskit
...
```

You can also load the quantum virtual environment. Now we have some module environments which have installed some quantum program testing tools, such as Quito. It also includes the qiskit packages for you to use.
```
module use /cm/shared/ex3-qc-modules/modulefiles
module load quito/quito-py39-cu118-1.0
```

## Run the quantum programs directly
Given a Python file of quantum programs, test.py.
```
from qiskit import (
    QuantumCircuit,
    QuantumRegister,
    ClassicalRegister,
    execute,
    Aer,
)

q = QuantumRegister(2)
c = ClassicalRegister(2)
qc = QuantumCircuit(q,c)
qc.h(q[0])
qc.cx(q[0], q[1])
qc.measure(q, c)
backend = Aer.get_backend('aer_simulator')
result = execute(qc, backend, shots=1024).result().get_counts(qc)
print(result)
```
You can directly run it in eX3 with the command line
```
python test.py
```
And it shall run on the node that you are at and print the results.

## Run the quantum programs with sbatch
You can edit a test.slurm file to run quantum programs. (recommended)
```
#!/bin/bash
#SBATCH -p defq
#SBATCH --job-name=qiskit_test
#SBATCH -n 1     # tasks / ranks
#SBATCH --time 00-1:00:00    # time (D-HH:MM:SS)
module purge
module use /cm/shared/ex3-modules/latest/modulefiles
module load slurm/slurm/21.08.8
source /home/xinyi/anaconda3/bin/activate quito_gpu
export PYTHONPATH=root_path:$PYTHONPATH
srun python test.py
```
Line 2-5 configures the partition, job name, number of nodes, and estimated time.  Line 8 and 9 loads the module environment. You can also replace these two lines with activating the virtual environment created, which is
```
source /cm/shared/apps/anaconda3/x86_64/2022.05/bin/activate env
```
The last line runs the Python file. In the example above, it's clear that the test.slurm file and test.py file are in the same directory.

You can run this sbatch file with command
```
sbatch test.slurm
```

The results will be printed in a slurm.out file.

## Running with GPU
If you hope to run quantum programs with GPU, you can install qiskit-aer-gpu in your virtual environment. Or you can use the modules such as 'quito/quito-py39-cu118-1.0' directly.

In the Python file, you can configure the simulator with
```
simulator.setoptions(device='GPU')
```
Also, in the test.slurm file, you can instead use a GPU node add a line for running on GPU
```
#SBATCH -p dgx2q
#SBATCH --gres=gpu:1
```
