"""

@Rodrigo.Galante  18.set.26

"""

# Titulo
print("== ANTECESSOR E SUCESSOR DE UM Nº INTEIRO")

#Entradas
try:
    num_escolhido=int(input("Número inteiro? "))
except ValueError:
    print("Tens de inserir um número!")
    exit()

# Saidas
print(f"Antecessor: {num_escolhido - 1} ; Sucessor : { num_escolhido + 1 }")

input("Prima ENTER para terminar")