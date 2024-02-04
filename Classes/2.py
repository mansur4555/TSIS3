class Shape(object):
    def __init__(self):
        pass
    def area(self):
        return 0

class Square(Shape):
        def __init__(self, L):
            self.length = L
        def area(self):
            return self.length * self.length
aSquare = Square(4)
print(aSquare.area())