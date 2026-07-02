def verificar_par(numero):
    if numero % 2 == 0:
        print('Par')
    else:
        print('Impar')

numero = int(input('Digite um número: '))
verificar_par(numero)