from qiskit import QuantumCircuit, transpile
from qiskit_aer import AerSimulator
from qiskit.visualization import plot_histogram
import matplotlib.pyplot as plt

def quantum_random_bit():
    """
    Generates one truly random bit (0 and 1) using quantum superposition    
    """
    # 1. Create a quantum circuit with 1 qubit and 1 classical bit
    qc = QuantumCircuit(1,1)
    # 2. Apply a Hadamard gate to put the qubit in superposition
    qc.h(0)
    # 3. Measure the qubit
    qc.measure(0,0)
    # 4. Initialise the AerSimulator
    simulator = AerSimulator()
    # 5. Transpile the circuit for the simulator
    compiled_circuit = transpile(qc, simulator)
    # 6. Run the simulation (1 shot - 1 random outcome)
    result = simulator.run(compiled_circuit, shots=1).result()
    # 7. Extract the measurement result
    counts = result.get_counts()
    bit = int(list(counts.keys())[0])
    return bit

def quantum_random_number(num_bits=8):
    """
    Generates a random integer composed of 'num_bits' quantum bits
    """
    bits = [str(quantum_random_bit()) for _ in range(num_bits)]
    bitstring = ''.join(bits)
    number = int(bitstring, 2)
    return number, bitstring

if __name__ == "__main__":
    num_bits = 8
    number, bitstring = quantum_random_number(num_bits)
    print(f"Quantum random {num_bits}-bit number: {number} (bits: {bitstring})")
    
# Example output:
# `python3 quantum_random_number_generator.py`
# Quantum random 8-bit number: 183 (bits: 10110111)