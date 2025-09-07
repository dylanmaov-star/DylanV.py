import random

#14 Control de temperatura


def obtener_humedad():
    return random.randint(20, 100)

def regar():
    print("Activando sistema de riego...")

def monitorear(umbral):
    while True:
        humedad = obtener_humedad()
        print(f"Humedad actual: {humedad}%")
        
        if humedad < umbral:
            regar()
        else:
            print("Humedad suficiente, no es necesario regar.")
            break

umbral = int(input("Ingrese el umbral de humedad deseado (%): "))
monitorear(umbral)