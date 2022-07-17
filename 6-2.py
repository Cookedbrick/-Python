class Road:

    def __init__(self, length, width):
        self._length = length
        self._width  = width

    def mass(self, wps, thickness):
        return self._length*self._width*wps*thickness

r = Road(5000, 20)
print(r.mass(25, 5))
