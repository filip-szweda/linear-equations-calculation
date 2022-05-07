import math

import matrix


# A must be a lower triangular matrix with non-zero diagonal elements
def forward_substitution(A, b):
    x = matrix.Matrix(b.size)
    for row in range(A.size[0]):
        sum = 0
        for col in range(row):
            sum += x.values[col][0] * A.values[row][col]
        x.values[row][0] = (b.values[row][0] - sum) / A.values[row][row]
    return x


# A must be an upper triangular matrix with non-zero diagonal elements
def backward_substitution(A, b):
    x = matrix.Matrix(b.size)
    for row in range(A.size[0] - 1, -1, -1):
        sum = 0
        for col in range(A.size[0] - 1, row - 1, -1):
            sum += x.values[col][0] * A.values[row][col]
        x.values[row][0] = (b.values[row][0] - sum) / A.values[row][row]
    return x


def norm(vector):
    sum_of_squares = 0
    for row in range(vector.size[0]):
        sum_of_squares += vector.values[row][0] ** 2
    return math.sqrt(sum_of_squares)


def residuum(A, r, b):
    return A * r - b


def lu_factorization(A):
    U = A.duplicate()
    L = matrix.identity_matrix(A.size)
    for i in range(A.size[0]):
        for j in range(i + 1, A.size[0]):
            L.values[j][i] = U.values[i][j] / U.values[i][i]
            for k in range(i, A.size[0]):
                U.values[j][k] -= L.values[j][i] * U.values[i][k]
    return L, U
