from qiskit import QuantumCircuit, transpile
from qiskit_aer import AerSimulator
from qiskit.visualization import plot_histogram
import matplotlib.pyplot as plt

def quantum_circuit_optimiser():
    # We'll intentionally create a quantum circuit with some redundant or unnecessary gates (e.g., consecutive Hadamard gates, a CNOT followed by the inverse of the same CNOT). These kinds of operations are good candidates for optimisation.
    
    qc = QuantumCircuit(3)

    # Redundant gates - consecutive Hadamard gates and a CNOT followed by its inverse

    qc.h(0)
    qc.h(0) # Redundand Hadamard gate
    qc.cx(0,1)
    qc.cx(0,1) # Redundant CNOT gate, applying same CNOT again
    qc.h(2)
    qc.h(2) # Redundant Hadamard gate

    qc.measure_all()

    print("\nOriginal Circuit: ")
    print(qc)

    counts = run_simulator(qc)

    plot_histogram(counts)
    plt.show()

def run_simulator(qc):
    # Apply transpile with optimisation level 3
    qc_optimised = transpile(qc, basis_gates=['u1','u2','u3','cx'], optimization_level=3)

    print("\nOptimised Circuit: ")
    print(qc_optimised)

    simulator = AerSimulator()

    result = simulator.run(qc_optimised).result()
    counts = result.get_counts()

    print("\nMeasurement results: ")
    print(counts)

    return counts

if __name__=="__main__":
    quantum_circuit_optimiser()