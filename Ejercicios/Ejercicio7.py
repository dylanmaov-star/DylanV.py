#7 Suma de números pares hasta n
def pedir_numero():
    return int(input("Ingrese un número entero positivo: "))

def sumar_pares(n):
    suma = 0
    for i in range(2, n + 1, 2):
        suma += i
    return suma

def mostrar_resultado(suma):
    print("La suma de los números pares es:", suma)

n = pedir_numero()
resultado = sumar_pares(n)
mostrar_resultado(resultado)