from qiskit import QuantumCircuit, transpile
from qiskit_aer import AerSimulator
from qiskit.visualization import plot_histogram
import matplotlib.pyplot as plt

def run_x_gate():
    qc = QuantumCircuit(1,1)
    
    qc.x(0) # Apply X gate to flip |0> -> |1>

    qc.measure(0,0)

    simulator = AerSimulator()
    compiled_circuit = transpile(qc, simulator)
    result = simulator.run(compiled_circuit, shots=1024).result()
    counts = result.get_counts(qc)
    
    plot_histogram(counts)
    plt.show()

    print("Return result: ", counts)
    return counts

if __name__=="__main__":
    counts = run_x_gate()
    print("Measurement results: ", counts)