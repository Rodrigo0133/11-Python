"""

@Rodrigo.galante 18.set.26

"""
# Titulo
print("Calculadora de descontos\nProgramador: Rodrigo Galante")

#Entradas
nome_artigo = input("Nome do artigo? ")
while True:
    try:
        
        custo_artigo = float(input("Custo (euros)? "))
        percentagem_desconto = float(input("Percentagem de descontos?  "))
        break
    except ValueError:
        print("Digite um número!")
        
#Processamento
valor_desconto = custo_artigo * (percentagem_desconto/100)

#Saidas
print(f"Artigo: {nome_artigo} || Valor de desconto : {valor_desconto:.2f}€ || Total a pagar : {custo_artigo-valor_desconto}€")

#Finalização
input("prima ENTER para terminar ...")