#!/bin/bash
#SBATCH --job-name="QuEST Spack GPU"
#SBATCH --time=00:10:00
#SBATCH --nodes=1
#SBATCH --ntasks-per-node=1
#SBATCH --mail-user=handy.kurniawan@ut.ee
#SBATCH --mail-type=END
#SBATCH --partition=dgx2q
##SBATCH -o output/dgx2q/slurm.%N.%j.out # STDOUT
##SBATCH -e output/dgx2q/slurm.%N.%j.err # STDERR

ulimit -s 10240
#mkdir -p ~/output/dgx2q

module purge
module load slurm/20.02.7
module use /cm/shared/spack-modules/modulesfiles
module load spack/0.19.2

spack load quest +gpu~ipo~mpi~multithread build_system=cmake build_type=RelWithDebInfo gpu_capability=70 precision=1

. load_QuEST.sh

cc -o gpu_example_32 -I $QuEST_INCLUDE_DIR -L $QuEST_LIBRARY_PATH ~/examples/tutorial_example.c -lQuEST -lm -DQuEST_PREC=1
./gpu_example_32

cc -o gpu_grover_32 -I $QuEST_INCLUDE_DIR -L $QuEST_LIBRARY_PATH ~/examples/grovers_search.c -lQuEST -lm -DQuEST_PREC=1
./gpu_grover_32

cc -o gpu_bernstein_32 -I $QuEST_INCLUDE_DIR -L $QuEST_LIBRARY_PATH ~/examples/bernstein_vazirani_circuit.c -lQuEST -lm -DQuEST_PREC=1
./gpu_bernstein_32


spack unload quest +gpu~ipo~mpi~multithread build_system=cmake build_type=RelWithDebInfo gpu_capability=70 precision=1

spack load quest +gpu~ipo~mpi~multithread build_system=cmake build_type=RelWithDebInfo gpu_capability=70 precision=2

. load_QuEST.sh

cc -o gpu_example_64 -I $QuEST_INCLUDE_DIR -L $QuEST_LIBRARY_PATH ~/examples/tutorial_example.c -lQuEST -lm -DQuEST_PREC=2
./gpu_example_64

cc -o gpu_grover_64 -I $QuEST_INCLUDE_DIR -L $QuEST_LIBRARY_PATH ~/examples/grovers_search.c -lQuEST -lm -DQuEST_PREC=2
./gpu_grover_64

cc -o gpu_bernstein_64 -I $QuEST_INCLUDE_DIR -L $QuEST_LIBRARY_PATH ~/examples/bernstein_vazirani_circuit.c -lQuEST -lm -DQuEST_PREC=2
./gpu_bernstein_64

spack unload quest +gpu~ipo~mpi~multithread build_system=cmake build_type=RelWithDebInfo gpu_capability=70 precision=2
