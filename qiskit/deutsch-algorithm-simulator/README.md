# Deutsch Algorithm Simulation

Implement the 1-bit Deutsch algorithm.

## Overview
The algorithm prepares a superposition, applies the oracle encoding 
`f(x)`, and then interferes the paths via a final Hadamard.
- Measuring 0 means the function is `constant`.
- Measuring 1 means the function is `balanced`.

Deutsch's algorithm distinguishes two cases:
1. Constant function
    - Measurement result should be 0 → counts ≈ {'0': shots}

2. Balanced function
    - Measurement result should be 1 → counts ≈ {'1': shots}

Additionally, in Deutsch's algorithm, the measurement result is determined only by whether the function is constant or balanced, `not` by whether the constant function returns `0 or 1`.

So:
    - Constant 0 → output 0
    - Constant 1 → output 0

Only the balanced oracle returns 1.

## Requirements
```bash
pip3 install -r requirements.txt
```

## Run
```bash
python3 deutsch_algorithm_simulator.py
```