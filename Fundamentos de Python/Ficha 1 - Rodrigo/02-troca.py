#Titulo
print("-" * 60)
print("\tTROCA DE NÚMEROS REAIS ENTRE DUAS VARIÁVEIS")
print("-" * 60)

#Entradas
print("Insira os seguintes dados:")
while True:
    try:
        variavel_a = float(input("Variável A? "))
        variavel_b = float(input("Variável B? "))
        break
    except ValueError:
        print("Digite um número válido!")

#Processamento
variavel_a, variavel_b = variavel_b, variavel_a

#Saída
print("Resultados:")
print(f"Variável A = {variavel_a:.1f}; Variável B = {variavel_b:.1f}")

#Finalização
input("Prima ENTER para terminar...")
