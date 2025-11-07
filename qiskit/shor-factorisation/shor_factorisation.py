from qiskit import QuantumCircuit
from qiskit_aer import AerSimulator
from qiskit_algorithms import Shor

# The backend for simulation
backend = AerSimulator()

# Create a Shor's algorithm instance
shor = Shor()

# Number to factor
N = 15

# Run Shor's algorithm
result = shor.factorize(N, backend=backend)

# Show result
print(f"Factors of {N}: {result.factors}")
