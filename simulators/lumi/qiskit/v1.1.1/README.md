# Running Quantum programs with Qiskit Simulator on LUMI

## Loading the qiskit module
The qiskit module on LUMI can be loaded using the following command:

```
module use /appl/local/quantum/modulefiles
module load qiskit
```

This will load the default version of qiskit (v1.1.1) along with other major Qiskit packages (Terra, Nature, Aer, etc.)

## Run the quantum programs with sbatch
You can edit a test.sh file to run quantum programs. (recommended)

```{code-block} sh
:caption: test.sh

#!/bin/bash
#SBATCH --account=<project>
#SBATCH --partition=small-g
#SBATCH --ntasks=1
#SBATCH --cpus-per-task=1
#SBATCH --time=1:00:00

module purge
module use /appl/local/quantum/modulefiles
module load qiskit

python test.py <options>
```
Line 2-7 configures the partition, job name, number of nodes, and estimated time.  Line 9-11 cleans the module environment and loads the qiskit module.

The last line runs the Python file. In the example above, it's clear that the test.slurm file and test.py file are in the same directory.

You can run this sbatch file with command
```
sbatch test.sh
```

The results will be printed in a slurm.out file.

## Running with GPU
It is possible to run GPU accelerated circuits on LUMI.

In the Python file, you can configure the simulator with
```
simulator.setoptions(device='GPU')
```
Also, in the test.sh file, you can instead use a GPU node add a line for running on GPU
```
#SBATCH --gpus-per-node=1
#SBATCH --gpu-bind=closest
```

Here is an example script to run on the GPU node.

```
from qiskit import transpile
#from qiskit.compiler import transpile
from qiskit_aer import AerSimulator
from qiskit.circuit.library import QuantumVolume

# Create a statevector simulation test
depth = 20
qubits = 20
shots = 1000

# Choose statevector with GPU
sim = AerSimulator(method='statevector', device="GPU")

# Create the circuit
circuit = QuantumVolume(depth, qubits, seed=100)
circuit.measure_all()
circuit = transpile(circuit, sim)

# Run the simulation with cuStateVec

result_statevec = sim.run(circuit,shots=shots,seed_simulator=333).result()
time_statevec = float(result_statevec.to_dict()['results'][0]['time_taken'])

print(f"Time statevector: {time_statevec}.")
```

You'll notice that the time taken to run with the GPU is much smaller than running with the CPU node.
