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
    b = matrix.Matrix([[math.sin(i * (f + 1))] for i in range(1, N+1)])

    return A, b


def zadanie_b(A: matrix.Matrix, b: matrix.Matrix):
    norm_res_j, time_j = solvers.jacobi(A, b)
    norm_res_gs, time_gs = solvers.gauss_seidel(A, b)
    return norm_res_j, time_j, norm_res_gs, time_gs


def zadanie_c(b: matrix.Matrix):
    a1 = 3
    a2 = -1
    a3 = -1
    N = 938
    A = matrix.Matrix((N, N))
    A.set_band((a1, a2, a3))

    # both methods diverge
    norm_res_j, _ = solvers.jacobi(A, b)
    norm_res_gs, _ = solvers.gauss_seidel(A, b)


if __name__ == '__main__':
    A, b = zadanie_a()
    norm_res_j, time_j, norm_res_gs, time_gs = zadanie_b(A, b)
    print("Iterations (Jacobi): " + str(len(norm_res_j)) + ", Time (Jacobi, in seconds): " + str(time_j))
    print("Iterations (Gauss-Seidl): " + str(len(norm_res_gs)) + ", Time (Gauss-Seidl, in seconds): " + str(time_gs))
    zadanie_c(b)
