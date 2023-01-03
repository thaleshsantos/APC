year = int(input())
primo = True

for i in range(2,year):
    if year % i == 0:
        primo = False
        
print('Emidio' if primo and year > 1 else 'Faina')
def chinelo(pe_do_bill, l):
    
    l.sort()
    i = 0
    while ((i < len(l)) and (l[i] < pe_do_bill)):
        i += 1
    if(i == len(l)):
        return -1
    else:
        return i

v = int(input())
l = [int(i) for i in input().split()]
print(chinelo(v, l))
