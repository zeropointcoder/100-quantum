from qiskit import QuantumCircuit, transpile
from qiskit_aer import AerSimulator
from qiskit_aer.noise import NoiseModel, pauli_error
from qiskit.visualization import plot_histogram
import matplotlib.pyplot as plt

# Bit-flip probability
def bitflip_error_simulation():
    
    p = 0.2 # 20% flip

    # Create a noise model with a bit-flip error on the qubit
    bit_flip = pauli_error([('X', p), ('I', 1-p)])
    noise_model = NoiseModel()
    # Apply on idle ('id') or other chosen operations
    noise_model.add_all_qubit_quantum_error(bit_flip, ['id'])
    
    qc = QuantumCircuit(1,1) # Build a simple circuit
    qc.x(0) # Prepare \1>
    qc.id(0) # Apply an id gate to attach noise
    qc.measure(0,0)

    print(qc)

    counts = run_simulator(qc, noise_model)

    plot_histogram(counts)
    plt.show()

# Simulate
def run_simulator(qc, noise_model):
    simulator = AerSimulator(noise_model=noise_model)
    result = simulator.run(qc, shots=2000).result()
    counts = result.get_counts()

    print("\nMeasurement result: ")
    print(counts)

    return counts

if __name__=="__main__":
    bitflip_error_simulation()