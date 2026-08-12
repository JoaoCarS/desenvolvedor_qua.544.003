# TODO: atividade 03
# Crie um programa que receba o nome de um aluno e 3 notas.
''' O programa calcular a média do aluno e informar se o aluno está aprovado (média mínima = 7) ou
reprovado. Ao final, o usuário deverá escolher se deseja inserir as notas de outro aluno, que deverão 
ser gravadas no mesmo arquivo JSON'''

import json
import os

# criar lista
alunos = []
notas = []

os.system("cls" if os.name == "nt" else "clear")

while True:
    print(f"{'-'*15} BOLETIM {'-'*15}")
    print("1 - Calcular nota")
    print("2 - Listar nota")
    print("3 - Sair do programa")
    opcao = input("Informe a opção desejada: ").strip()

    os.system("cls" if os.name == "nt" else "clear")

    match opcao:
        case "1":
            aluno = {}
            aluno['nome'] = input("Informe o nome: ").strip().title()
            aluno['turma'] = input("Informe sua turma: ").strip()

            nota1 = float(input("Informe a primeira nota:"))
            nota2 = float(input("Informe a segunda nota:"))
            nota3 = float(input("Informe a terceira nota:"))
            aluno['notas'] = [nota1, nota2, nota3]

            media = sum(aluno['notas']) / len(aluno['notas'])

            if media >= 7:
                aluno['situacao'] = "Aprovado!"
            else:
                aluno['situacao'] = "Reprovado!"

            alunos.append(aluno)
            with open(f"atividade_03/{alunos}.json","w",encoding="utf-8") as f:
                json.dump(alunos, f)

            os.system("cls" if os.name == "nt" else "clear")
            continue
        case "2":
            if not alunos:
                print("Nenhum aluno cadastrado.")
            else: 
                for aluno in alunos:
                    print(f"Nome: {aluno['nome']}")
                    print(f"Turma: {aluno['turma']}")
                    print(f"Notas: {aluno['notas']}")

                    media = sum(aluno['notas']) / len(aluno['notas'])
                    print(f"Média: {media:.2f}")
                    print(f"Situação: {aluno['situacao']}")

                    with open(f"atividade_03/{alunos}.json","r",encoding="utf-8") as f:
                        alunos = json.load(f)
            continue
        case "3":
            print("Programa encerrado.")
            break
        case _:
            print("Opção inválida.")
            continue