n = int(input())
array = list(map(int, input().split()))
maximo = max(array)
for x in map(lambda x: maximo - x, array):
    print(x, end=' ') 
