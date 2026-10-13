from funções import inicio, fim, tri_int, continuar
import os
def num_pares(num):
    total = 0
    contador = 0
    print("Resultado do processamento: \n")
    print("== Lista de números pares ==")
    for i in range(1,num+1):
        if(i % 2 == 0):
            print(i,end= " ")
            total += i
            contador += 1
    print(f"\n\nForam exibidos {contador} números pares. Soma = {total}")
def main():
    opcao = "s"
    while opcao == "s":
        os.system("cls")
        inicio("PROCESSAMENTO DE NÚMEROS PARES DE 1 ATÉ AO LIMITE INDICANDO PELO UTILIZADOR")
        limite = tri_int("Limite superior para listagem de números --> ")
        num_pares(limite)
        opcao = continuar()
    fim()
main()
        
        