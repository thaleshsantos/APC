enter = input().split()
pa = int(enter[0])
pb = int(enter[1])
ca = float(enter[2])/100
cb = float(enter[3])/100
y = 0

if cb >= ca:
    print('A nunca alcancara B.')
else:
    while pa < pb and y <= 1000:
        pa += int(pa * ca)
        pb += int(pb * cb)
        y += 1
    if y > 1000 and ca > cb:
        print('Mais de um milenio.')
    elif y <= 1000:
        print(f'Vai alcancar em {y} ano(s).')
