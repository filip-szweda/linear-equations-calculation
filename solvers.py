import matrix
import time
import math


def jacobi(A: matrix.Matrix, b: matrix.Matrix):
    N = len(A.data[0])
    D = matrix.from_diagonal_list(A.get_diagonal_list())
    LU = A.get_hollow_matrix()
    r = matrix.Matrix([[1] for _ in range(N)])
    start = time.time()
    res = A * r - b
    iterations_j = 1
    while norm(res) > 10 ** -9:
        first_term = forward_substitution(D, LU * r) * -1
        second_term = forward_substitution(D, b)
        r = first_term + second_term
        res = A * r - b
        iterations_j += 1
    time_j = time.time() - start
    return iterations_j, time_j


def gauss_seidel(A: matrix.Matrix, b: matrix.Matrix):
    start = time.time()
    time_gs = time.time() - start


# A is a lower triangular matrix with non-zero diagonal elements
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
