usuario = {
    'nome':input('digite seu nome: '),
    'idade':float(input('digite sua idade: '))
}
if usuario['idade'] >= 18:
    print(f"Acesso liberado para: {usuario['nome']}")
else:
    print(f'Acesso negado para: {usuario['nome']}')