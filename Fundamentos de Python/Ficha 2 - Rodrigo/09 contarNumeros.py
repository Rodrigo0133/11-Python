from funções import inicio, fim, tri_int, continuar
#comandos do SO
import os
opcao = "s"
while opcao == "s":
    #limpa o ecra
    os.system("cls")
    # TÍTULO
    inicio('VERIFICADOR DE ANO BISSEXTO')
    print("Insira os seguintes dados")
    
    #ENTRADA
    contador_1 = 0
    contador_2 = 0
    soma = 0
    for i in range(1,6+1):
        numero = tri_int(f'{i}.º numero inteiro? ')
        if(numero >= 50 and numero <= 100):
                contador_1 += 1
                soma += numero
        else:
            contador_2 += 1
        
    print("\nResultado do processamento:\n")
    print(f"Números pertencentes ao intervalo [50,100] = {contador_1}")
    if(contador_1 == 0):
        print(" -> Média dos números no intervalo = Sem dados.")
    else:
        print(f" -> Média dos números no intervalo = {soma / contador_1}")
    print(f"\nNúmeros fora do intervalo [50,100] = {contador_2}")

        
    
    
    
    opcao = continuar()
# FINALIZAÇÃO
fim()
