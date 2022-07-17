class Worker:

    def __init__(self, name, surename, position, wage, bonus):
        self.name = name
        self.surename = surename
        self.position = position
        self._income = {"wage": wage, "bonus": bonus}
    def primer(self):
        print('Попа')

class Position(Worker):

    def get_full_name(self):
        print(self.name + ' ', self.surename)

    def get_total_income(self):
        print(sum(self._income.values()))

vasy = Position("Вася", "Пупкин", "Клерк", 25000, 10000)
petr_konstantinovich = Position("Пётр", "Каратов",
                                "БОЛЬШОЙ НАЧАЛЬНИК", 1000, 150000)
print(vasy.name, vasy.surename, vasy.position)
vasy.get_full_name()
vasy.get_total_income()
print(petr_konstantinovich.name,
      petr_konstantinovich.surename,
      petr_konstantinovich.position)
petr_konstantinovich.get_full_name()
petr_konstantinovich.get_total_income()
