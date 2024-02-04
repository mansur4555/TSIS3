class Point(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def show(self):
        print(self.x, self.y)
    def move(self, i, j):
        self.x = i
        self.y = j
    def dist(self, point):
        distance = (((self.x - point.x)**2 + (self.y - point.y)**2)**0.5)
        return distance
p1 = Point(3, 4)
p2 = Point(7, 8)
p1.show()
p2.move(5, 6)
p2.show()
print(p1.dist(p2))