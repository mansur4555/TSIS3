class MyClass(object):
    def __init__(self):
        self.s = ""
    def getString(self):
        self.s = input()
    def printString(self):
        print(self.s.upper())
gets = MyClass()
gets.getString()
gets.printString()