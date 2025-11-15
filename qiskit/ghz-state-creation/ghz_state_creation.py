from qiskit import QuantumCircuit, transpile
from qiskit_aer import AerSimulator
from qiskit.visualization import plot_histogram
import matplotlib.pyplot as plt

def create_ghz_state():
    # Create a quantum circuit with 3 qubits and 3 classical bits
    qc = QuantumCircuit(3,3)

    # Apply a Hadamard Gate to the first qubit to create superposition
    qc.h(0)

    # Apply CNOT gates to entangle the qubits
    qc.cx(0,1) # CNOT between qubit 0 and 1
    qc.cx(1,2) # CNOT between qubit 1 and 2

    # Measure qubits
    qc.measure([0,1,2], [0,1,2])

    # Visualise
    print(qc)

    # Simulate
    simulator = AerSimulator()
    compiled_circuit = transpile(qc, simulator)
    results = simulator.run(compiled_circuit, shots=1024).result()
    counts = results.get_counts()

    plot_histogram(counts)
    plt.show()
    return counts

if __name__=="__main__":
    ghz_state_counts = create_ghz_state()
    print("Measurement results: ", ghz_state_counts)