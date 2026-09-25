import math

#Titulo
print("-" * 55)
print("\tCÍRCULO")
print("-" * 55)

#Entradas
print("Insira os seguintes dados:")
while True:
    try:
        raio = float(input("Raio do círculo --> "))
        break
    except ValueError:
        print("Digite um número válido!")

#Processamento
perimetro = 2 * math.pi * raio
area = math.pi * raio ** 2

#Saída
print("Resultados:")
print(f"Perímetro do círculo = {perimetro:.2f}")
print(f"Área do círculo = {area:.2f}")

#Finalização
input("Prima ENTER para terminar...")
