from qiskit import QuantumCircuit, transpile
from qiskit_aer import AerSimulator
from qiskit.visualization import plot_histogram
import matplotlib.pyplot as plt

def make_oracle(case: str):
    """
    case = "constant0", "constant1" or "balanced"
    """
    qc = QuantumCircuit(2)

    if case == "constant0":
        # f(x) = 0 -> do nothing
        pass

    elif case == "constant1":
        # f(x) = 1 -> flip output qubit
        qc.x(1)

    elif case == "balanced":
        # f(x) = x -> CNOT from input to output
        qc.cx(0,1)

    else:
        raise ValueError("Unknown oracle case.")
    
    return qc

# Deutsch Algorithm Circuit
def deutsch(case: str):
    
    oracle = make_oracle(case)
    qc = QuantumCircuit(2,1)

    #Initialise |1> on the output qubit
    qc.x(1)

    # Hadamards before oracle
    qc.h([0,1])

    print("Original Circuit: \n")
    print(qc)

    # Apply oracle
    qc.compose(oracle, inplace=True)

    # Hadamard on input qubit
    qc.h(0)

    # Measure input
    qc.measure(0,0)

    counts = simulate(qc)

    plot_histogram(counts)
    plt.show()

def simulate(qc):
    simulator = AerSimulator()
    result = simulator.run(qc).result()
    counts = result.get_counts()

    print("Measurement result: \n")
    print(counts)

    return counts

if __name__=="__main__":
    deutsch("balanced")