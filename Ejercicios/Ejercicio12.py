#12 Verificar si un número es primo

def pedir_numero():
    return int(input("Ingrese un número entero: "))

def es_primo(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def mostrar_resultado(n, resultado):
    if resultado:
        print(n, "es un número primo")
    else:
        print(n, "NO es un número primo")

n = pedir_numero()
resultado = es_primo(n)
mostrar_resultado(n, resultado)