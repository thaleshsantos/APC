a, b = map(int, input().split())
c = list()
for din in range(a):
    c.append(int(input()))
media = sum(c)//len(c)
print(f'media: {media}')
print(f'o rock reinara mais uma vez' if media >= b else 'rockeiros trabalhando ja')
