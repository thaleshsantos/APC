N = int(input())
for x in range(N):
    if x>0:
        print(f'{x+1} elefantes incomodam muita gente...')
        print(f'{x+2} elefantes incomodam, {"incomodam, "*x}incomodam muito mais...')
    else:
       print(f'{x+1} elefante incomoda muita gente...')
       print(f'{x+2} elefantes incomodam, {"incomodam, "*x}incomodam muito mais...')  
        
