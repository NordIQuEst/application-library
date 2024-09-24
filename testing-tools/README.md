# Run Software Testing Tools on Jupyter Notebook
This tutorial tells you how to load the quantum testing module and execute on Jupyter Notebook. Please follow the steps here to load the model and open the Jupyter Notebook connected to eX3. Then you can begin to run three quantum software testing tools Quito, QuSBT and QuCAT.

## Step 1. Load the Jupyter Module environment
Please first load all QC models on eX3.
```
module use /cm/shared/ex3-qc-modules/modulefiles
```

Currently, we probide the following QC modules:

Google,  IBM,  Nvidia,  qucat,  QuEST-kit,  quito,  qusbt,  Xanadu,  ZabataComputing

You can load the environment of one of the three tools, quito, qusbt and qucat.

Taking quito enviornment as an example:
```
module load quito/quito-py311-jupyter-cu118-1.0
```

## Step 2. Open the Jupyter Notebook on eX3 with a port that is not in use currently
```
jupyter notebook --no-browser --port [port number]
```

## Step 3. Open the local terminal and log in
```
ssh -t -t [user name]@[eX3 login node ip address] -L [port number]:localhost:[port number] ssh g001 -L [port number]:localhost:[port number]
```

Now, you can open http://localhost:[port number]/ in your local browser to run the Jupyter Notebook tutorials.
