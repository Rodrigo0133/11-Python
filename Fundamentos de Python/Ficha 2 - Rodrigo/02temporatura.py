from funções import inicio, fim, tri_float, continuar
#Titulo
opcao = "s"
while opcao == "s":
    inicio('CLASSIFICAÇÃO DA TEMPERATURA DO AR')

    print("Insira o seguinte valor:")

    #Entradas
    temperatura = tri_float('Temperatura do ar (ºC) --> ')


    #Processamento e saida
    print("\nResultado")
    if temperatura > 54 or temperatura < -90:
        print("ERRO!! dado invalido ")
    elif temperatura < 5:
        print("Tempo muito frio\nAgasalhe-se bem e evite permanecer muito tempo no exterior\n")
    elif temperatura <= 5 and temperatura < 15:
        print("Tempo frio\nUse roupa quente, especialmente de manhã e à noite\n")
    elif temperatura >= 15 and temperatura < 25:
        print("Tempo agradável\nTemperatura confortável para a maioria das atividades ao ar livre\n")
    elif temperatura >= 25 and temperatura < 35:
        print("Tempo quente\nBeba água regularmente e evite exposição prolongada ao sol\n")
    else:
        print(" Tempo muito quente\nEvite esforços físicos nas horas de maior calor, procure locais frescos e hidrate-se frequentemente.\n")
    opcao = continuar()

# FINALIZAÇÃO
fim()
