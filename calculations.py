import matrix
import time
import math


def jacobi(A: matrix.Matrix, b: matrix.Matrix):
    D = matrix.from_diagonal_list(A.get_diagonal_list())
    H = A.get_hollow_matrix()
    r = matrix.Matrix(b.size)
    r.data = [[1] * r.size[1] for _ in range(r.size[0])]
    norm_res_j = []
    second_term = forward_substitution(D, b)
    start = time.time()
    while norm(res(A, r, b)) > 10 ** -9:
        norm_res_j.append(norm(res(A, r, b)))
        first_term = forward_substitution(D * -1, H * r)
        r = first_term + second_term
    time_j = time.time() - start
    return norm_res_j, time_j


def gauss_seidel(A: matrix.Matrix, b: matrix.Matrix):
    D = matrix.from_diagonal_list(A.get_diagonal_list())
    L = A.get_lower_triangular_matrix()
    U = A.get_upper_triangular_matrix()
    r = matrix.Matrix(b.size)
    r.data = [[1] * r.size[1] for _ in range(r.size[0])]
    first_term = (D + L) * -1
    second_term = forward_substitution(D + L, b)
    norm_res_gs = []
    start = time.time()
    while norm(res(A, r, b)) > 10 ** -9:
        norm_res_gs.append(norm(res(A, r, b)))
        r = forward_substitution(first_term, U * r) + second_term
    time_gs = time.time() - start
    return norm_res_gs, time_gs


def lu_factorization(A: matrix.Matrix):
    U = A.copy()
    L = matrix.Matrix(A.size)
    for i in range(A.size[0]):
        L.data[i][i] = 1
    for i in range(A.size[0]):
        print(i)
        for j in range(i + 1, A.size[0]):
            L.data[j][i] = U.data[j][i] / U.data[i][i]
            for k in range(j, A.size[0]):
                U.data[j][k] = U.data[j][k] - L.data[j][i] * U.data[i][k]
    return L, U


def lu(A: matrix.Matrix, b: matrix.Matrix):
    start = time.time()
    L, U = lu_factorization(A)
    y = forward_substitution(L, b)
    # result
    x = backward_substitution(U, y)
    time_lu = time.time() - start
    return time_lu


# A must be a lower triangular matrix with non-zero diagonal elements
def forward_substitution(A: matrix.Matrix, b: matrix.Matrix):
    x = matrix.Matrix(b.size)
    for row in range(A.size[0]):
        sum = 0
        for col in range(row):
            sum += x.data[col][0] * A.data[row][col]
        x.data[row][0] = (b.data[row][0] - sum) / A.data[row][row]
    return x


# A must be an upper triangular matrix with non-zero diagonal elements
def backward_substitution(A: matrix.Matrix, b: matrix.Matrix):
    x = matrix.Matrix(b.size)
    for row in range(A.size[0]-2, -1, -1):
        sum = 0
        for col in range(row-2, -1, -1):
            sum += x.data[col][0] * A.data[row][col]
        x.data[row][0] = (b.data[row][0] - sum) / A.data[row][row]
    return x


def norm(vector):
    sum_of_squares = 0
    for row in range(vector.size[0]):
        sum_of_squares += vector.data[row][0] ** 2
    return math.sqrt(sum_of_squares)


def res(A, r, b):
    return A * r - b
