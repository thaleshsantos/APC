N = int(input())
for x in range(N):
    aluno = map(float, input().split())
    med = (sum(aluno)/3)
    if med >= 7:
        print(f'O ALUNO {x} FOI APROVADO')
    else:
        print(f'O ALUNO {x} FOI REPROVADO')
