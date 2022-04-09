class Road:
    _length = 0
    _width = 0

    def __init__(self, l, w):
        self._length = l
        self._width = w

    def cloth_mass(self, m=25, h=5):
        return self._length * self._width * m * h / 1000


road = Road(5000, 20)
print(
    f'For road of length {road._length} m. and width {road._width} m. you need {road.cloth_mass()} tons of asphalt with default parameters '
    f'or {road.cloth_mass(15, 3)} tons of superthin asphalt for superthin covering')
