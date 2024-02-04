def solve(numheads, numlegs):
    rabbit = (int(numlegs) - (2 * int(numheads))) // 2
    chicken = int(numheads) - int(rabbit)
    print(rabbit, chicken)
x = input()
y = input()

solve(x, y)