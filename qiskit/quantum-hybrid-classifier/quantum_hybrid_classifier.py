import numpy as np
from qiskit import QuantumCircuit, transpile
from qiskit.circuit import Parameter
from qiskit_aer import AerSimulator
from sklearn.datasets import make_blobs
import matplotlib.pyplot as plt
from qiskit.quantum_info import SparsePauliOp

# synthetic dataset
X, y = make_blobs(n_samples=20, centers=2, n_features=2, random_state=6)
y = 2*y - 1 # convert to {-1,+1}

plt.figure()
plt.scatter(X[:,0], X[:,1], c=y, cmap="coolwarm", edgecolors="k")
plt.title("Training Data")
plt.show()

# Define a simple parametarised quantum circuit
x0, x1 = Parameter('x0'), Parameter('x1')
theta = Parameter('θ')
observable = SparsePauliOp('Z')

qc = QuantumCircuit(1)
qc.ry(x0, 0)
qc.rz(x1, 0)
qc.ry(theta, 0)
qc.save_expectation_value(operator=observable, qubits=[0], label="exp_val")

# Simular backend
backend = AerSimulator()

def quantum_forward(x, theta_val):
    """Run circuit and return expectation value"""
    bound_circ = qc.assign_parameters({x0: x[0], x1: x[1], theta: theta_val})
    transpiled = transpile(bound_circ, backend)
    result = backend.run(transpiled).result()
    return np.real(result.data(0)["exp_val"])

# Training loop
theta_val = np.random.uniform(0, 2*np.pi)
lr = 0.2
epochs = 15

for epoch in range(epochs):
    grad = 0
    loss = 0
    for xi, yi in zip(X, y):
        fwd = quantum_forward(xi, theta_val)
        loss += (fwd -yi)**2

        # parameter-shift rule
        shift = np.pi / 2
        fwd_plus = quantum_forward(xi, theta_val + shift)
        fwd_minus = quantum_forward(xi, theta_val - shift)
        grad += ((fwd_plus-fwd_minus)/2)*2*(fwd-yi) # include factor 2

    theta_val -= lr*grad/len(X)
    print(f"Epoch {epoch+1:02d} | Loss: {loss/len(X):.4f} | θ: {theta_val:.3f}")

print("\nTrained θ =", theta_val)

# Prediction and accuracy
def predict(x):
    return np.sign(quantum_forward(x, theta_val))

preds = np.array([predict(xi) for xi in X])
acc = np.mean(preds == y)
print(f"\nTraining Accuracy: {acc*100:.2f}%")

# Decision boundary plot
xx, yy = np.meshgrid(
    np.linspace(X[:,0].min()-1, X[:,0].max() + 1, 100),
    np.linspace(X[:,1].min()-1, X[:,1].max() + 1, 100)
)

Z = np.array([predict([x,y]) for x,y in zip(xx.ravel(), yy.ravel())])
Z = Z.reshape(xx.shape)

plt.figure(figsize=(6,5))
plt.contourf(xx, yy, Z, cmap="coolwarm", alpha=0.3)
plt.scatter(X[:,0], X[:,1], c=y, cpmap="coolwarm", edgecolors="k")
plt.title("Quantum Classifier Decision Boundary")
plt.xlabel("Feature 1")
plt.ylabel("Feature 2")
plt.show()

# Output:
# This is a minimal 1-qubit quantum classifier. 
# Due to the limited expressivity of the circuit, the maximum achievable accuracy on this dataset is 75%.