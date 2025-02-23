#!/bin/bash

# Set the current directory as the working directory
WORK_DIR=$(pwd)

# Function to check if a command was successful
check_success() {
    if [ $? -ne 0 ]; then
        echo "Error: $1 failed" >> $WORK_DIR/run.log
        exit 1
    fi
}

# Create and activate virtual environment
echo "Setting up virtual environment..." >> $WORK_DIR/run.log
python -m venv qiskit-nature-cp2k/venv
source qiskit-nature-cp2k/venv/bin/activate
python -m pip install --upgrade pip

# Install required packages
echo "Installing required packages..." >> $WORK_DIR/run.log
cd qiskit-nature-cp2k
pip install -e .
pip install qiskit-aer
pip install qiskit-braket-provider
pip install amazon-braket-default-simulator
pip install amazon-braket-schemas
pip install amazon-braket-sdk
cd ..

# First, pull the CP2K Singularity image if it doesn't exist
if [ ! -f "cp2k.sif" ]; then
    echo "Pulling CP2K Singularity image..." >> $WORK_DIR/run.log
    singularity pull cp2k.sif docker://cp2k/cp2k
    check_success "Pulling Singularity image"
fi

# Run CP2K using the .sif file
echo "Starting CP2K calculation..." >> $WORK_DIR/run.log
singularity exec --bind $WORK_DIR:/mnt --pwd /mnt \
    cp2k.sif \
    sh -c "umask 0000 && mpiexec -genv OMP_NUM_THREADS=1 -np 48 cp2k Al111_active_space.inp" > $WORK_DIR/cp2k.log 2>&1 &

# Store the Singularity process ID
SINGULARITY_PID=$!

# Wait for the socket file to be created
while [ ! -S $WORK_DIR/embedding_socket ]; do
   sleep 1
done

# Run the Python script using the virtual environment's Python
echo "Starting Python VQE calculation..." >> $WORK_DIR/run.log
python -u client-vqe-ucc.py --nalpha 1 --nbeta 1 --norbs 5 --adapt > $WORK_DIR/python_output.log 2>&1 &

# Wait for processes to finish
wait $SINGULARITY_PID
check_success "CP2K calculation"

# Ensure all files are readable and writable
chmod -R a+rw $WORK_DIR
echo "Calculations completed. Check cp2k.log and python_output.log for results." >> $WORK_DIR/run.log

# Deactivate the virtual environment when done
deactivate