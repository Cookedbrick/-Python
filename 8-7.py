class Compl:
    

    def __init__(self, a, b):
        self.a = a
        self.b = b

    def __str__(self):
        return f'{self.a}+i{self.b}'

    def __mul__(self, other):
        a = self.a * other.a - self.b * other.b
        b = self.a * other.b + self.b * other.a
        return Compl(a, b)

    def __add__(self, other):
        a = self.a + other.a
        b = self.b + other.b
        return Compl(a, b)


a = Compl(2, 5)
b = Compl(7, -3)
print(a + b)
print(a * b)

