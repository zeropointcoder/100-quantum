from qiskit import QuantumCircuit, transpile
from qiskit_aer import AerSimulator
from qiskit.visualization import plot_histogram
import matplotlib.pyplot as plt

# Create a quantum circuit
def create_circuit():
    # Create a quantum circuit with 2 qubits and 2 classical bits
    qc = QuantumCircuit(2,2)

    # Add quantum gates
    qc.h(0) # Apply Hadamard gate on qubit 0
    qc.cx(0,1) # Apply CNOT gate (control qubit 0, target qubit 1)
    qc.measure([0,1],[0,1])

    return qc

# Simulate the circuit
def simulate_circuit(qc):
    simulator = AerSimulator()
    compiled_circuit = transpile(qc, simulator)
    result = simulator.run(compiled_circuit, shots=1024).result()
    counts = result.get_counts()

    return counts

# Visualise the circuit and the results
def visualise_result(qc, counts):
    # Plot quantum circuit
    print("Quantum Circuit:")
    print(qc.draw())

    print("Measurement result (Counts):", counts)
    plot_histogram(counts).show()
    plt.show()

# Main function
def main():
    # Create the quantum circuit
    qc = create_circuit()

    # Simulate the circuit
    counts = simulate_circuit(qc)

    visualise_result(qc, counts)

# Run the main function
if __name__=="__main__":
    main()