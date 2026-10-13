"""

@Rodrigo.galante 18.set.26

"""
#Titulo
print("Calculadora do custo de uma viagem \nProgramador: Rodrigo Galante")

#Entrada
print("Insira os seguintes dados: \n")

while True:
    try:
        consume_medio = float(input("Consumo médio da viatura (l/100km) --> "))
        distancia_percorrer = float(input("Dinstancia a percorrer (km) --> "))
        preco_litro = float(input("Preço do litro de combustível (Euros) --> "))
        break
    except ValueError:
        print("Digite um número!")

#Processamento
litros_gastos = (consume_medio * distancia_percorrer)/100
custoViagem =  litros_gastos * preco_litro

#Saida
print("-"*20)
print(f"Litros de combustível gastos: {litros_gastos:.2f}€\n")
print(f"Custo de Viagem: {custoViagem}\n")
print("-"*20)

#Terminar
input("\nPrima ENTER para Terminar")