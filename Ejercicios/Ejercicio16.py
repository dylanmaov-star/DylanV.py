import random

#16 Riego automático de jardín

def obtener_bateria():
    return random.randint(0, 100)

def mostrar_estado(bateria):
    if bateria <= 15:
        print(f" Batería baja ({bateria}%) - Conecta el cargador.")
    elif bateria <= 50:
        print(f" Batería media ({bateria}%)")
    else:
        print(f" Batería alta ({bateria}%)")

def monitorear_bateria():
    while True:
        bateria = obtener_bateria()
        mostrar_estado(bateria)
        if bateria <= 15:
            break  

monitorear_bateria()