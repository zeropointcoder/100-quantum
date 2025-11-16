# Import required libraries
from qiskit import Aer, QuantumCircuit, execute
from qiskit.visualization import plot_bloch_multivector

# Create a Quantum Circuit with one qubit
qc = QuantumCircuit(1)

# Apply a rotation around the X-axis (rx) by 90 degrees (pi/2 radians)
qc.rx(3.14/2, 0)

# Apply a rotation around the Y-axis (ry) by 45 degrees (pi/4 radians)
qc.ry(3.14/4, 0)

# Apply a rotation around the Z-axis (rz) by 30 degrees (pi/6 radians)
qc.rz(3.14/6, 0)

# Draw the circuit
print(qc.draw())

# Use the AerSimulator to simulate the quantum circuit
simulator = Aer.get_backend('statevector_simulator')

# Execute the circuit on the simulator
result = execute(qc, simulator).result()

# Get the final state vector
statevector = result.get_statevector()

# Plot the Bloch sphere visualization
plot_bloch_multivector(statevector)
