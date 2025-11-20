from qiskit import QuantumCircuit, transpile
from qiskit_aer import AerSimulator
from qiskit_aer.noise import NoiseModel, depolarizing_error, amplitude_damping_error
from qiskit.visualization import plot_histogram
import matplotlib.pyplot as plt

# Function to run the simulation without noise
def run_without_noise():
    qc = QuantumCircuit(1,1) # Create quantum circuit
    qc.h(0) # Apply Hadamard Gate to create superposition
    qc.measure(0,0) # Measure the qubit

    simulator = AerSimulator()
    compiled_circuit = transpile(qc, simulator)
    result = simulator.run(compiled_circuit, shots=1024).result()
    counts = result.get_counts()

    return counts

# Function to run the simulation with noise
def run_with_noise():
    qc = QuantumCircuit(1,1)
    qc.h(0)
    qc.measure(0,0)

    # Create a noise model
    noise_model = NoiseModel()

    # Add depolarizing error (simulating random bit flips) for the Hadamard Gate
    depolarizing_err = depolarizing_error(0.1,1) # 10% depol error
    noise_model.add_all_qubit_quantum_error(depolarizing_err, ['h'])

    # Add amplitude damping (simulating energy loss) for the Hadamard Gate
    amplitude_damping = amplitude_damping_error(0.1,0.9) # 10% error probability and 90% damping factor
    noise_model.add_all_qubit_quantum_error(amplitude_damping, ['h'])

    simulator = AerSimulator()
    compiled_circuit = transpile(qc, simulator)
    result = simulator.run(compiled_circuit, shots=1024).result()
    counts = result.get_counts()

    return counts

# Run quantum simulation without noise
counts_without_noise = run_without_noise()

# Run quantum simulation with noise
counts_with_noise = run_with_noise()

# Plot the results
fig, (ax1, ax2) = plt.subplots(1,2,figsize=(12,6))

# Plot the histogram for results without noise
ax1.set_title("Without Noise: ")
plot_histogram(counts_without_noise, ax=ax1)

# Plot the histogram for results with noise
ax2.set_title("With Noise: ")
plot_histogram(counts_with_noise, ax=ax2)

# Show the plots
plt.tight_layout()
plt.show()

# Print the results for both cases
print("Counts without noise: ", counts_without_noise)
print("Counts with noise: ", counts_with_noise)