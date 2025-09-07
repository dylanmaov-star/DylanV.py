
#2 Notas de Estudiantes


def calcular_nota_final():
    p1 = float(input("Nota 1: "))
    p2 = float(input("Nota 2: "))
    p3 = float(input("Nota 3: "))
    return (p1 + p2 + p3) / 3

aprobados = reprobados = total = suma = 0

while True:
    nombre = input("Nombre del estudiante: ")
    nota_final = calcular_nota_final()
    suma += nota_final
    total += 1

    if nota_final >= 3.0:
        aprobados += 1
    else:
        reprobados += 1

    continuar = input("¿Desea ingresar otro estudiante? (s/n): ")
    if continuar.lower() != "s":
        break

print(f"\nTotal estudiantes: {total}")
print(f"Aprobados: {aprobados}, Reprobados: {reprobados}")
print(f"Promedio general: {suma/total:.2f}")