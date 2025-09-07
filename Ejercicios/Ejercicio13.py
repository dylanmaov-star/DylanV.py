#13 Separar números pares e impares

def pedir_numero():
    return int(input("Ingrese un número entero positivo: "))

def separar_pares_impares(n):
    pares, impares = [], []
    for i in range(1, n+1):
        if i % 2 == 0:
            pares.append(i)
        else:
            impares.append(i)
    return pares, impares

def mostrar_listas(pares, impares):
    print("\nNúmeros pares:", pares)
    print("Números impares:", impares)

n = pedir_numero()
pares, impares = separar_pares_impares(n)
mostrar_listas(pares, impares)