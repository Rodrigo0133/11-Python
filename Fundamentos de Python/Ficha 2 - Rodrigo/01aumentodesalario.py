from funções import inicio, fim, tri_float, continuar
#Titulo
opcao = "s"
while opcao == "s":
    inicio('CALCULADORA DE AUMENTO DO VENCIMENTO 5% ou 7%')
    # Entradas
    vencimento = tri_float('Vencimento: ')
    # Processamento & Saida
    if vencimento > 1500:
        vencimento = vencimento + (vencimento * 0.05) 
        print(f"Vencimento com aumento de 5% = {vencimento}")
    else:
        vencimento = vencimento + (vencimento * 0.07) 
        print(f"Vencimento com aumento de 7% = {vencimento}")
    opcao = continuar()

# FINALIZAÇÃO
fim()
