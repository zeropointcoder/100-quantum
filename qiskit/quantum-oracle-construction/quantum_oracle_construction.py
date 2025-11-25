from qiskit import QuantumCircuit
from qiskit_aer import AerSimulator
from qiskit.visualization import plot_histogram
import matplotlib.pyplot as plt

def build_oracle(n_qubits, marked_state):
    """
    Return a QuantumCircuit implementing a phase-flip oracle.
    """
    qc = QuantumCircuit(n_qubits, name=f"Oracle_{marked_state}")

    # Match zeros
    for i, bit in enumerate(marked_state):
        if bit == '0':
            qc.x(i)

    # Multi-controlled Z
    qc.h(n_qubits - 1)
    qc.mcx(list(range(n_qubits - 1)), n_qubits - 1)
    qc.h(n_qubits - 1)

    # Undo
    for i, bit in enumerate(marked_state):
        if bit == '0':
            qc.x(i)

    return qc # Note: return the circuit, NOT a Gate

def run_oracle(n_qubits, marked_state):
    oracle = build_oracle(n_qubits, marked_state)
    
    qc = QuantumCircuit(n_qubits)
    qc.h(range(n_qubits))

    # Append circuit-as-oracle
    qc.compose(oracle, inplace=True)

    qc.measure_all()

    simulator = AerSimulator()
    result = simulator.run(qc).result()
    counts = result.get_counts()

    plot_histogram(counts)
    plt.show()

    return counts

if __name__=="__main__":
    print(run_oracle(3, "101"))
    