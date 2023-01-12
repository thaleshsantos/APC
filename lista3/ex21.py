x = int(input())
f = 'Fizz'
b = 'Buzz'
fb = 'Fizz Buzz'

for i in range(1, x+1):
    if ((i%3 == 0) and (i%5 == 0)):
        print(fb)
    elif i%3 == 0:
        print(f)
    elif i%5 == 0:
        print(b)
    else:
        print(i)
