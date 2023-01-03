def function(pe, x):
    x.sort()
    i = 0
    while ((i < len(x)) and (x[i] < pe)):
        i += 1
    if(i == len(x)):
        return -1
    else:
        return i

v = int(input())
x = [int(i) for i in input().split()]
print(function(v, x))
