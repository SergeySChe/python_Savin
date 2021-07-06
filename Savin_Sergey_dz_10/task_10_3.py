class Cell:
    def __init__(self, quantity):
        self.quantity = quantity


    def make_order(self, rows):
        return '\n'.join(['*' * rows for _ in range(self.quantity // rows)]) \
               + '\n' + '*' * (self.quantity % rows)


    def __str__(self):
        return str(self.quantity)


    def __add__(self, other):
        return 'Сумма клеток ' + str(self.quantity + other.quantity)


    def __sub__(self, other):
        return self.quantity - other.nums if self.quantity - other.nums > 0 \
            else 'Вычитание не возможно, так как ячеек в первой клетке <= второй'


    def __mul__(self, other):
        return 'Multiply of cells is ' + str(self.quantity * other.nums)


    def __truediv__(self, other):
        return 'Truediv of cells is ' + str(round(self.quantity / other.nums))


cell_1 = Cell(15)
cell_2 = Cell(29)
print(cell_1)
print(cell_1 + cell_2)
print(cell_2.make_order(23))
