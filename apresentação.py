def apresentar_pessoa(nome, idade):
    print(f"Nome: {nome} | Idade: {idade} anos")

nome = str(input('Digite seu nome: '))
idade = int(input('Digite sua idade: '))
apresentar_pessoa(nome, idade)