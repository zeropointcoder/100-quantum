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
1. A qubit starts in the |0⟩ state.
2. A **Hadamard gate (H)** is applied to place it in an equal superposition of |0⟩ and |1⟩.
3. Measuring the qubit collapses it randomly to either 0 or 1.
4. Repeat this for multiple bits to create a random number.

---

## Installation

```bash
# Clone this repository
git clone https://github.com/<your-username>/quantum-random-number-generator.git
cd quantum-random-number-generator

# Install dependencies
pip install -r requirements.txt
