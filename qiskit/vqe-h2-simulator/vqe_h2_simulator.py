from __future__ import annotations
from dataclasses import dataclass

import numpy as np
from scipy.optimize import minimize

from qiskit import QuantumCircuit
from qiskit.circuit import ParameterVector
from qiskit.quantum_info import SparsePauliOp, Statevector

# Hard-coded H₂ Hamiltonian (2-qubit parity mapping)
def h2_hamiltonian() -> SparsePauliOp:
    coeffs = [
        -1.052373245772859,
        0.3979374248431802,
        -0.3979374248431802,
        -0.01128010425623538,
        0.18093119978423156,
        0.18093119978423156
    ]
    paulis = ["II", "ZI", "IZ", "ZZ", "XX", "YY"]
    return SparsePauliOp(paulis, coeffs)

# Ansatz circuit
class H2Ansatz:
    """Three-parameter ansatz for H₂."""

    def __init__(self):
        self.parameters = ParameterVector("θ", 3)

    def build(self) -> QuantumCircuit:
        qc = QuantumCircuit(2)
        θ = self.parameters

        qc.ry(θ[0], 0)
        qc.ry(θ[1], 1)
        qc.cx(0, 1)
        qc.ry(θ[2], 1)

        return qc
        
# VQE Solver
class H2VQESolver:
    """VQE implementation for Qiskit 2.2.3"""

    def __init__(self):
        self.hamiltonian = h2_hamiltonian()
        self.ansatz = H2Ansatz()
        self.circuit = self.ansatz.build()
    
    def expectation_value(self, params: np.ndarray) -> float:
        """Compute ⟨ψ(θ)| H |ψ(θ)⟩ using Statevector simulation."""
        bound = self.circuit.assign_parameters(dict(zip(self.ansatz.parameters, params)))
        state = Statevector.from_instruction(bound)
        return state.expectation_value(self.hamiltonian).real

    def run(self) -> float:
        print("\n\nRunning VQE (NumPy backend)..")

        x0 = np.random.uniform(0, 2 * np.pi, len(self.ansatz.parameters))

        result = minimize(
            self.expectation_value,
            x0,
            method="SLSQP",
            options={"maxiter": 300}
        )

        energy = result.fun

        print(f"\nGround-state energy: {energy:.12f} Hartree")
        return energy

# Usage
if __name__=="__main__":
    solver = H2VQESolver()
    energy = solver.run()

    print(f"\nFinal energy: {energy:.12f} Ha\n")