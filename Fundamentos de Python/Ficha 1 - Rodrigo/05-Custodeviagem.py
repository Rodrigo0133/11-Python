#Titulo
print("-" * 55)
print("\tCUSTO DE VIAGEM")
print("-" * 55)

#Entradas
print("Insira os seguintes dados:")
while True:
    try:
        consumo_medio = float(input("Consumo médio da viatura (l/100 km) --> "))
        distancia_percorrer = float(input("Distância a percorrer (km) --> "))
        preco_litro = float(input("Preço do litro de combustível (€) --> "))
        break
    except ValueError:
        print("Digite valores numéricos válidos!")

#Processamento
litros_gastos = consumo_medio * distancia_percorrer / 100
custo_viagem = litros_gastos * preco_litro

#Saída
print("Resultados:")
print(f"Litros de combustível gastos: {litros_gastos:.1f} l")
print(f"Custo da viagem: {custo_viagem:.2f} €")

#Finalização
input("Prima ENTER para terminar...")
