# Quantum Basic Circuits

## Goal
To create, simulate, and visualise a basic quantum circuit using **Qiskit**, the leading open-source quantum SDK from IBM.

## Steps
1. Creates a quantum circuit with **one qubit** and **one classical bit**.  
2. Applies a **Hadamard gate (H)** to put the qubit into superposition — i.e., both `|0⟩` and `|1⟩` at once.  
3. Measures the qubit, which collapses it randomly to `|0⟩` or `|1⟩`.  
4. Runs the simulation 1000 times using the **Aer simulator** to observe the probability distribution.  
5. Visualises:
   - The quantum circuit diagram.
   - The measurement results as a histogram.

## Requirements
```bash
pip3 install qiskit qiskit-aer matplotlib pylatexenc
```

## Run
```bash
python3 quantum_basic_circuits.py
```