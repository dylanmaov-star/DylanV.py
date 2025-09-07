# 1. Área y perímetro de figuras (menú)

import math

def triangulo():
    base = float(input("Ingrese la base: "))
    altura = float(input("Ingrese la altura: "))
    lado = float(input("Ingrese el lado: "))
    area = (base * altura) / 2
    perimetro = base + altura + lado
    print(f"Área del triángulo: {area}")
    print(f"Perímetro del triángulo: {perimetro}")

def cuadrado():
    lado = float(input("Ingrese el lado: "))
    area = lado ** 2
    perimetro = 4 * lado
    print(f"Área del cuadrado: {area}")
    print(f"Perímetro del cuadrado: {perimetro}")

def circunferencia():
    radio = float(input("Ingrese el radio: "))
    area = math.pi * radio ** 2
    perimetro = 2 * math.pi * radio
    print(f"Área de la circunferencia: {area}")
    print(f"Perímetro de la circunferencia: {perimetro}")

while True:
    print("\n1. Triángulo\n2. Cuadrado\n3. Circunferencia\n4. Salir")
    opcion = input("Elija una opción: ")
    if opcion == "1":
        triangulo()
    elif opcion == "2":
        cuadrado()
    elif opcion == "3":
        circunferencia()
    elif opcion == "4":
        break
    else:
        print("Opción inválida")
