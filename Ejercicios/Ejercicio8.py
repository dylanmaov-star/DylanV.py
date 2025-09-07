#8 Verificar si una palabra es palíndromo

def pedir_palabra():
    return input("Ingrese una palabra: ")

def es_palindromo(palabra):
    # Comprobamos manualmente con bucle y condicional
    for i in range(len(palabra) // 2):
        if palabra[i] != palabra[-(i+1)]:
            return False  # Si una letra no coincide, ya no es palíndromo
    return True  # Si todas coinciden, sí lo es

def mostrar_resultado(palabra, resultado):
    if resultado:
        print(f"{palabra} es un palíndromo")
    else:
        print(f"{palabra} NO es un palíndromo")

palabra = pedir_palabra()
resultado = es_palindromo(palabra)
mostrar_resultado(palabra, resultado)