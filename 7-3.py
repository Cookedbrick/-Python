from random import randint

class Cell:

    def __init__(self, unit = 'not input'):
        #если сразу написать unit = randint(1,100) в __init__()
        #тогда для всех экземляров класса значении unit будет одинаковым
        if unit == 'not input':
            unit = randint(1,100)
        self.unit = unit
        
    def __str__(self):
        return f'{self.unit}'

    def __add__(self, other):
        return Cell(self.unit + other.unit)

    def __sub__(self, other):
        return Cell(self.unit - other.unit)

    def __mul__(self, other):
        return Cell(self.unit * other.unit)

    def __truediv__(self, other):
        return Cell(self.unit // other.unit)
      
    def make_order(self, sample, unit_in_row):       
        return( ''.join('\n'.rjust(unit_in_row + 1 if i < sample.unit else sample.unit % unit_in_row +1, '*')
                       for i in range(unit_in_row, sample.unit + unit_in_row, unit_in_row)))


c_1 = Cell()
print(c_1.unit)
c_2 = Cell()
print(c_2.unit)
print(c_1 + c_2)
print(c_1 - c_2)
print(c_1 * c_2)
print(c_1 / c_2)
print(c_1.make_order(c_2, 6))
