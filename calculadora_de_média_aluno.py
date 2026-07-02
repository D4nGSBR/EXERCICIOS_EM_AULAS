print("""Se for colocar número decimal, use ".", e não use ",", pois na linguagem do computador, a "," é do português, e não da matemática.""")
print("CALCULADORA DE MÉDIA: ")
nota1 = input("NOTA DO PRIMEIRO TRIMESTRE: ")
nota2 = input("NOTA DO SEGUNDO TRIMESTRE: ")
nota3 = input("NOTA DO TERCERO TRIMESTRE: ")

soma = float(nota1) + float(nota2) + float(nota3)
div = soma / 3
print("A MÉDIA ANUAL DO ALUNO É: " + str(div))