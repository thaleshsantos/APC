def fib(n):
    if n < 2:
        return n
    else:
        return fib(n-1) + fib(n-2)

def fibonacci(n):
    for i in range(n):
        print(fib(i), end=' ')
