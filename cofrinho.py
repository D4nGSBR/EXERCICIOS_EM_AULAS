cofrinho = 0
while cofrinho >= 0:
    valor = float(input('Quantos reais deseja guardar?: '))
    cofrinho+=valor
    if valor == 0:
        print(f'O seu valor do cofrinho é: {cofrinho}')
        break