a, b = map(int, input().split())
x, y = max(a,b), min(a,b)
if not x%y or (x%y>1 and not (x%(x%y))):
    print('Nao sao co-primos!')
else:
    print('Sao co-primos.')
