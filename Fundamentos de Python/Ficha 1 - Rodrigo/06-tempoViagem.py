#Titulo
print("-" * 70)
print("\tTEMPO DE VIAGEM")
print("-" * 70)

#Entradas
print("Insira os seguintes dados:")
while True:
    try:
        distancia_percorrer = float(input("Distância a percorrer (km) --> "))
        velocidade_media = float(input("Velocidade média no trajeto (km/h) --> "))
        if velocidade_media <= 0:
            print("A velocidade média deve ser superior a zero!")
            continue
        break
    except ValueError:
        print("Digite valores numéricos válidos!")

#Processamento
tempo_segundos = int((distancia_percorrer / velocidade_media) * 3600)
tempo_dias = tempo_segundos // 86400
tempo_segundos %= 86400
tempo_horas = tempo_segundos // 3600
tempo_segundos %= 3600
tempo_minutos = tempo_segundos // 60
tempo_segundos %= 60

#Saída
print("Resultados:")
print(f"Duração da viagem - {tempo_dias:02d} Dias : {tempo_horas:02d} Horas : {tempo_minutos:02d} Minutos : {tempo_segundos:02d} Segundo")

#Finalização
input("Prima ENTER para terminar...")
