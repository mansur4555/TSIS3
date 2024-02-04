def filter_prime(n):
    if n <= 1:
        return False
    flag = True
    for i in range(2, n):
        if n % i == 0:
            flag = False
            break
    return flag


MyList = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
primeNums = filter(filter_prime, MyList)

for x in primeNums:
    print(x)