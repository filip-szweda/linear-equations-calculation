import matrix
import time
import math


def jacobi(A: matrix.Matrix, b: matrix.Matrix):
    D = matrix.from_diagonal_list(A.get_diagonal_list())
    L = A.get_lower_triangular_matrix()
    U = A.get_upper_triangular_matrix()
    # LU = A.get_hollow_matrix() is quicker
    N = len(A.data[0])
    r = matrix.Matrix([[1] for _ in range(N)])

    start = time.time()
    res = A * r - b
    iterations_j = 1
    while norm(res) > 10 ** -9:
        first_term = forward_substitution(D, (L + U) * r) * -1
        # first_term = forward_substitution(D, LU * r) * -1 is quicker
        second_term = forward_substitution(D, b)
        r = first_term + second_term
        res = A * r - b
        iterations_j += 1
    time_j = time.time() - start

    return iterations_j, time_j


def gauss_seidel(A: matrix.Matrix, b: matrix.Matrix):
    D = matrix.from_diagonal_list(A.get_diagonal_list())
    L = A.get_lower_triangular_matrix()
    U = A.get_upper_triangular_matrix()
    N = len(A.data[0])
    r = matrix.Matrix([[1] for _ in range(N)])

    start = time.time()
    res = A * r - b
    iterations_gs = 1
    while norm(res) > 10 ** -9:
        print(norm(res))
        first_term = forward_substitution((D + L) * -1, U * r)
        second_term = forward_substitution(D + L, b)
        r = first_term + second_term
        res = A * r - b
        iterations_gs += 1
    time_gs = time.time() - start

    return iterations_gs, time_gs


# A must be a lower triangular matrix with non-zero diagonal elements
def forward_substitution(A: matrix.Matrix, b: matrix.Matrix):
    x = matrix.Matrix(b.size)
    x.data[0][0] = b.data[0][0] / A.data[0][0]
    for row in range(1, A.size[0]):
        dividend = b.data[row][0]
        for col in range(row):
            dividend -= x.data[col][0] * A.data[row][col]
        x.data[row][0] = dividend / A.data[row][row]
    return x


def norm(vector):
    sum_of_squares = 0
    for row in range(vector.size[0]):
        sum_of_squares += vector.data[row][0] ** 2
    return math.sqrt(sum_of_squares)
