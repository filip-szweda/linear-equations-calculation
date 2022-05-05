import time

import matrix
import helpers


def jacobi(A, b):
    D = A.get_diagonal_matrix()
    H = A.get_hollow_matrix()
    r = matrix.ones_vector(b.size)
    norm_res_j = []
    second_term = helpers.forward_substitution(D, b)
    start = time.time()
    while helpers.norm(helpers.residuum(A, r, b)) > 10 ** -9:
        norm_res_j.append(helpers.norm(helpers.residuum(A, r, b)))
        first_term = helpers.forward_substitution(D * -1, H * r)
        r = first_term + second_term
    time_j = time.time() - start
    return norm_res_j, time_j


def gauss_seidel(A, b):
    D = A.get_diagonal_matrix()
    L = A.get_lower_triangular_matrix()
    U = A.get_upper_triangular_matrix()
    r = matrix.ones_vector(b.size)
    first_term = (D + L) * -1
    second_term = helpers.forward_substitution(D + L, b)
    norm_res_gs = []
    start = time.time()
    while helpers.norm(helpers.residuum(A, r, b)) > 10 ** -9:
        norm_res_gs.append(helpers.norm(helpers.residuum(A, r, b)))
        r = helpers.forward_substitution(first_term, U * r) + second_term
    time_gs = time.time() - start
    return norm_res_gs, time_gs


def lu(A, b):
    start = time.time()
    L, U = helpers.lu_factorization(A)
    y = helpers.forward_substitution(L, b)
    x = helpers.backward_substitution(U, y)
    print(x.values[0][0])
    print(x.values[x.size[0] - 1][x.size[1] - 1])
    norm_res_lu = helpers.norm(helpers.residuum(A, x, b))
    time_lu = time.time() - start
    return norm_res_lu, time_lu
