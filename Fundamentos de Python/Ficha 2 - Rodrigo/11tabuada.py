from funções import inicio, fim, tri_int, continuar
#comandos do SO
import os
opcao = "s"
while opcao == "s":
    #limpa o ecra
    os.system("cls")
    #cabeçalho
    inicio('Tabuada')
    print("Insira os seguintes dados")
 
    #input
    while True:
        numero = tri_int('Numero inteiro [1 a 10]--> ')
        if numero<1 or numero>10:
            print("ERROR..insira um valor entre [1 e 10]")
        else:
            break
    #processamento
    for i in range(1,10+1):
        print(f"{numero} X {i} = {numero*i} ")
    #verificacao de finalizacao
    opcao = continuar()
# FINALIZAÇÃO
fim()
