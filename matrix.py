import copy


class Matrix:
    def __init__(self, argument):
        if type(argument) is list:
            self.size = (len(argument), len(argument[0]))
            self.values = argument
        elif type(argument) is tuple:
            self.size = argument
            self.values = [[0] * self.size[1] for _ in range(self.size[0])]

    def __add__(self, other):
        sum = Matrix((self.size[0], self.size[1]))
        for row in range(self.size[0]):
            for col in range(self.size[1]):
                sum.values[row][col] = self.values[row][col] + other.values[row][col]
        return sum

    def __sub__(self, other):
        difference = Matrix((self.size[0], self.size[1]))
        for row in range(self.size[0]):
            for col in range(self.size[1]):
                difference.values[row][col] = self.values[row][col] - other.values[row][col]
        return difference

    def __mul__(self, other):
        if type(other) is Matrix:
            product = Matrix((self.size[0], other.size[1]))
            for row in range(product.size[0]):
                for col in range(product.size[1]):
                    product.values[row][col] = 0
                    for i in range(self.size[1]):
                        product.values[row][col] += self.values[row][i] * other.values[i][col]
            return product
        else:
            product = self.duplicate()
            for row in range(product.size[0]):
                for col in range(product.size[1]):
                    product.values[row][col] *= other
            return product

    def duplicate(self):
        duplicate = Matrix(self.size)
        duplicate.values = copy.deepcopy(self.values)
        return duplicate

    def get_diagonal_matrix(self):
        diagonal = Matrix(self.size)
        diagonal_values = [self.values[i][i] for i in range(self.size[0])]
        for index, value in enumerate(diagonal_values):
            diagonal.values[index][index] = value
        return diagonal

    # hollow matrix combines non-zero values of lower triangular matrix and upper triangular matrix
    def get_hollow_matrix(self):
        hollow = self.duplicate()
        for i in range(hollow.size[0]):
            hollow.values[i][i] = 0
        return hollow

    def get_lower_triangular_matrix(self):
        lower_triangular = Matrix(self.size)
        for row in range(self.size[0]):
            for col in range(row):
                lower_triangular.values[row][col] = self.values[row][col]
        return lower_triangular

    def get_upper_triangular_matrix(self):
        upper_triangular = Matrix(self.size)
        for row in range(self.size[0]):
            for col in range(row + 1, self.size[1]):
                upper_triangular.values[row][col] = self.values[row][col]
        return upper_triangular


def band_matrix(size, values):
    band = Matrix(size)
    for offset, value in enumerate(values):
        for i in range(band.size[0]):
            if 0 <= i + offset < band.size[0]:
                band.values[i][i + offset] = value
            if 0 <= i - offset < band.size[0]:
                band.values[i][i - offset] = value
    return band


def identity_matrix(size):
    identity = Matrix(size)
    for i in range(size[0]):
        identity.values[i][i] = 1
    return identity


def ones_vector(size):
    ones = Matrix(size)
    ones.values = [[1] * size[1] for _ in range(size[0])]
    return ones
