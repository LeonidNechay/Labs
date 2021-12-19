class Vector:
    def __init__(self, size):
        self.size = size
        self.coordinates = []
    def enter_el(self):
        self.coordinates = [float(input('{0} coordinate = '.format(i+1))) for i in range(self.size)]
    def print_coordinates(self):
        print(str(self.coordinates))
    def vector_lenth(self):
        return (sum(map(lambda x: x ** 2, self.coordinates))) ** (1 / 2)
    def vector_norm(self):
        return [(i / self.vector_lenth()) for i in self.coordinates]


v1 = Vector(int(input('Enter size = ')))
v1.enter_el()
v1.print_coordinates()
v1.vector_lenth()
print(v1.vector_norm())