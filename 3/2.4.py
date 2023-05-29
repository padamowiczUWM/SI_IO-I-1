import numpy as np

def step_function(x):
    return 1 if x >= 0 else 0

def perceptron_learn(X, y):
    w = np.zeros(X.shape[1])
    eta = 0.1
    n = 100

    for _ in range(n):
        for xi, yi in zip(X, y):
            update = eta * (yi - step_function(np.dot(xi, w)))
            w += update * xi

    return w

X_and = np.array([[0, 0], [0, 1], [1, 0], [1, 1]])
y_and = np.array([0, 0, 0, 1])
w_and = perceptron_learn(X_and, y_and)
print("Wagi dla funkcji AND:", w_and)

X_not = np.array([[0], [1]])
y_not = np.array([1, 0])
w_not = perceptron_learn(X_not, y_not)
print("Wagi dla funkcji NOT:", w_not)