import math

import matrix
import solvers


# Filip Szweda 184738

def zadanie_a():
    a1 = 5 + 7
    a2 = -1
    a3 = -1
    N = 938
    A = matrix.Matrix((N, N))
    A.set_band((a1, a2, a3))

    f = 4
    b = matrix.Matrix([[math.sin(i * (f + 1))] for i in range(N)])

    return A, b


def zadanie_b(A: matrix.Matrix, b: matrix.Matrix):
    iterations_j, time_j = solvers.jacobi(A, b)
    # iterations_gs, time_gs = solvers.gauss_seidel(A, b)
    return iterations_j, time_j


def zadanie_c(b: matrix.Matrix):
    a1 = 3
    a2 = -1
    a3 = -1
    N = 938
    A = matrix.Matrix((N, N))
    A.set_band((a1, a2, a3))

    iterations_j, _ = solvers.jacobi(A, b)
    # iterations_gs, _ = solvers.gauss_seidel(A, b)


if __name__ == '__main__':
    A, b = zadanie_a()
    iterations_j, time_j = zadanie_b(A, b)
    print("Iterations (Jacobi): " + str(iterations_j) + ", Time (Jacobi, in seconds): " + str(time_j))
    zadanie_c(b)
