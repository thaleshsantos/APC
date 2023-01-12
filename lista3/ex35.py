x = input()
if int(x) >= 0:
    print(int(x[::-1]))
    
elif int(x) < 0:
    print(int('-'+x[1:][::-1]))
