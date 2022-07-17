class Stationery:

    def __init__(self, title):
        self.title = title
    def draw(self):
        print('Запуск отрисовки')

class Pen(Stationery):

    def draw(self):
        print('This is pen, this is apple...')

class Pencil(Stationery):

    def draw(self):
        print(80085)

class Handle(Stationery):

    def draw(self):
        print('У меня не хорошие воспоменания связаны\
с handle из С++')

a = Pen('Фу')
b = Pencil('Какая')
c = Handle('Гадость')
a.draw()       
b.draw()
c.draw()
