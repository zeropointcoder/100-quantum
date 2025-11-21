# SWAP Gate Experiment

To demonstrate that the SWAP gate correctly exchanges the quantum states of two qubits.

## Overview

**Initial state**
- Qubit 0 is flipped to |1⟩
- Qubit 1 stays at |0⟩
So the starting state is |10⟩.

**After SWAP**
The SWAP gate exchanges the states of the qubits:
- q0 takes q1’s former value (0)
- q1 takes q0’s former value (1)
Final state should be |01⟩, which your histogram will confirm.

## Requirements
```bash
pip3 install -r requirements.txt
```

## Run
```bash
python3 swap_gate_experiment.py
```