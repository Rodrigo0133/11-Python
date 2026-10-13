from funções import inicio, fim, tri_int, continuar
import os
#Menu
def menu():
    print("PLANETAS QUE PODEM SER ANALISADOS\n\n[1] Mercúrio\n[2] Vénus\n[3] Marte\n[4] Jupiter\n[5] Saturno\n[6] Urano")
#Case para saber o peso no planeta
def planeta_indicado(num):
    match num:
        case 1:
            return 0.37
        case 2:
            return 0.88
        case 3:
            return 0.38
        case 4:
            return 2.64
        case 5:
            return 1.15
        case 6:
            return 1.17
        case _:
            return 0
def main():
    opcao = "s"
    while opcao == "s":
        os.system("cls")
        inicio("PESO DE UMA PESSOA NOUTRO PLANETA")
        menu()
        print("Insira os seguintes dados:")
        Peso = tri_int("\nEntre com um peso na Terra --> ")
        planeta = tri_int("Escolha o planeta pelo número indicado --> ")
        valor_planeta = planeta_indicado(planeta)
        print("\nResultado:")
        print(f"O seu peso no planeta Júpiter seria: {Peso * valor_planeta:.2f}\n")
        opcao = continuar()
    fim()

main()