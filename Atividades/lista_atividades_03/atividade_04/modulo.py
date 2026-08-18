import os 
import math

def limpar():
    os.system("cls" if os.name == "nt" else "clear")

def calcular_potencia(base, expoente):
    return base ** expoente

def calcular_raiz_quadrada(numero):
    return math.sqrt(numero)

def calcular_volume_paralelepípidico(comprimento, largura, altura):
    return comprimento * largura * altura

def calcular_volume_cilindrico(raio, altura):
    return math.pi * (raio ** 2) * altura