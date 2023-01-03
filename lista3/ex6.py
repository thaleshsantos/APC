N = int(input())
array = list(map(int, input().split()))
minimo = min(array)
print(*map(lambda x: x - minimo, array))
