from dataclasses import dataclass

@dataclass
class Pessoa:
    telefone: str
    email: str

    def __str__(self):
        return f"Telefone: {self.telefone}, Email: {self.email}"

    def __del__(self):
        print(f"Objeto {self} foi morto com sucesso!")

@dataclass
class PessoaFisica(Pessoa):
    nome: str
    cpf: str
    profissao: str
    idade: int
    salario: float

    def __str__(self):
        return f"Nome: {self.nome}\n CPF: {self.cpf}\n Profissão: {self.profissao}\n Idade: {len(self)}\n Salário: {float(self):.2f} {super().__str__()}"
    
    def __len__(self):
        return self.idade

    def __float__(self):
        return self.salario

@dataclass
class PessoaJuridica(Pessoa):
    razao_social: str
    nome_fantasia: str
    cnpj: str
    valor_de_mercado: float

    def __str__(self):
        return f"Razão Social: {self.razao_social}\n Nome Fantasia: {self.nome_fantasia}\n CNPJ: {self.cnpj}\n Valor de Mercado: R$ {float(self):.2f} {super().__str__()}"

    def __float__(self):
        return self.valor_de_mercado