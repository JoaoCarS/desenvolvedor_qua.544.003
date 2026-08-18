# TODO: atividade 04
''' Utilizando o conceito de módulo, crie um módulo com funções que façam as seguintes ações:
- limpa o terminal.
- Calcula a potência de um  número informado pelo usuário elevado a outro número informado pelo usuário.
- Calcula a raiz quadrada de um número informdo pelo usuário.
- Calcula o volume de um recipiente paralelepíoidico.
- Calcula o volume de um cilíndrico.
- Em seguida, faça um programa que o usuário escolha executar uma dessas funções ou sair do programa. '''

from modulo import limpar, calcular_potencia, calcular_raiz_quadrada, calcular_volume_paralelepípidico, calcular_volume_cilindrico

def main():
    limpar()

    while True:
        print("MATEMÁTICA")
        print("1 - Potência")
        print("2 - Raiz quadrada")
        print("3 - Volume paralelepípidico")
        print("4 - Volume cilindrico")
        print("5 - Sair do programa")
        opcao = input("Informe a opção desejada: ").strip()

    
        limpar()

        match opcao:
            case "1":
                x = int(input("Informe o valor x: "))
                y = int(input("Informe o valor de y: "))
                limpar()
                print(f"O valor da potência é : {calcular_potencia(x, y)}")

                continue

            case "2":
                x = int(input("Informe o valor x: "))
                limpar()
                print(f"O valor da raiz quadrada é : {calcular_raiz_quadrada(x)}")

                continue

            case "3":
                x = int(input("Informe o valor x: "))
                y = int(input("Informe o valor de y: "))
                z = int(input("Informe o valor de z: "))
                limpar()
                print(f"O valor do volume paralelepípidico é : {calcular_volume_paralelepípidico(x, y, z)} ")

                continue

            case "4":
                x = int(input("Informe o valor x: "))
                y = int(input("Informe o valor de y: "))
                limpar()
                print(f"O valor do volume cilindrico é : {calcular_volume_cilindrico(x, y)}")

                continue

            case "5":
                print("Programa encerrado.")
                break
            case _:
                print("Opção inválida.")
                continue    