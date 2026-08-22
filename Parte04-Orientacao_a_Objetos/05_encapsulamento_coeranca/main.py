import os

from models import PessoaFisica,PessoaJuridica


def limpar():
    os.system("cls" if os.name == "nt" else "clear")

def main():
    usuario = PessoaFisica(nome="",cpf="",email="",telefone="")
    empresa = PessoaJuridica(nome_fantasia="",cnpj="",email="",telefone="")

    limpar()

    usuario.nome = input("Informe o nome do usuário: ").strip().title()
    usuario.cpf = input("Informe o CPF do usuário: ").strip()
    usuario.email = input("Informe o E-mail do usuário: ").strip().lower()
    usuario.telefone = input("Informe o telefone do usuário: ").strip()

    limpar()

    empresa.nome_fantasia = input("Informe o nome da empresa: ").strip()
    empresa.cnpj = input("Informe o CNPJ da empresa: ").strip()
    empresa.email = input("Informe o email da empresa: ").strip().lower()
    empresa.telefone = input("Informe o telefone da empresa: ").strip()

    limpar()

    print(f"Nome: {usuario.nome}")
    print(f"CPF: {usuario.cpf}")
    print(f"E-mail: {usuario.email}")
    print(f"Telefone: {usuario.telefone}")

    print(f"Nome da Empresa: {empresa.nome_fantasia}")
    print(f"CNPJ: {empresa.cnpj}")
    print(f"E-mail: {empresa.email}")
    print(f"Telefone: {empresa.telefone}")

if __name__ == "__main__":
    main()