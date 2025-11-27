from qiskit import QuantumCircuit, QuantumRegister, ClassicalRegister
from qiskit_aer import AerSimulator
from qiskit.visualization import plot_bloch_multivector
from qiskit.quantum_info import DensityMatrix, partial_trace
import matplotlib.pyplot as plt

class TeleportationVisualiser:
    def __init__(self):
        # Initialise registers, circuit and simulator
        self.q = QuantumRegister(3, "q")
        self.c0 = ClassicalRegister(1, "c0")
        self.c1 = ClassicalRegister(1, "c1")

        self.circuit = QuantumCircuit(self.q, self.c0, self.c1)
        self.sim = AerSimulator()
        self.teleported_dm = None

    def prepare_unknown_state(self):
        # Prepare state to be teleported (example |+>)
        self.circuit.h(self.q[0])
    
    def create_bell_pair(self):
        # Create a Bell pair between qubits 1 and 2
        self.circuit.h(self.q[1])
        self.circuit.cx(self.q[1], self.q[2])

    def bell_measurement(self):
        # Perform Bell measurement on qubits 0 and 1
        self.circuit.cx(self.q[0], self.q[1])
        self.circuit.h(self.q[0])
        self.circuit.measure(self.q[0], self.c0)
        self.circuit.measure(self.q[1], self.c1)

    def apply_corrections(self):
        # Apply conditional X/Z corrections depending on classical results
        with self.circuit.if_test((self.c1, 1)):
            self.circuit.z(self.q[2])
        
        with self.circuit.if_test((self.c0, 1)):
            self.circuit.x(self.q[2])

    def simulate(self):
        # Save simulator's final state
        self.circuit.save_statevector()
        result = self.sim.run(self.circuit).result()
        statevec = result.data(0)["statevector"]

        # Convert to density matrix
        dm = DensityMatrix(statevec)

        # Keep qubit 2 (trace out qubits 0 and 1)
        self.teleported_dm = partial_trace(dm, [0,1])

    def plot_bloch(self, filename="teleported_bloch.png"):
        if self.teleported_dm is None:
            raise ValueError("Run simulate() before plotting.")
        
        fig = plot_bloch_multivector(self.teleported_dm)
        fig.savefig(filename)
        print(f"Saved as {filename}")
        plt.show()

    def run_all(self):
        # Execute entire teleportation protocol
        self.prepare_unknown_state()
        self.create_bell_pair()
        self.bell_measurement()
        self.apply_corrections()
        self.simulate()
        self.plot_bloch()

# Usage
if __name__=="__main__":
    tv = TeleportationVisualiser()
    tv.run_all()