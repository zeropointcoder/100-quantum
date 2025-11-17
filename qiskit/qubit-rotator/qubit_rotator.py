from qiskit import QuantumCircuit, transpile
from qiskit_aer import AerSimulator
from qiskit.visualization import plot_histogram, plot_bloch_multivector
import matplotlib.pyplot as plt

def qubit_rotator():

    # Create quantum circuit with 1 qubit
    qc = QuantumCircuit(1)

    # Apply a rotation around X-axis by 90 degrees (pi/2 radians)
    qc.rx(3.14/2, 0)

    # Apply a rotation around Y-axis by 45 degrees (pi/4 radians)
    qc.ry(3.14/4, 0)

    # Apply a rotation around Z-axis by 30 degrees(pi/6 radians)
    qc.rz(3.14/6, 0)

    # Save the statevector so AerSimulator returns it
    qc.save_statevector()

    # Draw the circuit
    print(qc.draw())

    # Create simulator
    simulator = AerSimulator()
    compiled_circuit = transpile(qc, simulator)
    result = simulator.run(compiled_circuit).result()

    # Get the final state vector
    statevector = result.get_statevector()

    # Plot the Bloch Sphere Visualisation
    plot_bloch_multivector(statevector)
    plt.show()

if __name__=="__main__":
    qubit_rotator()