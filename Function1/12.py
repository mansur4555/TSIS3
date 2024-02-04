def histogram(li):
    if li.isdigit():
        print('*' * int(li))
        

lis = list(input())
for x in lis:
    histogram(x)