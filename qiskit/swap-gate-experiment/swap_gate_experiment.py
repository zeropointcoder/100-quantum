from qiskit import QuantumCircuit, transpile
from qiskit_aer import AerSimulator
from qiskit.visualization import plot_histogram
import matplotlib.pyplot as plt

def swap_gate_experiment():
    qc = QuantumCircuit(2,2) # Create the circuit

    # Prepare an initial non-symmetric state so swap is evident
    # |q0> = |1>, |q1> = |0>
    qc.x(0)

    print("\nBefore SWAP, circuit:")
    print(qc)

    # Apply SWAP gate
    qc.swap(0,1)

    # Measure
    qc.measure([0,1], [0,1])

    print("\nAfter SWAP, circuit:")
    print(qc)

    counts = run_simulator(qc)
    
    plot_histogram(counts)
    plt.show()

def run_simulator(qc):
    simulator = AerSimulator()
    compiled_circuit = transpile(qc, simulator)
    result = simulator.run(compiled_circuit, shots=1024).result()
    counts = result.get_counts()

    print("\nMeasurement results: ")
    print(counts)

    return counts

if __name__=="__main__":
    swap_gate_experiment()