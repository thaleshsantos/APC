numero = int(input())
valor = 0
for x in range(numero):
    x = input()
    if x =='++X' or x == 'X++':
        valor += 1
    elif x == '--X' or x == 'X--':
        valor -= 1
print(valor)
