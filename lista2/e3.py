def area(x, y, forma):
    if forma == 'losango':
        print(f'O losango tem {int(x*y/2)} de area')
    elif forma == 'retangulo':
        print(f'O retangulo tem {int(x*y)} de area')
    elif forma == 'triangulo':
        print(f'O triangulo tem {int(x*y/2)} de area')
    else:
        print(f'O circulo tem {int(y*x**2)} de area')
