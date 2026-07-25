# Atividade 02
""" Crie um programa que receba uma vez o nome e a idade do usuário, e em seguida mostre os filmes em cartaz em 5 salas de cinema:
- A volta dos que não foram (livre)
- A roda quadrada (12 anos)
- As tranças do rei careca (14 anos)
- Poeira em alto mar (16 anos)
- A vingança do frango assado (18 anos)
O usuário irá escolher a sala onde o filme desejado está passando. Caso o usuário não tenha idade, o programa impede sua entrada e re-exibe a lista para que o mesmo possa escolher outro filme. Caso o usuário tenha a idade mínima, o programa grava o arquivo do bilhete do filme e encerra o programa.
"""

nome = input("Informe seu nome: ")
idade = int(input("Informe sua idade: "))

print("1 - Sala 01 - A volta dos que não foram (livre)")
print("2 - Sala 02 - A roda quadrada (12 anos)")
print("3 - Sala 03 - As tranças do rei careca (14 anos)")
print("4 - Sala 04 - Poeira em alto mar (16 anos)")
print("5 - Sala 05 - A vingança do frango assado (18 anos)")

opcao = input("Informe sua opção: ").strip()

match opcao:
    case "1":
        print(f"Sala 01 - A volta dos que não foram (livre)")
    case "2":
        print(f"Sala 02 - A roda quadrada (12 anos)")
    case "3":
        print()