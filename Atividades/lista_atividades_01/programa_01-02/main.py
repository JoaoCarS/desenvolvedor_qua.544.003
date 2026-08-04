# Atividade 02
""" Crie um programa que receba uma vez o nome e a idade do usuário, e em seguida mostre os filmes em cartaz em 5 salas de cinema:
- A volta dos que não foram (livre)
- A roda quadrada (12 anos)
- As tranças do rei careca (14 anos)
- Poeira em alto mar (16 anos)
- A vingança do frango assado (18 anos)
O usuário irá escolher a sala onde o filme desejado está passando. Caso o usuário não tenha idade, o programa impede sua entrada e re-exibe a lista para que o mesmo possa escolher outro filme. Caso o usuário tenha a idade mínima, o programa grava o arquivo do bilhete do filme e encerra o programa.
"""

# importação de biblioteca
import math
import os



nome = input("Informe seu nome: ")
idade = int(input("Informe sua idade: "))

os.system("cls" if os.name == "nt" else "clear")

while True:
    print("1 - Super Mario Bros (livre) - Sala 01")
    print("2 - Divertida Mente (12 anos) - Sala 02")
    print("3 - Jurassic World (14 anos) - Sala 03")
    print("4 - Vikings (16 anos) - Sala 04")
    print("5 - Deadpool (18 anos) - Sala 05")

    opcao = input("Escolha seu filme: ").strip()

    os.system("cls" if os.name == "nt" else "clear")

    match opcao:
        case "1":
            print("\n=== FICHA DA SEÇÃO ===")
            print("Nome:", nome)
            print("Idade:", idade)
            print(f"1 - Super Mario Bros (livre)")
            print("Sala: 1")
            print("Tenha uma ótima seção 😀")
            break

        case "2":
            if idade >= 12:
                print("\n=== FICHA DA SEÇÃO ===")
                print("Nome:", nome)
                print("Idade:", idade)
                print(f"2 - Divertida Mente (12 anos)")
                print("Sala: 02")
                print("Tenha uma ótima seção 😀")
                break
            else:
                print("Você não tem idade para esse filme. Escolha outro.")

        case "3":
            if idade >= 14:
                print("\n=== FICHA DA SEÇÃO ===")
                print("Nome:", nome)
                print("Idade:", idade)
                print(f"03 - Jurassic World (14 anos)")
                print("Sala: 03")
                print("Tenha uma ótima seção 😀")
                break
            else:
                print("Você não tem idade para esse filme. Escolha outro.")

        case "4":
            if idade >= 16:
                print("\n=== FICHA DA SEÇÃO ===")
                print("Nome:", nome)
                print("Idade:", idade)
                print(f"4 - Vikings (16 anos)")
                print("Sala: 04")
                print("Tenha uma ótima seção 😀")
                break
            else:
                print("Você não tem idade para esse filme. Escolha outro.")

        case "5":
            if idade >= 18:
                print("\n=== FICHA DA SEÇÃO ===")
                print("Nome:", nome)
                print("Idade:", idade)
                print(f"5 - Deadpool (18 anos)")
                print("Sala: 05")
                print("Tenha uma ótima seção 😀")
                break
            else:
                print("Você não tem idade para esse filme. Escolha outro.")

        case _:
            print("Opção inválida. Tente novamente.")
