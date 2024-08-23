# Running Quantum programs on the Qiskit Simulator in LUMI

## Loading the virtual environment
First you need to activate the environment

```
source /appl/local/quantum/qiskit-aer/0.12.0/bin/activate
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

You can directly run it in LUMI with the command line
```
python test.py
```
And it will run on the node that you are at and print the results.
