import math
import time

import matrix
import solvers


# Filip Szweda 184738

def zadanie_A():
    a1 = 5 + 7
    a2 = -1
    a3 = -1
    N = 938
    A = matrix.Matrix((N, N))
    A.band((a1, a2, a3))

    f = 4
    b = [math.sin(i * (f + 1)) for i in range(N)]

    return A, b


def zadanieB(A, b):
    start = time.time()
    iterationsJ = solvers.Jacobi(A, b)
    timeJ = time.time() - start

    start = time.time()
    iterationsGS = solvers.GaussSeidel(A, b)
    timeGS = time.time() - start

    return iterationsJ, iterationsGS, timeJ, timeGS


def zadanieC(b):
    a1 = 3
    a2 = -1
    a3 = -1
    N = 938
    A = matrix.Matrix((N, N))
    A.band((a1, a2, a3))

    iterationsJ = solvers.Jacobi(A, b)

    iterationsGS = solvers.GaussSeidel(A, b)


if __name__ == '__main__':
    A, b = zadanie_A()
    iterationsJ, iterationsGS, timeJ, timeGS = zadanieB(A, b)
    zadanieC(b)
