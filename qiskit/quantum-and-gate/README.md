# Quantum AND Gate (Toffoli Gate)

## Goal
This project implements a **quantum AND gate** using the **Toffoli (CCX) gate** in Qiskit.

## Overview
 
A Toffoli gate acts as a classical AND when the target qubit is initialised to \|0⟩.

Truth table:
- target = control1 AND control2

If the target starts as 0, then after CCX it becomes:
target = control1 AND control2 → This is a quantum AND gate.

## Requirements
```bash
pip3 install -r requirements.txt
```

## Run
```bash
python3 quantum_and_gate.py
```