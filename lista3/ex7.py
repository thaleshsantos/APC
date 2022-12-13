a = float(input())
b = int(input())
c = int(input())



for X in range(c):
    y = (a * b) * 1.025
    print(f'Lote: {X+1} - Total da venda: R$ {y:.2f}')
