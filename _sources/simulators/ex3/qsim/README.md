# QSIM
## Running quantum programs directly in eX3 with Python file

Loading the module environment
```
module use /cm/shared/ex3-qc-modules/modulefiles
module load Google/quantumlib/Cirq/cirq-py310-1.1.0
```
Given a Python file of quantum programs, `test.py`

First we need to import Cirq and QSim library
```
import cirq
import qsimcirq
```

And here an example how to create a quantum circuit with measurement
```
q0, q1 = cirq.LineQubit.range(2)
circuit = cirq.Circuit(
	cirq.H(q0), cirq.X(q1), cirq.CX(q0, q1),
	cirq.measure(q0, key='qubit_0'),
	cirq.measure(q1, key='qubit_1'),
 )
 print("Circuit:")
 print(circuit)
```

Then we can simulate the circuit with qsim and return just the measurement values
```
print('qsim results:')
qsim_simulator = qsimcirq.QSimSimulator()
qsim_results = qsim_simulator.run(circuit, repetitions=5)
print(qsim_results)
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
#SBATCH --job-name=qsim_test
#SBATCH -n 1     # tasks / ranks
#SBATCH --time 00-1:00:00    # time (D-HH:MM:SS)
module purge
module use /cm/shared/ex3-modules/latest/modulefiles
module load slurm/slurm/21.08.8
source /home/xinyi/anaconda3/bin/activate quito_gpu
export PYTHONPATH=root_path:$PYTHONPATH
srun python test.py
```
Line 2-5 configures the partition, job name, number of nodes, and estimated time.  Line 8 and 9 loads the module environment. The last line runs the Python file. I

You can run this sbatch file with the command
```
sbatch test.slurm
```

The results will be printed in a slurm.out file.
