# Guide of Running QuEST in eX3

## Loading Spack

Spack is used for QuEST installation. First we need to load Spack:

```
module use /cm/shared/spack-modules/modulesfiles
module load spack/0.19.2
```

## Loading QuEST

First find which `QuEST` package do you want to load, `spack find -vl quest`

```
-- linux-ubuntu18.04-skylake_avx512 / gcc@8.4.0 -----------------
hsiv66y quest@3.5.0~gpu~ipo~mpi~multithread build_system=cmake build_type=RelWithDebInfo precision=1
4n625o4 quest@3.5.0~gpu~ipo~mpi~multithread build_system=cmake build_type=RelWithDebInfo precision=2
bbhnd67 quest@3.5.0~gpu~ipo~mpi~multithread build_system=cmake build_type=RelWithDebInfo precision=4
kt72o53 quest@3.5.0~gpu~ipo~mpi+multithread build_system=cmake build_type=RelWithDebInfo precision=1
5s2skmp quest@3.5.0~gpu~ipo~mpi+multithread build_system=cmake build_type=RelWithDebInfo precision=2
33fqt2c quest@3.5.0~gpu~ipo~mpi+multithread build_system=cmake build_type=RelWithDebInfo precision=4
2qabssi quest@3.5.0~gpu~ipo+mpi+multithread build_system=cmake build_type=RelWithDebInfo precision=1
joeqfso quest@3.5.0~gpu~ipo+mpi+multithread build_system=cmake build_type=RelWithDebInfo precision=2
neueo37 quest@3.5.0~gpu~ipo+mpi+multithread build_system=cmake build_type=RelWithDebInfo precision=4
y7cfly2 quest@3.5.0+gpu~ipo~mpi~multithread build_system=cmake build_type=RelWithDebInfo gpu_capability=70 precision=1
lifs72m quest@3.5.0+gpu~ipo~mpi~multithread build_system=cmake build_type=RelWithDebInfo gpu_capability=70 precision=2
```

There are two options how to load `QuEST` here:

- with the hash tag

```
spack load /hsiv66y
```

- with the variants

```
spack load quest ~gpu~ipo~mpi~multithread precision=1
```

After loading `QuEST`, we need to run the script to set up the variables

```
. load_QuEST.sh
```

It will give this output:

```
QuEST loaded ...
QuEST_INCLUDE_DIR:/cm/shared/spack-modules/apps/linux-ubuntu18.04-skylake_avx512/gcc-8.4.0/quest-3.5.0-hsiv66yqgmi2oumoa2mj5akjcl5vegwx/include
QuEST_LIBRARY_PATH:/cm/shared/spack-modules/apps/linux-ubuntu18.04-skylake_avx512/gcc-8.4.0/quest-3.5.0-hsiv66yqgmi2oumoa2mj5akjcl5vegwx/lib
QuEST_PREC=1
```

## Compiling the file

Once loaded, we can compile the `file.c` that we want to run in QuEST. For example,

```
cc -o bernstein -I $QuEST_INCLUDE_DIR -L $QuEST_LIBRARY_PATH  bernstein_vazirani_circuit.c -lQuEST -lm -DQuEST_PREC=$QuEST_PREC
```

After that, we can just run the output `./bernstein` to get the result.

```
success probability: 0.99999976
```

## Run with slurm for GPU

This is the example for running the GPU with slurm

```
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
module load slurm/slurm/21.08.8
module use /cm/shared/spack-modules/modulesfiles
module load spack/0.19.2

spack load quest +gpu~ipo~mpi~multithread build_system=cmake build_type=RelWithDebInfo gpu_capability=70 precision=1

. load_QuEST.sh

cc -o example -I $QuEST_INCLUDE_DIR -L $QuEST_LIBRARY_PATH example.c -lQuEST -lm -DQuEST_PREC=$QuEST_PREC
./gpu_example_32

```


## Running with `module`

To load QuEST module, first we need to run:

```
module use /cm/shared/ex3-qc-modules/modulefiles/
```

Then, choose which QuEST packages do you want to use. You can check by running `module av QuEST`. Then this list will come out
```
QuEST-kit/libQuEST/3.5.0/omp+fp32   QuEST-kit/libQuEST/3.5.0/omp+mpi+fp32   QuEST-kit/libQuEST/3.5.0/pthreaded+cu118+fp32  QuEST-kit/libQuEST/3.5.0/st+fp64
QuEST-kit/libQuEST/3.5.0/omp+fp64   QuEST-kit/libQuEST/3.5.0/omp+mpi+fp64   QuEST-kit/libQuEST/3.5.0/pthreaded+cu118+fp64  QuEST-kit/libQuEST/3.5.0/st+fp128
QuEST-kit/libQuEST/3.5.0/omp+fp128  QuEST-kit/libQuEST/3.5.0/omp+mpi+fp128  QuEST-kit/libQuEST/3.5.0/st+fp32
```
omp = multithreaded, mpi = distributed, fp = precision [1, 2, 4], cu118 = cuda


For example, `module load QuEST-kit/libQuEST/3.5.0/omp+mpi+fp64`,
this is a QuEST library with multithreaded, distributed and precision=2.

Once loaded, we can compile the `file.c` that we want to run in QuEST. For example,

```
cc -o bernstein bernstein_vazirani_circuit.c -lQuEST -lm -DQuEST_PREC=2
```

After that, we can just run the output `./bernstein` to get the result.

### Run QuEST GPU with sbatch

To run with GPU, we need to create a `test_gpu.job`

```
#!/bin/bash
#SBATCH --job-name="QuEST Spack GPU"
#SBATCH --time=00:10:00
#SBATCH --nodes=1
#SBATCH --ntasks-per-node=1
#SBATCH --mail-user=handy.kurniawan@ut.ee
#SBATCH --mail-type=END
#SBATCH --partition=a100q


module load QuEST-kit/libQuEST/3.5.0/pthreaded+cu118+fp32

cc -o gpu_example_32 tutorial_example.c -lQuEST -lm -DQuEST_PREC=1
./gpu_example_32

cc -o gpu_grover_32 grovers_search.c -lQuEST -lm -DQuEST_PREC=1
./gpu_grover_32

cc -o gpu_bernstein_32 bernstein_vazirani_circuit.c -lQuEST -lm -DQuEST_PREC=1
./gpu_bernstein_32
```

We can run this sbatch file with command

```sbatch test_gpu.job```

The results will be printed in a slurm.out file.

### Additional examples

For more examples, you can check [`job_quest_cpu.job`](job_quest_cpu.job) and [`job_quest_gpu.job`](job_quest_gpu.job).

- [`job_quest_spack_gpu.sh`](job_quest_spack_gpu.sh)
- [`run_quest_cpu.sh`](run_quest_cpu.sh)
