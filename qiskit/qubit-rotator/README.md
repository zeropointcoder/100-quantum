# Qubit rotator

To Visualise Qubit Rotations on the `Bloch Sphere`

## Overview
This project demonstrates how to simulate and visualise qubit rotations on the Bloch sphere. It provides a hands-on implementation of qubit rotation gates (`rx`, `ry`, `rz`) and plots the resulting qubit state on the Bloch sphere.

## Steps
- Initialise a quantum circuit with a single qubit.
- Apply a rotation gate (e.g., `rx`, `ry`, `rz`) to the qubit.
- Simulate the quantum circuit.
- Visualise the result on the `Bloch sphere`.

## Key Concepts:

**Qubit Rotation Gates**:
- `rx(theta, qubit)` applies a rotation around the `X-axis` by `theta`.
- `ry(theta, qubit)` applies a rotation around the `Y-axis` by `theta`.
- `rz(theta, qubit)` applies a rotation around the `Z-axis` by `theta`.

**Bloch Sphere Visualisation**:
- The `plot_bloch_multivector(statevector)` function generates a 3D Bloch sphere visualisation from the final state vector.

**Expected Output**:
The printed quantum circuit shows the sequence of gates applied.

The Bloch sphere is plotted, showing the qubit's final state after the rotations.

## Requirements
```bash
pip3 install -r requirements.txt
```

## Run
```bash
python3 qubit_rotator.py
```