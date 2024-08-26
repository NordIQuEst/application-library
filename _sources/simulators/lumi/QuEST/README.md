# Guide for Running QuEST on LUMI

## Loading Spack

Spack is used for QuEST installation in LUMI. First we need to load Spack:

```
module load spack/23.09
```

After loading spack, make sure that you set the `$SPACK_USER_PREFIX`. For example `/project/project_XXXXXXXXX/spack`, :

```
export SPACK_USER_PREFIX=/project/project_XXXXXXXXX/spack
```

Then we need to unset the `SPACK_DISABLE_LOCAL_CONFIG` to get the local repo in the project

```
unset SPACK_DISABLE_LOCAL_CONFIG
```

and then we need to source the setup-env.sh:

```
. /pfs/lustrep2/appl/lumi/spack/23.09/0.21.0-user/share/spack/setup-env.sh
```

## Loading QuEST

First find which `QuEST` package do you want to load, `spack find -vl quest`

```
-- linux-sles15-zen / gcc@7.5.0 ---------------------------------
t2zmtm4 quest@3.5.0_AMD~amd~gpu~ipo~mpi+multithread build_system=cmake build_type=Release generator=make precision=1
beqfj4i quest@3.5.0_AMD~amd~gpu~ipo~mpi+multithread build_system=cmake build_type=Release generator=make precision=2
rgq52du quest@3.5.0_AMD~amd~gpu~ipo~mpi+multithread build_system=cmake build_type=Release generator=make precision=4
eykqmbl quest@3.5.0_AMD~amd~gpu~ipo+mpi+multithread build_system=cmake build_type=Release generator=make precision=1
klia3mx quest@3.5.0_AMD~amd~gpu~ipo+mpi+multithread build_system=cmake build_type=Release generator=make precision=2
3n6s66e quest@3.5.0_AMD~amd~gpu~ipo+mpi+multithread build_system=cmake build_type=Release generator=make precision=4
-- linux-sles15-zen2 / gcc@12.2.0 -------------------------------
mlxrbyt quest@3.5.0_AMD~amd~gpu~ipo~mpi~multithread build_system=cmake build_type=Release generator=make precision=1
os2pvri quest@3.5.0_AMD~amd~gpu~ipo~mpi~multithread build_system=cmake build_type=Release generator=make precision=2
wtg6iks quest@3.5.0_AMD~amd~gpu~ipo~mpi~multithread build_system=cmake build_type=Release generator=make precision=4
==> 9 installed packages
```

There are two options how to load `QuEST` here:

- with the hash tag

```
spack load --sh /t2zmtm4
```

- with the variants

```
spack load --sh quest ~gpu~ipo~mpi~multithread precision=1
```

After loading `QuEST`, we need to run the script to set up the variables. This script is stored in `$root/quest-3.5.0_AMD-XXXXX/bin/load_QuEST.sh` e.g `/scratch/project_462000056/spack/23.09/0.21.0/quest-3.5.0_AMD-3n6s66e/bin/load_QuEST.sh`

```
. load_QuEST.sh
```

It will give this output:

```
QuEST loaded ...
QuEST_INCLUDE_DIR:/scratch/project_XXXXXXXXX/spack/23.09/0.21.0/quest-3.5.0-6pyoxur/include
QuEST_LIBRARY_PATH:/scratch/project_XXXXXXXXX/spack/23.09/0.21.0/quest-3.5.0-6pyoxur/lib
QuEST_PREC=1
```

## Compiling the file

Once loaded, we can for example, compile the `bernstein_vazirani_circuit.c` that we want to run in QuEST.

```
cc -o bernstein -I $QuEST_INCLUDE_DIR -L $QuEST_LIBRARY_PATH  bernstein_vazirani_circuit.c -lQuEST -lm -DQuEST_PREC=$QuEST_PREC
```

The file used in this example can be found [here](https://github.com/QuEST-Kit/QuEST/blob/master/examples/bernstein_vazirani_circuit.c)

After that, we can just run the output `./bernstein` to get the result.

```
success probability: 0.99999976
```
