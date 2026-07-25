# Atividade 01
"""
Crie um programa que receba o nome, peso e altura do usuário e informe na tela o seu IMC o seu diagnóstico com base no valor do IMC.
"""

nome = input("Informe seu nome: ").title()
peso = float(input("Informe seu peso: ").replace(",","."))
altura = float(input("Informe sua altura em metros: ").replace(",","."))


print(f"Seu nome é: {nome}")
print(f"Seu peso é: {peso}")
print(f"Sua altura é: {altura}")

imc = peso / (altura **2)
print(f"\nSeu IMC é: {imc:.2f}")

if imc < 18.5:
        print("Abaixo do peso") 
elif 18.5 <= imc < 25:
        print("Peso normal") 
elif 25 <= imc < 30:
        print("Sobrepeso") 
elif 30 <= imc < 35:
        print("Obesidade Grau 1")
elif 35 <= imc < 40:
        print("Obesidade Grau 2")
else:
        print("Obesidade Grau 3")