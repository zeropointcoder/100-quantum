from qiskit import QuantumCircuit, transpile
from qiskit_aer import AerSimulator
from qiskit.visualization import plot_histogram
import matplotlib.pyplot as plt

def create_bell_state():
    # Create quantum circuit with 2 qubits
    qc = QuantumCircuit(2,2)

    # Apply Hadamard gate to the 1st qubit
    qc.h(0)

    # Apply CNOT gate with -> control qubit as the first qubit and target as the second qubit
    qc.cx(0,1)

    # Measure the qubits
    qc.measure([0,1], [0,1])

    print(qc)

    # Use AerSimulator
    simulator = AerSimulator()
    compiled_circuit = transpile(qc, simulator)

    result = simulator.run(compiled_circuit, shots=1024).result()

    counts = result.get_counts()
    plot_histogram(counts)
    plt.show()

    return counts

if __name__=="__main__":
    bell_state_counts = create_bell_state()
    print("Measurement result: ", bell_state_counts)