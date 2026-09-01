from abc import ABC, abstractmethod

class IConta(ABC):
    @abstractmethod
    def consultar_dados():
        pass

    @abstractmethod
    def gerar_extrato():
        pass

    @abstractmethod
    def depositar(valor):
        pass

    @abstractmethod
    def sacar(valor):
        pass

class Conta(IConta):
    def __init__(self,titular,agencia,n_conta,saldo):
        self.__titular = titular
        self.__agencia = agencia
        self.__n_conta = n_conta
        self.__saldo = saldo

    @property
    def titular(self):
        return self.__titular

    @titular.setter
    def titular(self,titular):
        self.__titular = titular

    @property
    def agencia(self):
        return self.__agencia
    
    @agencia.setter
    def agencia(self,agencia):
        self.__agencia = agencia

    @property
    def n_conta(self):
        return self.__n_conta
        
    @n_conta.setter
    def n_conta(self,n_conta):
        self.__n_conta = n_conta

    @property
    def saldo(self):
        return self.__saldo
            
    @saldo.setter
    def saldo(self,saldo):
        self.__saldo = saldo

    def consultar_conta(self):
        print(f"Nome do titular da conta: {self.__titular}")
        print(f"Agência da conta: {self.__agencia}")
        print(f"Número da conta: {self.__n_conta}")
        print(f"Saldo da conta: R$ {self.__saldo:.2f}")

    def depositar(self, valor):
        if valor > 0:
            self.__saldo += valor
        return self.__saldo

    def sacar(self, valor):
        if valor <=0:
            return self.__saldo
        if valor > self.__saldo:
            print("Saldo insuficiente.")
            return self.__saldo
        self.__saldo -= valor
        return self.__saldo

    def gerar_extrato(self):
        nome_arquivo = f"extrato_{self.__n_conta}.txt"
        with open(nome_arquivo, "w", encoding="utf-8") as arquivo:
            arquivo.write("====== EXTRATO BANCÁRIO ======\n")
            arquivo.write(f"Titular: {self.__titular}\n")
            arquivo.write(f"Agência: {self.__agencia}\n")
            arquivo.write(f"Conta: {self.__n_conta}\n")
            arquivo.write(f"Saldo: R$ {self.__saldo:.2f}\n")
            
        print(f"Extrato criado: {nome_arquivo}")

class Pessoa():
    def __init__(self,nome,cpf):
        self.__nome = nome
        self.__cpf = cpf

    @property
    def nome(self):
        return self.__nome
                
    @nome.setter
    def nome(self,nome):
        self.__nome = nome

    @property
    def cpf(self):
        return self.__cpf
                    
    @cpf.setter
    def cpf(self,cpf):
        self.__cpf = cpf

    def __str__(self):
        return f"Nome: {self.__nome}\nCPF: {self.__cpf}"