programa_fidel = input("voce esta cadastrado no programa de fidelidade?: ")
valor_compra = float(input("digite o valor da compra: "))

if valor_compra >= 100:
    print("voce atingiu 1 das condições para ter o frete então, após atingir 2, você tera frfete gratis")
if programa_fidel == "sim":
    print("voce atingiu 1 das condições para ter o frete então, após atingir 2, você tera frfete gratis")

if programa_fidel == "sim" and valor_compra >= 100:
    print("voce atingiu todas as condições para o frete ")
    print("frete liberado")