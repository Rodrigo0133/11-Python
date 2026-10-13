<<<<<<< HEAD
#Titulo
print("-" * 60)
print("\tTROCA DE NÚMEROS REAIS ENTRE DUAS VARIÁVEIS")
print("-" * 60)

#Entradas
print("Insira os seguintes dados:")
=======
"""

@Rodrigo.galante 18.set.26

"""

# Titulo
print("*"*60)
print("TROCA DE NÚMEROS REAIS ENTRE DUAS VARIÁVEIS")
print("*"*60)
# Entrada
>>>>>>> 0c8e24fcdcea24867aea3185da01a754650f77d7
while True:
    try:
        variavel_a = float(input("Variável A? "))
        variavel_b = float(input("Variável B? "))
        break
    except ValueError:
<<<<<<< HEAD
        print("Digite um número válido!")

#Processamento
variavel_a, variavel_b = variavel_b, variavel_a

#Saída
print("Resultados:")
print(f"Variável A = {variavel_a:.1f}; Variável B = {variavel_b:.1f}")

#Finalização
input("Prima ENTER para terminar...")
=======
        print("Digita um número!")
    

#Troca
c = variavel_a
variavel_a = variavel_b
variavel_b = c

#Saida
print(f"Variavel A = {variavel_a} ; Variavel B = {variavel_b}")

# Finalização
input("prima ENTER para terminar...")
>>>>>>> 0c8e24fcdcea24867aea3185da01a754650f77d7
