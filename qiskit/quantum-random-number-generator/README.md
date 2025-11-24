# quantum-random-number-generator (QRNG)

To implement a quantum-based random number generator that uses the quantum superposition principle to produce unbiased random bits. 

This project demonstrates how quantum superposition and measurement can be used to generate truly random numbers.

## Features
- Generates random bits using a quantum circuit.
- Combines multiple quantum bits into random integers.
- Works on both simulators and real IBM Quantum devices.

## Steps
Quantum randomness comes from measuring a qubit in `superposition`.
1. A qubit starts in state `|0⟩`
2. Apply a **Hadamard gate (H)** → puts it into superposition:
   `|ψ⟩ = (|0⟩ + |1⟩) / √2`
3. Measuring the qubit collapses it randomly to either `0` or `1` each with `50%` probability.
4. Repeat this for multiple bits to create a random number.

## Requirements
```bash
pip3 install -r requirements.txt
```

## Run
```bash
python3 quantum_random_number_generator.py
```
