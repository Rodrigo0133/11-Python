from funções import inicio, fim, tri_float, continuar
#Entradas
opcao = "s"
while opcao == "s":
    inicio("TARIFA DE ESTACIONAMENTO EM AEROPORTO")
    print("Insira o seguinte valor: \n")
    horas = tri_float('Número de horas de estacionamento --> ')

    if horas < 3:
        valor_pagar = horas * 3
    elif horas >= 3 and horas < 13:
        valor_pagar = horas * 2.50
    elif horas >= 13 and horas <= 24:
        valor_pagar = 25
    else:
        horas -= 24
        valor_pagar = 25 + (15*(horas//24))
    # SAIDA
    print(f"Valor a pagar pelo estacionamento = {valor_pagar:.2f}")
    opcao = continuar()

#Finalização
fim()