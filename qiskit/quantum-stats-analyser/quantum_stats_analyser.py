from qiskit import Aer, QuantumCircuit, transpile
from qiskit.visualization import plot_histogram
import matplotlib.pyplot as plt

# Create a 2-qubit quantum circuit
qc = QuantumCircuit(2, 2)

# Apply a Hadamard gate to the first qubit
qc.h(0)

# Apply a CNOT gate with the first qubit as control and the second as target
qc.cx(0, 1)

# Measure the qubits
qc.measure([0, 1], [0, 1])

# Visualize the circuit
print("Quantum Circuit:")
print(qc.draw())

# Set up the Aer simulator
simulator = Aer.get_backend('aer_simulator')

# Compile and execute the circuit on the simulator
compiled_circuit = transpile(qc, simulator)
job = simulator.run(compiled_circuit, shots=1024)

# Get the results from the simulation
result = job.result()

# Retrieve the counts (measurement results)
counts = result.get_counts(compiled_circuit)

# Print the measurement results
print("\nMeasurement counts:", counts)

# Calculate and print probabilities of each outcome
total_shots = sum(counts.values())
probabilities = {outcome: count / total_shots for outcome, count in counts.items()}
print("\nMeasurement Probabilities:")
for outcome, probability in probabilities.items():
    print(f"Outcome {outcome}: Probability {probability:.4f}")

# Plot the histogram of the measurement results
plot_histogram(counts)
plt.show()
