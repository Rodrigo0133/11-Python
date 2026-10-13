from funções import inicio, fim, tri_float, continuar
#comandos do SO
import os
#biblioteca
import math
opcao = "s"
while opcao == "s":
    #limpa o ecra
    os.system("cls")
    #cabeçalho
    inicio('Entrada controlada de dados')
    print("Insira os seguintes dados")
 
    #input
   
    for i in range(1,10+1,1):
        while True:
            numero = tri_float(f'{i}º numero--> ')
            if numero<1:
                print("ERROR..insira um valor maior que 0")
            else:
                break
                    #processamento
                
        print(f"Raiz quadrada de {numero:.3f} = {math.sqrt(numero):.3f} ")
                #verificacao de finalizacao
    opcao = continuar()
# FINALIZAÇÃO
fim()
