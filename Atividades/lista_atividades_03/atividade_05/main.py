# TODO: atividade 05
''' Usando recursiviade, crie um programa onde o usuário informa um número inteiro e o programa calcula a sequência Fibonacci até o número informado. '''

def fibonacci(n):
    if n <= 1:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)

def main():
    n = int(input("Informe um número inteiro: "))

    for i in range(n):
        print(fibonacci(i), end=" ")

if __name__ == "__main__":
    main()

# versao corrigida do professor
'''
def fibonacci(n):
    return n if n <= 1 else fibonacci(n-1) + fibonacci(n-2)
    
def main():
    n = int(input("Informe um número inteiro: "))
    print(f"O Número da sequência de Fibonacci: {fibonacci(n)}")
    
if __name__ == "__main__":
    main()
    
'''
# a versão corrigida do professor mostra apenas o número final, já a primeira mostra uma lista 