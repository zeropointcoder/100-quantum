# Hadamard single qubit superposition

This project demonstrates quantum superposition on a single qubit using **Qiskit**. A `Hadamard` gate is applied to a qubit to create a `superposition` state, and the results are visualised on a `Bloch sphere` and as a measurement histogram.

## Theory
- The Hadamard gate `(H)` puts a single qubit into an equal superposition of `|0⟩` and `|1⟩`.
- Measurement collapses the qubit state to either `|0⟩` or `|1⟩`, producing probabilistic outcomes, it has approximately a `50%` chance of being `0` or `1`.
- A single qubit is put into `superposition` with a `Hadamard` gate, visualised on the `Bloch sphere`, then `measured` and `simulated` to show roughly equal probabilities of `0` and `1`.

## Requirements
```bash
pip3 install -r requirements.txt
```

## Run
```bash
python3 hadamard_superposition.py
```