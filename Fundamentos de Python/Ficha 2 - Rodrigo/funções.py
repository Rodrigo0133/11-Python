# Imprimir o nome do programador
def inicio(titulo):
    print("-"*60)
    print(f"\t{titulo}")
    print("\t@2026 por Rodrigo Galante") 
    print("-"*60)

# Imprimir o final de cada exercicio
def fim():
    print("-"*60)
    print()
    input("Prima ENTER para terminar...")

# Declarar uma variavel int já com verificação de erros
def tri_int(titulo):
    while True:
        try:
            valor = int(input(f"{titulo}"))
            break
        except:
            print("ERROR Valor inválido!")
    return valor

# Imprimir linha
def linha():
    print("-"*60)
# Declarar uma variavel float já com verificação de erros
def tri_float(titulo):
    while True:
        try:
            valor = float(input(f"{titulo}"))
            break
        except:
            print("ERROR Valor inválido!")
    return valor

def continuar():
    opcao = input("Deseja continuar o programa? (s) --> ").lower().strip()
    return opcao 