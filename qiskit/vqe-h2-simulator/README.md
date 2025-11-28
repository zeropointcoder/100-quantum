# VQE-H2-Simulator

To implement the Variational Quantum Eigensolver (VQE) algorithm to find the ground state energy of the H₂ molecule using quantum simulation.

## Overview
1. **Hamiltonian** – Hard-code `H₂` qubit Hamiltonian (`SparsePauliOp`).

2. **Ansatz** – Build a `2-qubit` parameterised circuit with `3` variational parameters.

3. **Expectation Value** – Compute `⟨ψ(θ)|H|ψ(θ)⟩` using `Statevector`.

4. **Optimisation** – Minimise energy with `SLSQP` classical optimiser.

5. **Result** – Extract and report the `minimum` energy.

## Example Output
```bash
Running VQE (NumPy backend)…

Ground-state energy: -1.137270174246 Hartree

Final energy: -1.137270174246 Ha
```

## Requirements
```bash
pip3 install -r requirements.txt
```

## Run
```bash
python3 vqe_h2_simulator.py
```