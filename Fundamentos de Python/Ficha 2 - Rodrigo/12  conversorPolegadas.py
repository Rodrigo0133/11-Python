from funções import inicio,fim,tri_float,linha
import os

# Funções de processamento
def converter_cm():
    cm = tri_float("Digite o valor dos centímetros a converter --> ")
    polegadas = cm/2.54
    print(f"Conversão em polegadas = {polegadas}")
def converter_pol():
    polegadas = tri_float("Digite o valor das polegadas a coverter --> ")
    cm = polegadas*2.54
    print(f"Conversão em centímetro = {cm}")


# MENU do conversor
def menu():
    print("[C] Polegadas --> Centímetros\n[P] Centímetros --> Polegadas\n[S] Sair")
    linha()
    escolha = input("\nPrima a tecla de uma opção valida --> ").lower().strip()
    return escolha


def main():
    while True:
        os.system("cls")
        #Titulo
        inicio("CONVERSOR DE MEDIDAS DE COMPRIMENTO\nPOLEGADAS <--> CENTÍMETROS")
        print("MENU")
        linha()
        escolha = menu()
        #Escolha de processamento
        match escolha:
            case "c":
                converter_pol()
            case "p":
                converter_cm()
            case "s":
                break # Sair do programa
            case _:
                print("ERRO")
    fim()
main()
