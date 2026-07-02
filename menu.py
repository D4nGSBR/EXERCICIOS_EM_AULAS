client = int(input("escolha uma opção do cardapio: \n1. pizza\n2. salada\n3. sushi\n escolha de acordo com os números: "))
match client:
    case 1: 
        print('VOCE ESCOLHEU PIZZA.')
    case 2:
        print('VOCE ESCOLHEU SALADA.')
    case 3:
        print('VOCE ESCOLHEU SUSHI.')
    case _:
        print("OPÇÃO INVALIDA.")