import os

from models import Conta, Pessoa

def limpar():
    os.system("cls" if os.name == "nt" else "clear")


def main():
    conta = Conta(titular="",agencia="1234-0",n_conta="432111-0",saldo=0.0)
    pessoa = Pessoa(nome="",cpf="")

    limpar()

    conta.titular = input("Informe o nome do titular da conta: ").strip().title()
    pessoa.cpf = input("Informe o CPF do titular da conta: ").strip()