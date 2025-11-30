import cirq
import numpy as np

# Create 2 qubits
qubit1, qubit2 = cirq.LineQubit.range(2)

# Create a 2-qubit circuit with some basic gates
circuit = cirq.Circuit(
    cirq.H(qubit1), # Hadamard on qubit 1
    cirq.CNOT(qubit1, qubit2), # CNOT on qubit 1 as control and qubit 2 as target
    cirq.measure(qubit1, qubit2) # Measure both qubits
)

# Define the noise model
def add_noise_to_gate(op: cirq.Operation):
    """Function to add depolarizing noise after each gate."""
    noise_prob = 0.1 # 10% depolarizing noise

    noise_operations = [] # Apply noise to individual operations

    # For single-qubit operations, apply depolarizing noise to the qubit
    if len(op.qubits) == 1:
        noise_operations.append(op)
        noise_operations.append(cirq.depolarize(noise_prob).on(*op.qubits))

    # For multi-qubit operations (like CNOT), apply noise to each qubit individually
    elif len(op.qubits) > 1:
        noise_operations.append(op)
        for qubit in op.qubits:
            noise_operations.append(cirq.depolarize(noise_prob).on(qubit))

    return noise_operations

# Create a noisy circuit by applying noise after each gate
noisy_circuit = cirq.Circuit()
for moment in circuit:
    for op in moment:
        noisy_circuit.append(add_noise_to_gate(op))

# Simulate the noisy circuit
simulator = cirq.Simulator()
result = simulator.run(noisy_circuit, repetitions=1000)

# Inspect the measurement keys to see how Cirq has named them
print("\nMeasurement keys: ", result.measurements.keys())

# Access the histogram using that key
measurement_key = list(result.measurements.keys())[0] # Get the first key (for 2 qubits, this will be like '0,1')
print("\nMeasurement histogram:")
print(result.histogram(key=measurement_key), "\n") # Use the correct key for the histogram