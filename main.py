import math

import matrix
import methods


# Filip Szweda 184738

def zadanie_a():
    a1 = 5 + 7
    a2 = -1
    a3 = -1
    N = 938
    A = matrix.band_matrix((N, N), (a1, a2, a3))
    f = 4
    b = matrix.Matrix([[math.sin(i * (f + 1))] for i in range(N)])
    return A, b


def zadanie_b(A, b):
    norm_res_j, time_j = methods.jacobi(A, b)
    norm_res_gs, time_gs = methods.gauss_seidel(A, b)
    return norm_res_j, time_j, norm_res_gs, time_gs


def zadanie_c(b):
    a1 = 3
    a2 = -1
    a3 = -1
    N = 938
    A = matrix.band_matrix((N, N), (a1, a2, a3))
    # both methods diverge
    norm_res_j, _ = methods.jacobi(A, b)
    norm_res_gs, _ = methods.gauss_seidel(A, b)


def zadanie_d(b):
    a1 = 3
    a2 = -1
    a3 = -1
    N = 938
    A = matrix.band_matrix((N, N), (a1, a2, a3))
    norm_res_lu, time_lu = methods.lu(A, b)
    return norm_res_lu, time_lu


if __name__ == '__main__':
    A, b = zadanie_a()

    norm_res_j, time_j, norm_res_gs, time_gs = zadanie_b(A, b)
    print("[Jacobi] Iterations: " + str(len(norm_res_j)) + ", Time (in seconds): " + str(time_j))
    print("[Gauss-Seidl] Iterations: " + str(len(norm_res_gs)) + ", Time (in seconds): " + str(time_gs))

    zadanie_c(b)

    norm_res_lu, time_lu = zadanie_d(b)
    print("[LU] Norm from residuum: " + str(norm_res_lu) + ", Time (in seconds): " + str(time_lu))
