def anobissexto(A):
    if (A % 4 == 0 and A % 100 != 0) or (A % 400 == 0):
        return('Sim')
    else:
        return('Nao')
