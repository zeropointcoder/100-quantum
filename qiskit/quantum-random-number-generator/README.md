# quantum-random-number-generator (QRNG)

A simple quantum-based random number generator built using Qiskit. It uses the quantum superposition principle to produce unbiased random bits. 

This project demonstrates how quantum superposition and measurement can be used to generate truly random numbers.

---

## Features
- Generates random bits using a quantum circuit.
- Combines multiple quantum bits into random integers.
- Works on both simulators and real IBM Quantum devices.

---

## How It Works
Quantum randomness comes from measuring a qubit in superposition.

1. A qubit starts in state |0⟩

2. Apply a **Hadamard gate (H)** → puts it into superposition:
   
   |ψ⟩ = (|0⟩ + |1⟩) / √2

3. Measuring the qubit collapses it randomly to either 0 or 1 each with 50% probability.

4. Repeat this for multiple bits to create a random number.

---

## Installation

```bash
# Clone this repository
git clone https://github.com/<your-username>/quantum-random-number-generator.git
cd quantum-random-number-generator

# Install dependencies
pip3 install -r requirements.txt
