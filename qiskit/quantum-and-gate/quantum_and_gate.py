from qiskit import QuantumCircuit, transpile
from qiskit_aer import AerSimulator
from qiskit.visualization import plot_histogram
import matplotlib.pyplot as plt

def run_AND_gate():
    # Create a 3-qubit circuit
    qc = QuantumCircuit(3,1)
    print(qc)

    # Example input:
    # control qubit 0: |1>
    # control qubit 1: |1>
    # target qubit 2: |0>
    qc.x(0) # Set control 1 to |1>
    qc.x(1) # Set control 2 to |1>
    # target remains |0>

    # Apply Toffoli (CCX) gate
    qc.ccx(0,1,2)

    qc.measure(2,0)

    simulator = AerSimulator()
    compiled_circuit = transpile(qc, simulator)
    result = simulator.run(compiled_circuit, shots=1024).result()

    counts = result.get_counts()
    plot_histogram(counts)
    plt.show()
    
    print("Return result: ", counts)

    return counts

if __name__=="__main__":
    counts = run_AND_gate()
    print("Measurement results: ", counts)
