#Titulo
print("-" * 55)
print("\tDIVISÃO DE DESPESAS NUMA REFEIÇÃO")
print("-" * 55)

#Entradas
print("Insira os seguintes dados:")
while True:
    try:
        valor_total = float(input("Valor total da fatura (€) --> "))
        numero_pessoas = int(input("Número de pessoas --> "))
        if numero_pessoas <= 0:
            print("O número de pessoas deve ser superior a zero!")
            continue
        break
    except ValueError:
        print("Digite valores numéricos válidos!")

#Processamento
valor_por_pessoa = valor_total / numero_pessoas

#Saída
print("Resultados:")
print(f"Valor a pagar por cada pessoa = {valor_por_pessoa:.2f} €")

#Finalização
input("Prima ENTER para terminar...")
