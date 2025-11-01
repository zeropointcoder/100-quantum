from qiskit import QuantumCircuit
from qiskit_aer import AerSimulator
from qiskit.visualization import plot_histogram
import matplotlib.pyplot as plt

# 1. Create quantum qubit with 1 qubit and 1 classical qubit
qc = QuantumCircuit(1,1)

# 2. Add a Hadamard gate to create superposition
qc.h(0) # This puts qubit 0 into superposition state (|0> + |1>)/√2

# 3. Measure the cubit
qc.measure(0,0)

# 4. Simulate the circuit using Aer simulator
simulator = AerSimulator()
job = simulator.run(qc, shots=1000)
result = job.result()
counts = result.get_counts()

# 5. Output results : 
# >> python3 quantum_basic_circuits.py
print('Measurement results: ', counts) 

# 6. Visualise the circuit and results  
qc.draw('mpl')
plot_histogram(counts)
plt.show()