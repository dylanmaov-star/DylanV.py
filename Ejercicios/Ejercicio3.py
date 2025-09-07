#3 Factorial + pares/impares


def pedir_numero():
    return int(input("Ingrese un número entero positivo: "))

def calcular_datos(n):
    factorial = 1
    pares, impares = 0, 0
    suma_pares, suma_impares = 0, 0

    for i in range(1, n+1):
        factorial *= i
        if i % 2 == 0:
            pares += 1
            suma_pares += i
        else:
            impares += 1
            suma_impares += i

    return factorial, pares, impares, suma_pares, suma_impares

def mostrar_resultado(factorial, pares, impares, suma_pares, suma_impares):
    print("\n--- Resultados ---")
    print("Factorial:", factorial)
    print("Cantidad de pares:", pares, "→ Suma:", suma_pares)
    print("Cantidad de impares:", impares, "→ Suma:", suma_impares)

n = pedir_numero()
factorial, pares, impares, suma_pares, suma_impares = calcular_datos(n)
mostrar_resultado(factorial, pares, impares, suma_pares, suma_impares)

