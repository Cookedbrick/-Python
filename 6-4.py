class Car:

    def __init__(self, speed, color, name, is_police):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = bool(is_police)
        self.azimuth = 0
        self.direction = {0: 'Север',
                          1: 'Северо-восток',
                          2: 'Восток',
                          3: 'Юго-восток',
                          4: 'Юг',
                          5: 'Юго-запад',
                          6: 'Запад',
                          7: 'Северо-запад'
                          }
#что бы не писать каждый раз print для вывода атрибутов класса
    def show(self):
        print(self.speed, self.color, self.name, self.is_police)

    def go(self):
        print('Поехали!')

    def stop(self):
        print('Ну вот')

    def show_speed(self):
        print(self.speed, 'км/ч')

    
    def turn(self, deg = 0):
        self.azimuth += deg
        if deg == 0:
            print('Вы продолжаете ехать прямо')
        else:
            print('Вы повернули на',
                    self.direction[int((self.azimuth%360)/45)])

class TownCar(Car):

    def show_speed(self):
        if self.speed > 60:
            print('Вы привысили скорость')
        else:
            print(self.speed, 'км/ч')

class WorkCar(Car):

    def show_speed(self):
        if self.speed > 40:
            print('Вы привысили скорость')
        else:
            print(self.speed, 'км/ч')
class SportCar(Car):
    pass
    
class PoliceCar(Car):
    pass

a = TownCar(50, 'red', 'Ласточка', 0)
b = WorkCar(250, 'green', 'Ласточка', 0)
c = SportCar(90, 'blue', 'Ласточка', 0)
d = PoliceCar(249, 'white', 'Ласточка', 1)
a.go()
a.turn(90)
a.show_speed()
a.stop()
a.show()
print('\n')
b.go()
b.turn(60)
b.show_speed()
b.stop()
b.show()
print('\n')
c.go()
c.turn(6514351)
c.show_speed()
c.stop()
c.show()
print('\n')
d.go()
d.turn(0)
d.show_speed()
d.stop()
d.show()

        
