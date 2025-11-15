# Bell State Creation

## Goal
This project demonstrates the creation of a Bell state (specifically entangled state) 
$$
|\Psi^+\rangle = \frac{1}{\sqrt{2}} (|00\rangle + |11\rangle)
$$ 

The Bell state is created by applying a Hadamard gate on the first qubit followed by a CNOT gate between the first and second qubits.

## Overview
Bell State

The Bell state is a specific kind of maximally entangled quantum state of two qubits. In this case, the state generated is:

$$
|\Psi^+\rangle = \frac{1}{\sqrt{2}} (|00\rangle + |11\rangle)
$$

## Requirements
```bash
pip3 install -r requirements.txt
```

## Run
```bash
python3 bell_state_creation.py
```