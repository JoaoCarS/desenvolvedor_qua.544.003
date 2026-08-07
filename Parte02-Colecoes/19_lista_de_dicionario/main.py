# lista de dicionários
usuarios = [
    {
        'nome': "Fulano",
        'idade': 18,
        'email': "fulano@gmail.com"
    },
    {
        'nome': "Cicrano",
        'idade': 21,
        'email': "cicrano@gmail.com"
    },
    {    
        'nome': "Beltrano",
        'idade': 35,
        'email': "beltrano@gmail.com"
    }
]

# percorre a lista de dicionários
for usuario in usuarios:
    for chave, valor in usuario.items():
        print(f"{chave.capitalize()}: {valor}")

    # imprime 40 traços separando as listas
    print(f"{'-'*40}")