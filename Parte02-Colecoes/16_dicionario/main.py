# dicionário
usuario = {
    'nome': "Fulano de tal",
    'idade': 35,
    'email': "fulano@gmail.com",
    'cpf': "123.456.789-12"
}

# exibe os dados do dicionário
# forma 1
print("Forma 1:")
print(f"Nome: {usuario['nome']}")
print(f"Idade: {usuario['idade']}")
print(f"E-mail: {usuario['email']}")
print(f"CPF: {usuario['cpf']}")

# forma 2 - o get ele só pega os valores, ele não insere
print("Forma 2:")
print(f"Nome: {usuario.get('nome')}")
print(f"Idade: {usuario.get('idade')}")
print(f"E-mail: {usuario.get('email')}")
print(f"CPF: {usuario.get('cpf')}")

# forma 3
print("Forma 3:")
for chave in usuario:
    print(f"{chave.capitalize()}: {usuario.get(chave)}")