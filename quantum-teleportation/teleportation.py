# Theoretical Background:
# Quantum teleportation relies on three main steps:
    # 1. Entanglement Creation – Alice and Bob share an entangled Bell pair.
    # 2. Bell Measurement – Alice entangles her unknown qubit with her part of the Bell pair and measures.
    # 3. Classical Communication & Correction – Alice sends her results to Bob, who applies appropriate gates to recover the original state.
# Mathematically: ∣ψ⟩ = α∣0⟩ + β∣1⟩ is teleported to Bob using two classical bits and one shared entangled pair.

from qiskit import QuantumCircuit
from qiskit_aer import AerSimulator
from qiskit.visualization import plot_bloch_multivector, plot_histogram
from qiskit.quantum_info import Statevector
import matplotlib.pyplot as plt

# 1. Create 3 qubits (Alice's input, Alice's entangled qubit and Bob's entangled qubit)
qc = QuantumCircuit(3, 2)

# Inititialise Alice's qubit with some state |ψ⟩ = α|0⟩ + β|1⟩
qc.h(0) # example state: superposition
qc.barrier()

# 2. Create entanglement between qubits 1 and 2 (Bell pair)
qc.h(1)
qc.cx(1,2)
qc.barrier()

# 3. Alice performs Bell measurement on qubits 0 and 1
qc.cx(0,1)
qc.h(0)
qc.measure([0,1], [0,1])
qc.barrier()

# 4. Bob applies conditional operations based on Alice's measurements
qc.cx(1,2)
qc.cz(0,2)

# 5. Simulate using Aer simulator
simulator = AerSimulator()
job = simulator.run(qc, shots=1024)
result = job.result()
counts = result.get_counts()

# 5. Visualise results 
qc.draw('mpl')
plot_histogram(counts)
plt.show()