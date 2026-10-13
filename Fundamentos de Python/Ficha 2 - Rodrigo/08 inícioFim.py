from funções import inicio, fim, tri_int,continuar

def verificar_dados(num_1,num_2):
    if(num_1<num_2):
        return False
    else:
        return True
def mostrar_numeros(num_1,num_2):
    print("Números compreendidos entre entre o menor valor e o maior valor: ")
    for i  in range(num_1,num_2+1):
        print(i,end=" ")

def main():
    opcao = "s"
    while opcao == "s":
        #Inicio
        inicio("== L I S T A G E N S  D E  N Ú M E R O S ==")

        print("Insira os dados:\n\n")
        #Entradas
        numero_1 = tri_int("Primeiro número inteiro --> ")
        numero_2 = tri_int("Segundo número inteiro --> ")
        print("\nResultado do processamento: \n")
        # Processamento e saida 
        if(verificar_dados(numero_1,numero_2) == True):
            print("Os valores de entrada foram trocados!\n")
            numero_1,numero_2 = numero_2,numero_1
        mostrar_numeros(numero_1,numero_2)
        opcao = continuar()
    print("\n")
    #Fim
    fim()
main()