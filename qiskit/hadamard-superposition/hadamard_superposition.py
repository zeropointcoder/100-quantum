# Hadamard single qubit superposition

from qiskit import QuantumCircuit
from qiskit_aer import AerSimulator
from qiskit.visualization import plot_histogram, plot_bloch_multivector
from qiskit.quantum_info import Statevector
import matplotlib.pyplot as plt

# Create a quantum circuit with 1 qubit and 1 classical bit
qc = QuantumCircuit(1,1)

# Apply a Hadamard gate to put the qubit into superposition 
qc.h(0)

# Visualise the circuit
print("Quantum circuit: ")
print(qc)

# Visualise the state on the Bloch sphere (BEFORE MEASUREMENT)
state = Statevector.from_instruction(qc)
plot_bloch_multivector(state)
plt.title("State vector on the Bloch Sphere (superposition)")
plt.show()

# Measure the qubit
qc.measure(0,0)

# Initialise the simulator
simulator = AerSimulator()

# Run the simulator
job = simulator.run(qc, shots=1024)
result = job.result()

# Get and plot results
counts = result.get_counts()
print("\nMeasurement results: ", counts)

plot_histogram(counts)
plt.title("Quantum superposition measurement results: ")
plt.show()