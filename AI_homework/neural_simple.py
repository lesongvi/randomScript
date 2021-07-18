## Backup: https://notevn.com/simpleNeural

J = True
import numpy as A


def C(x, deriv=False):
    if deriv == J:
        return x * (1 - x)
    return 1 / (1 + A.exp(-x))


F = A.array([[0, 0, 1], [0, 1, 1], [1, 0, 1], [1, 1, 1]])
G = A.array([[0, 0, 1, 1]]).T
A.random.seed(1)
D = 2 * A.random.random((3, 1)) - 1
for iter in range(10000):
    E = F
    B = C(A.dot(E, D))
    H = G - B
    I = H * C(B, J)
    D += A.dot(E.T, I)
print B
