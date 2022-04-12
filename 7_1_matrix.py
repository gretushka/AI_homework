class Matrix:
    matrix = []

    def __init__(self, matrix):
        for row in matrix:
            try:
                tmp = int(sum(row))
            except TypeError:
                print('Matrix must consists of numbers')
                return None
        self.matrix = matrix

    def __str__(self):
        result = ''
        for row in self.matrix:
            result += '\t\t'.join(str(el) for el in row) + '\n'
        return result

    def __add__(self, other):
        matrix = []
        for i, row in enumerate(self.matrix):
            if len(other.matrix) > i:
                res_row = []
                for j, el in enumerate(row):
                    if len(other.matrix[i]) > j:
                        res_row.append(el + other.matrix[i][j])
                    else:
                        res_row.append(el)
                if len(other.matrix[i]) > len(row):
                    for j in range(len(row), len(other.matrix[i])):
                        res_row.append(other.matrix[i][j])
                matrix.append(res_row)
            else:
                matrix.append(row)
        if len(other.matrix) > len(self.matrix):
            for i in range(len(self.matrix), len(other.matrix)):
                matrix.append(other.matrix[i])
        return Matrix(matrix)


print(Matrix([[1, 200000, 1], ['3'], [5000, 15, 20]]))
print(Matrix([[1, 2, 3], [4], [5, 6]]) + Matrix([[1, 2], [3, 4, 5]]))
