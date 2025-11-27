# Simple Quantum Game

A minimal interactive game that uses a single qubit, where the player chooses quantum operations and the final measurement determines whether they win.

## Overview
- **Initial State**:
The game begins with a qubit in the standard state `∣0⟩`.

- **Player Moves**:
The player selects from a small set of quantum gates (e.g., `X`, `H`, `Z`) that will be applied in sequence to the qubit.

- **Circuit Construction**:
Each chosen move adds the corresponding gate to a Qiskit circuit.

- **Simulation**:
The final circuit is run on the simulator to produce measurement outcomes.

- **Win Condition**:
The result (usually measurement in the computational basis) is checked: e.g., the player wins if the qubit collapses to `∣1⟩`.

## Requirements
```bash
pip3 install -r requirements.txt
```

## Run
```bash
python3 simple_quantum_game.py
```