from qiskit import QuantumCircuit
from qiskit_aer import AerSimulator
from qiskit.visualization import plot_histogram
import matplotlib.pyplot as plt

class SimpleQuantumGame:
    def __init__(self):
        self.circuit = QuantumCircuit(1,1)
        print("\nWelcome to the Simple Quantum Game!")
        print("\nYour qubit begins in the state |0>.")
        print("\nAvailable moves X, H, Z")
        print("\nType DONE when you have finished choosing your moves\n")

    def start(self):
        while(True):
            move = input("\nEnter your move (X, H, Z or DONE): ").strip().lower()

            if(move == "done"):
                break

            elif(move == "x"):
                self.circuit.x(0)
                print("\nApplied: X Gate")
            elif(move == "h"):
                self.circuit.h(0)
                print("\nApplied: H Gate")
            elif(move == "z"):
                self.circuit.z(0)
                print("\nApplied Z Gate")
            else:
                print("\nInvalid input. Please choose X, H, Z or DONE.")

        self.finish_game()

    def finish_game(self):
        print("\nFinalising your circuit and measuring the qubit..\n")
        self.circuit.measure(0,0)

        simulator = AerSimulator()
        result = simulator.run(self.circuit).result()
        counts = result.get_counts()

        print("\nMeasurement result: ", counts)

        if counts.get("1", 0) > counts.get("0",0):
            print("\n⭐ You win! The qubit collapsed to |1> more often.")
        else:
            print("\n❌ You lose! The qubit collapsed to |0> more often.")
        
        print("\nThanks for playing!\n")

        plot_histogram(counts)
        plt.show()

# Run the game if executed directly
if __name__=="__main__":
    game = SimpleQuantumGame()
    game.start()