#9 Conversión de temperaturas Celsius → Fahrenheit

def pedir_cantidad():
    return int(input("¿Cuántas temperaturas desea convertir? "))

def convertir_celsius_a_fahrenheit(c):
    return (c * 9/5) + 32

def mostrar_conversion(c, f):
    print(f"{c}°C  =  {f}°F")

cantidad = pedir_cantidad()

i = 0
while i < cantidad:
    c = float(input("Ingrese temperatura en °C: "))
    f = convertir_celsius_a_fahrenheit(c)
    mostrar_conversion(c, f)
    i += 1
