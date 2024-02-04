from itertools import permutations 

def print_permutations(s):
    ans = list(permutations(s))
    print(s)
    for permutation in ans: 
        print(str().join(permutation), end = " ")
s = input()
print_permutations(s)   
