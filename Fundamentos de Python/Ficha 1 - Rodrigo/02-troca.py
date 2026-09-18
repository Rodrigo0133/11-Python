"""

@Rodrigo.galante 18.set.26

"""

# Titulo
print("*"*60)
print("TROCA DE NÚMEROS REAIS ENTRE DUAS VARIÁVEIS")
print("*"*60)
# Entrada
while True:
    try:
        variavel_a = float(input("Variável A? "))
        variavel_b = float(input("Variável B? "))
        break
    except ValueError:
        print("Digita um número!")
    

#Troca
c = variavel_a
variavel_a = variavel_b
variavel_b = c

#Saida
print(f"Variavel A = {variavel_a} ; Variavel B = {variavel_b}")

# Finalização
input("prima ENTER para terminar...")