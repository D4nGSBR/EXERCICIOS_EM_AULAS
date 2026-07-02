def quadrado(numero):
    elevado = numero * numero
    return elevado

num = float(input('escolha um número: '))
num_elev = quadrado(num)
print(f'O quadrado do numero {num} é {num_elev} ')