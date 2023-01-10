list = []
while True:
    x = int(input())
    if x != -1:
        list.append(x)
    elif x == -1:
        m = (sum(list)/len(list))
        print(f'{int(m)}')
        break
