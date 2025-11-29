import networkx as nx
import numpy as np
from qiskit.quantum_info import SparsePauliOp
from qiskit.circuit.library import QAOAAnsatz
from qiskit_aer.primitives import SamplerV2 as Sampler
from qiskit_aer import AerSimulator
from qiskit import transpile
from scipy.optimize import minimize
from qiskit.visualization import plot_histogram
import matplotlib.pyplot as plt

class QAOAMaxCutSolver:
    def __init__(self, graph, p=1, shots=512):
        self.graph = graph
        self.n = len(graph.nodes)
        self.p = p
        self.shots = shots
        self.H = self.maxcut_hamiltonian(graph)
        self.ansatz = QAOAAnsatz(cost_operator=self.H, reps=self.p)
        self.backend = AerSimulator()
        self.sampler = Sampler.from_backend(self.backend)

    def maxcut_hamiltonian(self, graph):
        """Build the Max-Cut Hamiltonian from the given graph."""
        paulis = []
        coeffs = []

        for u,v in graph.edges:
            paulis.append("I" * self.n); coeffs.append(0.5)
            z = ["I"] * self.n
            z[u] = "Z"; z[v] = "Z"
            paulis.append("".join(z)); coeffs.append(-0.5)
        
        return SparsePauliOp(paulis, coeffs)

    def energy(self, params):
        """Calculate the expected energy (cut) for the given QAOA parameters."""
        qc = self.ansatz.assign_parameters(params)

        # Transpile/decompose to basis gates for simulator
        qc_decomp = transpile(qc, self.backend)
        qc_decomp.measure_all()
        job = self.sampler.run([qc_decomp], shots=1024)
        res = job.result()
        pub = res[0]
        counts = pub.data.meas.get_counts()
        total = sum(counts.values())
        exp_cut = 0.0

        for bitstr, cnt in counts.items():
            prob = cnt / total
            assign = {i: int(bitstr[i]) for i in range(self.n)}
            cut = sum(1 for u, v in self.graph.edges if assign[u] != assign[v])
            exp_cut += prob * cut

            return -exp_cut # Minimise the negative cut -> maximise cut
    
    def solve(self):
        """Use COBYLA optimiser to find the optimal QAOA parameters."""
        x0 = np.random.rand(2 * self.p) * np.pi # Random initial parameters
        res = minimize(self.energy, x0, method='COBYLA')
        print("\nOptimal params:", res.x)
        print("\nEstimated expected max-cut:", -res.fun)

        return res.x # Return optimal parameters for final sampling

    def final_sampling(self, optimal_params):
        """Run the final QAOA circuit to sample the best bit-string."""
        qc = self.ansatz.assign_parameters(optimal_params)
        qc_decomp = transpile(qc, self.backend)
        qc_decomp.measure_all()
        job = self.sampler.run([qc_decomp], shots=1024)
        res = job.result()
        pub = res[0]
        counts = pub.data.meas.get_counts()

        plot_histogram(counts)
        plt.show()

        best = max(counts.items(), key=lambda kv: kv[1])[0]
        print("\nBest bit-string:", best)

        return best

    def cut_value(self, bitstr):
        """Calculate the cut value from the best bit-string."""
        assign = {i: int(bitstr[i]) for i in range(len(bitstr))}
        return sum(1 for u, v in self.graph.edges if assign[u] != assign[v])

# Usage
if __name__=="__main__":
    # Build a small-graph (for Max-Cut)
    G = nx.Graph()
    G.add_edges_from([(0, 1), (1, 2), (2, 3), (3, 0), (0, 2)])

    # Instantiate the solver class
    solver = QAOAMaxCutSolver(graph=G, p=1, shots=512)

    # Solve for the optimal parameters
    optimal_params = solver.solve()

    # Perform the final sampling to get the best bit-string
    best_bitstr = solver.final_sampling(optimal_params)

    # Calculate and print the cut value
    cut_val = solver.cut_value(best_bitstr)
    print(f"\nCut value: {cut_val} \n") # Corrected line