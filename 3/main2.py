def step(x):
    if x < 0:
        return 0
    else:
        return 1

def AND_perceptron(x1, x2):
    w1, w2, b = 1, 1, -1.5
    z = x1*w1 + x2*w2 + b
    y = step(z)
    return y

def NOT_perceptron(x):
    w, b = -1, 0.5
    z = x*w + b
    y = step(z)
    return y