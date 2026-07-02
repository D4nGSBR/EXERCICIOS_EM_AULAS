pizza = 0
hamburger = 0
while True: 
    voto = int(input('Opções para votar: \n' \
    '1- Pizza\n' \
    '2- Hambúrguer\n' \
    '3- Sair\n' \
    'Escolha: '))
    if voto == 1:
        pizza+=1
    elif voto == 2:
        hamburger+=1
    elif voto == 3:
        print(f'os votos de pizza foram: {pizza}.')
        print(f'os votos de hambúrguer foram: {hamburger}.')
        break