#Titulo
print("-" * 80)
print("\tCALCULADORA DE DESCONTOS")
print("-" * 80)

#Entradas
print("Insira os seguintes dados:")
nome_artigo = input("Nome do artigo? ")
while True:
    try:
        custo_artigo = float(input("Custo do artigo (€)? "))
        percentagem_desconto = float(input("Percentagem de desconto? "))
        break
    except ValueError:
        print("Digite valores numéricos válidos!")

#Processamento
valor_desconto = custo_artigo * percentagem_desconto / 100
total_pagar = custo_artigo - valor_desconto

#Saída
print("Resultados:")
print(f"Artigo: {nome_artigo}")
print(f"Valor de desconto: {valor_desconto:.2f} €")
print(f"Total a pagar: {total_pagar:.2f} €")

#Finalização
input("Prima ENTER para terminar...")
