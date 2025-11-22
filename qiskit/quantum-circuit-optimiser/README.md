# Quantum Circuit Optimiser

The Quantum Circuit Optimiser aims to streamline and enhance the efficiency of quantum circuits by reducing their size, depth, and complexity, ensuring better performance on quantum hardware and simulators.

## Overview
- Optimises quantum circuits by removing redundant gates and simplifying the design.
- Uses Qiskit transpiler with high-level optimisations (e.g., merging consecutive gates, eliminating unnecessary operations).
- Reduces circuit size and depth, improving efficiency.
- Applies automatic optimisation (level 3) for faster and more resource-efficient quantum algorithms.

## Explanation of the Changes:

**Redundant gates:** 
- We intentionally added redundant operations, like two consecutive Hadamard gates on the same qubit and repeated CNOT gates. These are prime candidates for optimisation.
    - Two consecutive Hadamard gates **(H H)** cancel each other out (since **H2=I** (Hsquare=I), the identity gate).
    - Two consecutive CNOT gates on the same pair of qubits (with the same control and target) cancel each other out (since **CNOT⋅CNOT=I**).
- By setting **optimization_level=3**, Qiskit's transpiler should automatically remove these redundant gates and simplify the circuit.

## Requirements
```bash
pip3 install -r requirements.txt
```

## Run
```bash
python3 quantum_circuit_optimiser.py
```