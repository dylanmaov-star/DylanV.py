#11 Contar dígitos en un número

def pedir_numero():
    return int(input("Ingrese un número entero positivo: "))

def contar_digitos(n):
    contador = 0
    while n > 0:
        n //= 10
        contador += 1
    return contador

def mostrar_resultado(digitos):
    print("Cantidad de dígitos:", digitos)

n = pedir_numero()
digitos = contar_digitos(n)
mostrar_resultado(digitos)