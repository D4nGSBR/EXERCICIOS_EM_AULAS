credenciais_corretas = {
    'nome':'Michael Jackson',
    'senha':'Billie Jean'
}
usuario = {
    'nome_usuario':input('Digite seu nome: '),
    'senha_usuario':input('Digite sua senha: ')
}
if credenciais_corretas['nome'] == usuario['nome_usuario'] and credenciais_corretas['senha'] == usuario['senha_usuario']:
    print("Login bem-sucedido")
else:
    print("Usuário ou senha incorretos")