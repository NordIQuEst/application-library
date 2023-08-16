# Quantum Chemistry on Quantum Computers

## Introduction

Quantum chemistry is a field that focuses on solving complex problems related to molecular structures and chemical reactions. Traditional computational methods struggle to efficiently simulate quantum systems due to their exponential complexity. However, quantum computers offer a promising avenue for simulating quantum chemistry problems with improved efficiency. This document aims to explain the key concepts of quantum chemistry in the context of quantum computing for individuals with a background in quantum computing.

## Quantum Chemistry Basics

### Molecular Hamiltonian

In quantum chemistry, the behavior of a molecular system is described by a mathematical operator known as the molecular Hamiltonian (H). The Hamiltonian consists of kinetic energy terms for electrons and nuclei, as well as potential energy terms accounting for electron-electron, electron-nucleus, and nucleus-nucleus interactions. Solving the Schrödinger equation using the Hamiltonian provides insights into molecular properties.

### Quantum Chemistry Methods

Traditional quantum chemistry methods, such as Hartree-Fock (HF) and Density Functional Theory (DFT), employ approximations to solve the Schrödinger equation for molecular systems. While these methods are effective for many problems, they become computationally expensive for larger and more complex molecules due to their polynomial or worse scaling.

## Quantum Computing and Quantum Chemistry

### Quantum Advantage

Quantum computers leverage qubits, the quantum analogs of classical bits, to perform calculations using quantum principles like superposition and entanglement. Quantum algorithms, such as the Quantum Phase Estimation (QPE) algorithm, can exploit these properties to efficiently solve certain problems that would be intractable for classical computers. Quantum chemistry is one such problem that holds the potential for quantum advantage.

### Variational Quantum Eigensolvers (VQE)

VQE is a quantum algorithm used for solving molecular Hamiltonians on quantum computers. It combines classical optimization techniques with quantum simulations. In VQE, a parameterized quantum circuit (ansatz) prepares a trial wavefunction, and the expectation value of the Hamiltonian is measured. Classical optimization adjusts the ansatz parameters iteratively to minimize the energy, yielding an estimate of the molecule's ground-state energy.

### Quantum Phase Estimation (QPE)

QPE is a foundational quantum algorithm that can determine the eigenvalues (energies) of a unitary operator such as the molecular Hamiltonian. It achieves this by encoding the eigenvalue information into the phase of a quantum state and then extracting that phase using quantum Fourier transforms. QPE is a critical subroutine in many quantum chemistry algorithms, including VQE.

### Quantum Chemistry Simulators

Quantum chemistry simulators are software tools that run on quantum computers to emulate molecular systems' behavior. They provide insights into molecular properties by mapping the quantum chemistry problem onto a quantum processor. While current quantum computers have limitations in terms of qubit count and error rates, they offer a promising platform for advancing quantum chemistry research.

## Why Quantum Computers Can Be Advantageous?

Quantum chemistry poses significant challenges for classical computers due to the exponential complexity of simulating quantum systems. Quantum computers, by harnessing the principles of quantum mechanics, offer the potential to revolutionize quantum chemistry simulations. Algorithms like VQE and QPE pave the way for solving molecular Hamiltonians efficiently. As quantum hardware continues to advance, quantum chemistry on quantum computers holds the promise of unlocking insights into molecular properties with unprecedented speed and accuracy.

# Workflow of Quantum Chemistry Simulations

## 1. Obtaining the Molecular Wavefunction

Use classical quantum chemistry software to compute the molecular wave function using the Hartree-Fock (HF) method. This provides an initial approximation to the ground state electronic configuration of the molecule.

## 2. Construction of the Molecular Hamiltonian

The molecular Hamiltonian (H) is constructed in the second quantization formalism. It consists of kinetic energy terms for electrons and nuclei, as well as electron-electron, electron-nucleus, and nucleus-nucleus interaction terms. The Hamiltonian can be expressed as:

![Molecular Hamiltonian](https://latex.codecogs.com/png.image?H%20%3D%20T%20%2B%20V_%7Bee%7D%20%2B%20V_%7Bnn%7D%20%2B%20V_%7Ben%7D)

Where:
- **T** represents the kinetic energy operator for electrons.
- **V<sub>ee</sub>** accounts for electron-electron repulsions.
- **V<sub>nn</sub>** represents nucleus-nucleus repulsions.
- **V<sub>en</sub>** includes electron-nucleus interactions.

## 3. Mapping to Paulis

The next step is to map the molecular Hamiltonian to a sum of Pauli operators. This involves using the Jordan-Wigner, Bravyi-Kitaev, or other suitable transformation techniques to represent the Hamiltonian in terms of Pauli matrices (X, Y, Z) acting on qubits. The Pauli-mapped Hamiltonian can be expressed as:

![Pauli-Mapped Hamiltonian](https://latex.codecogs.com/png.image?H%20%3D%20%5Csum_i%20c_i%20%5Csigma_%7Bq_i%7D)

Where:
- ![c_i](https://latex.codecogs.com/png.image?c_i) are coefficients corresponding to different Pauli terms.
- ![q_i](https://latex.codecogs.com/png.image?q_i) are qubit indices associated with the Pauli terms.

## 4. Introducing the Ansatz: UCC or HEA?

The ansatz is a parameterized quantum circuit that prepares a trial wavefunction to approximate the ground state of the molecular system. Two common ansatzes used in quantum chemistry are the Unitary Coupled Cluster (UCC) ansatz and the Hardware Efficient Ansatz (HEA).

### UCC Ansatz:

The UCC ansatz expands the trial wavefunction using exponentials of cluster operators. It's expressed as:

![UCC Ansatz](https://latex.codecogs.com/png.image?%7C%5Cpsi%28%5Ctheta%29%5Crangle%20%3D%20e%5E%7BT%28%5Ctheta%29%7D%7C%5Cphi%5Crangle)

Where:
- ![T(θ)](https://latex.codecogs.com/png.image?T%28%5Ctheta%29) is the cluster operator parameterized by angles ![θ](https://latex.codecogs.com/png.image?%5Ctheta).
- ![|ϕ⟩](https://latex.codecogs.com/png.image?%7C%5Cphi%5Crangle) is the Hartree-Fock state.

### HEA Ansatz:

The HEA ansatz aims to reduce the depth and complexity of the quantum circuit. It utilizes entanglement patterns optimized for specific quantum hardware architectures. The details of the HEA structure depend on the specific implementation and hardware.

## 5. Obtaining the Expectation Value via VQE or QPE

### Variational Quantum Eigensolver (VQE):

In VQE, the expectation value of the Pauli-mapped Hamiltonian is computed using the ansatz-prepared state:

![VQE Expectation Value](https://latex.codecogs.com/png.image?E%28%5Ctheta%29%20%3D%20%5Clangle%5Cpsi%28%5Ctheta%29%7CH%7C%5Cpsi%28%5Ctheta%29%5Crangle)

Classical optimization techniques, such as gradient descent, are employed to find the ansatz parameters (![θ](https://latex.codecogs.com/png.image?%5Ctheta)) that minimize the energy expectation value (![E(θ)](https://latex.codecogs.com/png.image?E%28%5Ctheta%29)). The optimized energy gives an estimate of the molecule's ground state energy.

### Quantum Phase Estimation (QPE):

QPE can also be used to estimate the energy eigenvalues. By preparing a quantum state and applying QPE, the phase corresponding to the energy eigenvalue is encoded in the quantum state's amplitudes. Measuring this phase yields an estimate of the energy eigenvalue, which corresponds to the ground state energy.
