#soma do vetores = 0 
V = int(input())
soma = 0
for x in range(V):
    soma += sum(map(int, input().split()))
if soma == 0:
   print('YES')
else:
   print('NO')
