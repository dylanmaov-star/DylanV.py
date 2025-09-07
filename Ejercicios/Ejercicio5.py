#5 Control de ventas semanales

def pedir_venta(dia):
    return float(input(f"Ingrese ventas del {dia}: "))

def calcular_total(lunes, martes, miercoles, jueves, viernes, sabado, domingo):
    return lunes + martes + miercoles + jueves + viernes + sabado + domingo

def mostrar_resumen(total):
    promedio = total / 7
    print("\n--- Resumen de Ventas ---")
    print("Total de ventas:", total)
    print("Promedio de ventas:", promedio)

print("=== Control de Ventas ===")

dias = ["Lunes", "Martes", "Miércoles", "Jueves", "Viernes", "Sábado", "Domingo"]

i = 0
lunes = martes = miercoles = jueves = viernes = sabado = domingo = 0.0


while i < len(dias):
    if dias[i] == "Lunes":
        lunes = pedir_venta("Lunes")
    elif dias[i] == "Martes":
        martes = pedir_venta("Martes")
    elif dias[i] == "Miércoles":
        miercoles = pedir_venta("Miércoles")
    elif dias[i] == "Jueves":
        jueves = pedir_venta("Jueves")
    elif dias[i] == "Viernes":
        viernes = pedir_venta("Viernes")
    elif dias[i] == "Sábado":
        sabado = pedir_venta("Sábado")
    elif dias[i] == "Domingo":
        domingo = pedir_venta("Domingo")
    i += 1

total = calcular_total(lunes, martes, miercoles, jueves, viernes, sabado, domingo)
mostrar_resumen(total)