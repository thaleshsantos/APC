import re
senha = input()
if 32 >= len(senha) >= 6:
    if re.match(r'(?=.*[a-z])(?=.*[A-Z])(?=.*[0-9])', senha):
        if not re.match(r'(?=.*[@#$%&¨!()])',senha):
            print('Senha valida.')
        else:
            print('Senha invalida.')
    else:
        print('Senha invalida.')
else:
    print('Senha invalida.')
