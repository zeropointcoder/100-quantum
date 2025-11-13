from qiskit import QuantumCircuit, transpile
from qiskit_aer import AerSimulator
from qiskit.visualization import plot_histogram
import matplotlib.pyplot as plt
import os

def quantum_measurement_simulation(num_shots=1000):
    # Create output dir for results if it doesn't exist
    os.makedirs("images", exist_ok=True)

    # Create 1-qubit quantum circuit with 1 classical bit
    qc = QuantumCircuit(1,1)

    # Apply Hadamard gate to create a superposition: 
    # |0> -> (|0> + |1>)/√2
    qc.h(0)
    
    # Measure the qubit
    qc.measure(0,0)

    # Initialise AerSimulator backend
    simulator = AerSimulator(method="automatic")

    # Transpile circuit for the simulator
    compiled_circuit = transpile(qc, simulator)

    # Run simulation
    job = simulator.run(compiled_circuit, shots=num_shots)
    result = job.result()
    counts = result.get_counts()

    print("Measurement results: ", counts)

    # Plot histogram of measurement outcomes
    plot_histogram(counts)
    plt.title("Quantum measurement simulation (Hadamard superposition)")
    plt.savefig("images/measurement_histogram.png")
    plt.show()

if __name__=="__main__":
    print("Running Quantum measurement simulation using Qiskit simulation...")
    quantum_measurement_simulation()
