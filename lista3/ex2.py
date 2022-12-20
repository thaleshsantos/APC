def soma_harmonica(x):
    numero = 1
    if x > 1:
        numero = ((1/x) + soma_harmonica(x-1))
    return numero
