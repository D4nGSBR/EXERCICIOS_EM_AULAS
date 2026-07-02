livros = ["Python", "Java", "C++"]
livros.append('JavaScript')
livros.remove('Java')
livros.remove('Python')
livros.insert(0, 'Go')
livro2 = len(livros)

print(f'a quantidade de livros que temos na lista é: {livro2}. e a lista é: {livros}')