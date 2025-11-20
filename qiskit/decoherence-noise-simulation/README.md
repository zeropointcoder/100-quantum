# Decoherence Noise Simulation

To simulate the effect of decoherence using a noise model.


## Overview
**Quantum Circuit**:

- A simple quantum circuit is created with one qubit.
- A Hadamard gate (h(0)) is applied to the qubit to create a superposition state.
- A measurement is performed to collapse the state into either |0⟩ or |1⟩.

**Noise Model**:

We define a noise model using NoiseModel(). Two types of errors are added:
- Depolarising Error: This introduces random bit flips (Pauli-X, Y, Z operations) to simulate decoherence.
- Amplitude Damping Error: This models the loss of energy from the qubit, mimicking real-world decoherence due to environmental interaction.

**Simulation**:

The circuit is transpiled (optimised) for the simulator. The AerSimulator is used to run the quantum circuit with the noise model applied.

**Result Visualisation**:

The result is obtained using result.get_counts() and plotted using plot_histogram() to show the outcome probabilities, which reflect the decoherence effects on the quantum system.

**Notes**:

**Depolarising error**: Introduces random errors that can be thought of as the qubit being completely mixed due to interaction with the environment.

**Amplitude damping**: Models energy loss in the system. It is more realistic for qubits that interact with their environment and lose energy (such as in superconducting qubits).

**Adjusting Decoherence**:

We can control the amount of decoherence by tweaking the parameters of the noise model:
- For depolarising error, the first argument is the error probability (e.g., 0.1 means 10% error).
- For amplitude damping, we can adjust the damping factor (the second argument) and the error probability.

This approach allows us to simulate how noise and decoherence affect our quantum circuits and test our algorithms in a noisy environment, which is crucial for understanding the behavior of quantum computers in real-world conditions.

## Requirements
```bash
pip3 install -r requirements.txt
```

## Run
```bash
python3 decoherence_noise_simulation.py
```