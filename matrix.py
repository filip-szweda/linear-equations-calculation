import copy


class Matrix:
    size: tuple[int, int]
    data: list[list]

    def __init__(self, arg):
        if type(arg) is tuple:
            self.size = arg
            self.data = [[0] * self.size[1] for _ in range(self.size[0])]
        elif type(arg) is list:
            self.size = (len(arg), len(arg[0]))
            self.data = arg

    def set_band(self, values: tuple):
        for offset, value in enumerate(values):
            for i in range(self.size[0]):
                if 0 <= i + offset < self.size[0]:
                    self.data[i][i + offset] = value
                if 0 <= i - offset < self.size[0]:
                    self.data[i][i - offset] = value

    def get_diagonal_list(self):
        return [self.data[i][i] for i in range(self.size[0])]

    # hollow combines non-zero values of lower triangular matrix and upper triangular matrix
    def get_hollow_matrix(self):
        hollow = self.copy()
        for i in range(hollow.size[0]):
            hollow.data[i][i] = 0
        return hollow

    def get_lower_triangular_matrix(self):
        lower_triangular = Matrix(self.size)
        for row in range(self.size[0]):
            for col in range(row):
                lower_triangular.data[row][col] = self.data[row][col]
        return lower_triangular

    def get_upper_triangular_matrix(self):
        upper_triangular = Matrix(self.size)
        for row in range(self.size[0]):
            for col in range(row + 1, self.size[1]):
                upper_triangular.data[row][col] = self.data[row][col]
        return upper_triangular

    def copy(self):
        result = Matrix(self.size)
        result.data = copy.deepcopy(self.data)
        return result

    def __add__(self, other):
        result = Matrix((self.size[0], self.size[1]))
        for row in range(self.size[0]):
            for col in range(self.size[1]):
                result.data[row][col] = self.data[row][col] + other.data[row][col]
        return result

    def __sub__(self, other):
        result = Matrix((self.size[0], self.size[1]))
        for row in range(self.size[0]):
            for col in range(self.size[1]):
                result.data[row][col] = self.data[row][col] - other.data[row][col]
        return result

    def __mul__(self, other):
        if type(other) is Matrix:
            result = Matrix((self.size[0], other.size[1]))
            for row in range(result.size[0]):
                for col in range(result.size[1]):
                    result.data[row][col] = 0
                    for x in range(self.size[1]):
                        result.data[row][col] += self.data[row][x] * other.data[x][col]
            return result
        else:
            result = self.copy()
            for row in range(result.size[0]):
                for col in range(result.size[1]):
                    result.data[row][col] *= other
            return result


def from_diagonal_list(diagonal_list: list):
    diagonal_matrix = Matrix((len(diagonal_list), len(diagonal_list)))
    for index, value in enumerate(diagonal_list):
        diagonal_matrix.data[index][index] = value
    return diagonal_matrix
