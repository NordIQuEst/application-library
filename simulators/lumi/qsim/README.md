# QSIM

This documentation will show how to run QSIM in LUMI

## Running quantum programs directly in LUMI with Python file

First, you need to load the environment. At the moment, it only works in `uan02`, so to load QSIM, you need to login to `uan02`

```
ssh -i lumi <user_name>@lumi-uan02.csc.fi
```

Once you are connected to `uan02`, you can activate the environment

```
source /appl/local/quantum/qsim/v0.16.3/bin/activate
```

After that you can try to compile the `test.py` below

```
import cirq
import qsimcirq
q0, q1 = cirq.LineQubit.range(2)
circuit = cirq.Circuit(
	cirq.H(q0), cirq.X(q1), cirq.CX(q0, q1),
	cirq.measure(q0, key='qubit_0'),
	cirq.measure(q1, key='qubit_1'),
 )
print("Circuit:")
print(circuit)
print('qsim results:')
qsim_simulator = qsimcirq.QSimSimulator()
qsim_results = qsim_simulator.run(circuit, repetitions=5)
print(qsim_results)
```

You can directly run it in LUMI with the command line
```
python test.py
```

And it shall run on the node that you are at and print the results.
