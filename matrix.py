class Matrix:
    size: tuple[int, int]
    data: list[list]

    def __init__(self, arg):
        if type(arg) is tuple:
            self.size = arg
            self.data = [[None] * self.size[1] for _ in range(self.size[0])]
        elif type(arg) is list:
            self.size = (len(arg), len(arg[0]))
            self.data = arg

    def diagonal(self, value):
        for index in range(self.size[0]):
            self.data[index][index] = value

    def band(self, values):
        for offset, value in enumerate(values):
            for index in range(self.size[0]):
                if 0 <= index + offset < self.size[0]:
                    self.data[index][index + offset] = value
                if 0 <= index - offset < self.size[0]:
                    self.data[index][index - offset] = value
