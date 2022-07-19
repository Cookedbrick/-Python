from abc import ABC, abstractmethod

class Clothes(ABC):
    class_dict = {}
    counter = 0
    counter_coat = 0
    counter_suit = 0

    @abstractmethod
    def show(self, a):
        pass
    
    @classmethod
    def cloth(cls):
        print(f'Всего {sum(cls.class_dict.values()):.4} \
погонных метров уйдёт на {cls.counter_coat} ед.\
пальто и {cls.counter_suit} ед. костюмов')

class Coat(Clothes):

    def __init__(self, v):
        Clothes.counter += 1
        Clothes.counter_coat += 1
        self.copy_numb = Clothes.counter
        Clothes.class_dict[self.copy_numb] = v/6.5 +0.5

    @property
    def show(self):
        print(f'На пошив данного пальто ушло \
{Clothes.class_dict[self.copy_numb]:.3} погонных метров ткани')

class Suit(Clothes):

    def __init__(self, h):
        Clothes.counter += 1
        Clothes.counter_suit += 1
        self.copy_numb = Clothes.counter
        Clothes.class_dict[self.copy_numb] = h*2 +0.3

    @property
    def show(self):
        print(f'На пошив данного костюма ушло \
{Clothes.class_dict[self.copy_numb]:.3} погонных метров ткани')

s_1 = Suit(1.84)
s_1.show
s_2 = Suit(2.0)
s_2.show
s_3 = Suit(1.63)
s_3.show
s_4 = Suit(1.75)
s_4.show
c_1 = Coat(48)
c_1.show
c_2 = Coat(22)
c_2.show
c_3 = Coat(39)
c_3.show
c_4 = Coat(40)
c_4.show
c_5 = Coat(38)
c_5.show
Clothes.cloth()

