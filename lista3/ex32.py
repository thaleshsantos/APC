soma, quantidade = 0, 0
while True:
    nota = int(input())
    if nota != -1:
        soma += 1/nota
        quantidade += 1
    if nota == -1:
        break 
print(int(quantidade/soma))
