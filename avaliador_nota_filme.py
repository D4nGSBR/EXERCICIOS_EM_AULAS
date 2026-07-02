print("Pense no filme mais recente que você viu.")
nota = float(input("Qual a nota que você da para o filme?: "))
if nota >= 9:
    print("Exelente!")
elif nota > 7:
    print("Muito bom!")
elif nota > 5:
    print("regular.")
elif nota <= 5:
    print("ruim.")