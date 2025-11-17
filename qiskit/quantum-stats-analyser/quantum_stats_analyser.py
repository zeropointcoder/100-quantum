from qiskit import QuantumCircuit, transpile
from qiskit_aer import AerSimulator
from qiskit.visualization import plot_histogram
import matplotlib.pyplot as plt

def quantum_stats_analyser():
    # Create 2-qubit quantum circuit
    qc = QuantumCircuit(2,2)

    # Apply Hadamard gate to the first qubit
    qc.h(0)

    # Apply a CNOT gate with the first qubit as control and the second as target 
    qc.cx(0,1)

    # Measure the qubits
    qc.measure([0,1], [0,1])

    # Visualise the circuit
    print("Quantum Circuit:")
    print(qc.draw())

    # Create simulator
    simulator = AerSimulator()
    compiled_circuit = transpile(qc, simulator)
    result = simulator.run(compiled_circuit, shots=1024).result()
    counts = result.get_counts()

    print("Measurement Results: ", counts)

    # Calculate and print probabilities of each outcome
    total_shots = sum(counts.values())
    probabilities = {outcome: count/total_shots for outcome, count in counts.items()}
    
    print("\nMeasurement Probabilities:")
    for outcome, probability in probabilities.items():
        print(f"Outcome {outcome}: Probability {probability:.4f}")

    plot_histogram(counts)
    plt.show()

if __name__=="__main__":
    quantum_stats_analyser()