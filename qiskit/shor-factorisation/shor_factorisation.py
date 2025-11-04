from qiskit import QuantumCircuit
from qiskit_aer import AerSimulator
from qiskit_algorithms import Shor
from qiskit.utils import QuantumInstance

N = 15 # choose a small number only 

simulator = AerSimulator() # simulate

qi = QuantumInstance(backend=simulator) # create a QuantumInstance for the simulator

shor = Shor(QuantumInstance=qi) # initialise Shor's algorithm

result = shor.factor(N) # run the algorithm

print(f"Factors of {N}: {result.factors}")