#15 Control de iluminación

def pedir_datos():
    hora = int(input("Ingrese la hora actual (0-23): "))
    en_casa = input("¿Hay alguien en casa? (s/n): ").lower() == "s"
    return hora, en_casa

def decidir_luces(hora, en_casa):
    if 18 <= hora <= 23 or 0 <= hora < 6:  # noche
        if en_casa:
            return "Luces encendidas"
        else:
            return "Luces apagadas (nadie en casa)"
    else:  # día
        return "Luces apagadas (es de día)"

def mostrar_resultado(resultado):
    print("\n" + resultado)

hora, en_casa = pedir_datos()
resultado = decidir_luces(hora, en_casa)
mostrar_resultado(resultado)
