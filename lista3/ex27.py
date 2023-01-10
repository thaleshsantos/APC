def ehPrimo(x):
    x = int(x)
    t = 0
    for i in range(1, x+1):
        if x % i == 0:
            t += 1
    if t == 2:
        return (1)
    else:
        return(0)

def divisoresPrimos(n):
    r = 0
    for y in range(2, n//2 + 1):
        if not n % y and ehPrimo(y):
            r += 1
    return r
