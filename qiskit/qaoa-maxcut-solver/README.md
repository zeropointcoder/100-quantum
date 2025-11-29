# QAOA Maxcut Solver

Implement a `QAOA` workflow to solve a small graph optimisation problem (e.g., `Max-Cut`) using manual sampling and classical optimisation.

## Overview
### What QAOA Is
`QAOA` is a variational (hybrid quantum-classical) algorithm designed to solve combinatorial optimisation problems, such as `MaxCut`, `MaxSAT`, `graph coloring`, etc.

**It works by**:
1. Encoding the problem into a quantum Hamiltonian.
2. Applying alternating layers of:
    - a problem unitary (from the cost Hamiltonian), 
    - and a mixing unitary.
3. Optimising angles (parameters) using a classical optimiser.
4. Sampling the quantum state to obtain a good approximate solution.

## Explanation
1. **Define the graph** – specify nodes and edges (e.g., `NetworkX`) and build the cost `Hamiltonian` for `Max-Cut`.

2. **Build the QAOA circuit** – use `QAOAAnsatz` from Qiskit to create the variational quantum circuit, then set the depth `p`.

3. **Select a backend** – run on an AerSimulator or a real quantum backend via Qiskit Runtime (optional).

4. **Optimise parameters** – use a classical optimiser (e.g., `COBYLA`, `SPSA`) to update the variational angles and minimise the expected cut value.

5. **Sample the bitstring solution** – sample from the quantum circuit, then interpret the most frequent bitstring as the graph's partition.

6. **Evaluate quality** – compute the cut value by comparing the partition from the bitstring with the actual graph's edges.

## Requirements
```bash
pip3 install -r requirements.txt
```

## Run
```bash
python3 qaoa_maxcut_solver.py
```