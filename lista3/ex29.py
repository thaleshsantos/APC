n = int(input())
p = 0
for x in range(n):
    if sum(map(int, input().split())) >= 2:
        p += 1
print(p)
