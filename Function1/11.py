def isPal(word):
    letters = list(word)
    isPal = True
    for letter in letters:
        if letter == letters[-1]:
            letters.pop(-1)
        else:
            isPal = False

        return isPal

x = input()
print(isPal(x))