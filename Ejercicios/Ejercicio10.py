#10 Tabla de multiplicar
def pedir_numero():
    return int(input("Ingrese un número entero: "))

def generar_tabla(n):
    for i in range(1, 11):
        print(f"{n} x {i} = {n * i}")

def mostrar_tabla(n):
    print(f"\n--- Tabla de multiplicar del {n} ---")
    generar_tabla(n)

n = pedir_numero()
mostrar_tabla(n)

