year = int(input())
primo = True

for i in range(2,year):
    if year % i == 0:
        primo = False
        
print('Emidio' if primo and year > 1 else 'Faina')

