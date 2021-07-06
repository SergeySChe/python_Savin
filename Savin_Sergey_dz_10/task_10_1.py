class Matrix:
    def __init__(self, data):
        self.matrix = data

    def __iter__(self):
        return iter(self.matrix)

    def __add__(self, other):
        if len(list(self.matrix)) != len(list(other)):
            return 'Cложить нельзя. Введите матрицы одинакового типа!'
        for row1, row2 in zip(self.matrix, other):
            if len(row1) != len(row2):
                return 'Cложить нельзя. Введите матрицы одинакового типа!'
        matrix_sum = [[cell1 + cell2 for cell1, cell2 in zip(row1, row2)]
              for row1, row2, in zip(self.matrix, other)]
        return str(matrix_sum)[1:-1].replace(',', '').replace('] [', '\n').replace('[', '').replace(']', '')

    def __str__(self):
        return str(self.matrix)[1:-1].replace(',', '').replace('] [', '\n').replace('[', '').replace(']', '')

mat_1 = Matrix([
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
])
print(mat_1)
print()

mat_2 = Matrix ([
    [10, 20, 30],
    [40, 50, 60],
    [70, 80, 90]
])
print(mat_2)
print()
print(mat_1 + mat_2)
