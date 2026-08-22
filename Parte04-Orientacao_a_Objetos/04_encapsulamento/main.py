import os

from models import Pessoa


def limpar():
    os.system("cls" if os.name == "nt" else "clear")

def main():
    limpar()

    usuario = Pessoa(nome="",cpf="",email="",telefone="")

    usuario.nome = input("Informe seu nome: ").strip().title()
    usuario.cpf = input("Informe seu CPF: ").strip()
    usuario.email = input("Informe seu e-mail: ").strip().lower()
    usuario.telefone = input("Informe seu telefone: ").strip()

    print(f"Nome: {usuario.nome}")
    print(f"CPF: {usuario.cpf}")
    print(f"E-mail: {usuario.email}")
    print(f"Telefone: {usuario.telefone}")

if __name__ == "__main__":
    main()