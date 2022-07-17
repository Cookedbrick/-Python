#Баловался ос списком функциий

from time import sleep

class TrafficLight:

    def __init__(self):
        self.__color = ('красный', 'жёлтый','зелёный')
        self.time = (7,2)

    def running(self):
        asd = ([print(self.__color[i]),
                sleep(self.time[i] if i < len(self.time) else 0)]
                   for i in range(3))
        for i in asd:
            i

tl = TrafficLight()
tl.running()
