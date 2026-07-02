v = str(input("digite um veículo: "))
match v.lower():
    case "carro":
        print("Veículo terrestre")
    case "bicicleta":
        print("Transporte sustentável")
    case "avião":
        print("Transporte aéreo")
    case "helicóptero":
        print("Transporte aéreo")
    case _:
        print("Transporte desconhecido")