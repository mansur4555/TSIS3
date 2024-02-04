def check(n, m):
    print("Take a guess.")
    cnt = 1
    while n != m:
        n = input()
        n = int(n)
        if n < m:
            print("Your guess is too low.")
            cnt += 1
        elif n > m:
            print("Your guess is too high.")
            cnt += 1
        else:
            print("Good job, KBTU! You guessed my number in", cnt, "guesses.")
import random
print("Hello! What is your name?")
name = input()
print("Well, " + name + ", I am thinking of a number between 1 and 20.")
secret = random.randint(1, 20)
number = 0
check(number, secret)