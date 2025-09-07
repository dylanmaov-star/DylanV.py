#6 Factorial con bucle

def pedir_numero():
    return int(input("Ingrese un número entero no negativo: "))

def calcular_factorial(n):
    factorial = 1
    for i in range(1, n+1):
        factorial *= i
    return factorial

def mostrar_resultado(n, factorial):
    print(f"El factorial de {n} es {factorial}")

n = pedir_numero()
resultado = calcular_factorial(n)
mostrar_resultado(n, resultado)