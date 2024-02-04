def prime (mylist):
    for i in range(2, 8):
        print(i) 
        return filter(lambda x: x == i or x % i, mylist)
def prime2 (mylist):
    nums = mylist
    for i in range(2, 8):
        print(i) 
        nums = filter(lambda x: x == i or x % i, nums)
    return nums
li = [1, 2, 3, 4, 5, 6, 7]
prime(li)
