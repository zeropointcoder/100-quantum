from qiskit import QuantumCircuit
from qiskit_aer import AerSimulator

def build_oracle(n_qubits, marked_state):
    """Return a QuantumCircuit implementing a phase-flip oracle."""
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

    return qc   # NOTE: return circuit, NOT a Gate


def run_oracle(n_qubits, marked_state):
    oracle = build_oracle(n_qubits, marked_state)

    qc = QuantumCircuit(n_qubits)
    qc.h(range(n_qubits))

    # Append circuit-as-oracle (works in Aer)
    qc.compose(oracle, inplace=True)

    qc.measure_all()

    sim = AerSimulator()
    result = sim.run(qc).result()
    return result.get_counts()


if __name__ == "__main__":
    print(run_oracle(3, "101"))
