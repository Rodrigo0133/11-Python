from funções import inicio, fim, tri_float, continuar
# MENU
def menu():
    print("MENU\n")
    print("[+] Soma")
    print("[-] Subtração")
    print("[*] Multiplicação")
    print("[/] Divisão")
    print("[p|P] Potenciação")
    print("-"*60)

# TÍTULO
opcao = "s"
while opcao == "s":
    inicio('CALCULADORA DE CONSOLA SIMPLES')

    menu()
    #Entrada
    print("Insira os seguintes dados:\n")

    numero_1 = tri_float('Número 1? ')
    numero_2 = tri_float('Número 2? ')

    operacao = input("\nEscolha a operação pelo caracter indicado --> ")

    # Processamento & Saida
    print("Resultado:\n")
    match operacao:
        case "+":
            print(f"{numero_1} + {numero_2} = {numero_1 + numero_2}")
        case "-":
            print(f"{numero_1} - {numero_2} = {numero_1 - numero_2}")
        case "*":
            print(f"{numero_1} * {numero_2} = {numero_1 * numero_2}")
        case "/":
            print(f"{numero_1} / {numero_2} = {numero_1 / numero_2}")
        case "p"|"P":
            print(f"{numero_1}^{numero_2} = {pow(numero_1,numero_2)}")
        case _:
            print("ERROR!! opção invalida")
    opcao = continuar()

# FINALIZAÇÃO
fim()
