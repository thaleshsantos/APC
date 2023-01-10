
n = int(input())
y = 0

for i in range(n):
    x = int(input())
    y += max(0, 1000-x)

print(y)
