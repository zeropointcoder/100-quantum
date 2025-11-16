# Quantum Circuit Visualiser

## Goal
This project demonstrates the creation, simulation and visualisation of a quantum circuit

## Overview
1. Quantum Circuit (create_circuit):
- A quantum circuit with 2 qubits and 2 classical bits is created.
- A Hadamard gate (h) is applied to the first qubit to create a superposition.
- A CNOT gate (cx) is applied between the first and second qubit to entangle them.
- The qubits are measured into classical bits.

2. Simulation (simulate_circuit):
- The AerSimulator backend from Qiskit is used to simulate the quantum circuit.
- The circuit is transpiled and assembled into a quantum object, which is then executed on the simulator.
- The results are returned in the form of counts (the number of times each measurement outcome occurs).

3. Visualisation (visualise_results):
- The circuit is drawn using qc.draw().
- The measurement results are plotted as a histogram using plot_histogram to show the probability distribution of the measurement outcomes.

## Requirements
```bash
pip3 install -r requirements.txt
```

## Run
```bash
python3 quantum_circuit_visualiser.py
```