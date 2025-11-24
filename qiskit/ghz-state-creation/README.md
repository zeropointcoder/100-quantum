# Greenberger-Horne-Zeilinger (GHZ) State Creation

This project demonstrates the creation of a `GHZ` state

## Overview
A `GHZ` state involves multiple qubits that are entangled in a specific way. The most common form is a 3-qubit `GHZ` state, which is represented as:

$$
|GHZ\rangle = \frac{1}{\sqrt{2}} (|000\rangle + |111\rangle)
$$

## Explanation
- **Quantum Circuit Setup**: We initialise a quantum circuit with 3 qubits and 3 classical bits. The classical bits will be used to store the measurement results.

- **Hadamard Gate**: The Hadamard gate (denoted by `h`) is applied to the first qubit. This creates a superposition of `∣0⟩` and `∣1⟩`.

- `CNOT` Gates: The CNOT (`controlled-X`) gates are applied to entangle the qubits. The first CNOT gate entangles the first and second qubits, while the second CNOT gate entangles the second and third qubits.

- **Measurement**: The qubits are measured and the results are stored in the classical bits.

- Display the results as a histogram.

## Expected Output:
When we run this code, we get a histogram that shows two possible outcomes:
- `000` (with a probability of `50%`)
- `111` (with a probability of `50%`)

These are the two states that the GHZ state collapses into after measurement.

## Requirements
```bash
pip3 install -r requirements.txt
```

## Run
```bash
python3 ghz_state_creation.py
```