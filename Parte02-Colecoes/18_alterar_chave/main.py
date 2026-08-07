usuario = {
    'nome': "Fulano de tal",
    'idade': 35,
    'email': "fulano@gmail.com",
    'cpf': "123.456.789-12"
}

# usuário informa a chave que deseja alterar
chave = input("Informe o nome da chave: ").strip().lower()

if chave in usuario:
    # usuário informa o novo valor para a chave escolhida
    usuario[chave] = input(f"Informe o novo valor para {chave}:").strip()

    # exibe o dicionário com o novo valor da chave escolhida
    for chave, valor in usuario.items():
        print(f"{chave.capitalize()}: {valor}")
else:
    print("Chave não encontrada.")