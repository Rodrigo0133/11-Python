from funções import inicio, fim, tri_int, continuar
# TÍTULO
opcao = "s"
while opcao == "s":
    inicio('VERIFICADOR DE ANO BISSEXTO')

    #ENTRADAS
    ano = tri_int('Ano a avaliar --> ')

    #Processamento & Saida
    if (ano % 4 == 0 and ano % 100 != 0 ) or ano % 400 == 0 :
        print("\nO ano indicado é bissexto.")
    else:
        print("\nO ano indicado não e bissexto.")
    opcao = continuar()

# FINALIZAÇÃO
fim()
