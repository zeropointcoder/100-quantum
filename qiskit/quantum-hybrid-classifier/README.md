# Quantum hybrid classifier

## Goal
Implement a simple hybrid quantum–classical classifier. It uses a parameterised quantum circuit (ansatz) as a feature map, followed by a classical optimisation loop to train the parameters for binary classification.

## Concept Overview
We’ll build a classifier to distinguish between two small synthetic datasets (e.g., points in 2D).

## Steps
- Generate training data (two classes of 2D points).
- Encode data into a quantum circuit using a feature map.
- Define a parameterised ansatz circuit with trainable weights.
- Measure an observable (Pauli Z) to get a scalar output.
- Train parameters using a classical optimiser (gradient-free).
- Classify test points based on the sign of the expectation value.

## Requirements
```bash
pip3 install -r requirements.txt
```

## Run
```bash
python3 quantum_hybrid_classifier.py
```