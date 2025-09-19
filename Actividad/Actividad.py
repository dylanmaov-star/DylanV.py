
usuarios = []

def agregarUsuario():
    nombre = input("Ingrese el nombre del usuario: ")
    usuarios.append(nombre)
    print("El usuario agregado es: ", nombre)

def mostrarUsuarios():
    print("Usuarios actuales:", usuarios)

def usarExtend():
    nuevos = input("Ingrese nuevos usuarios: ").split(",")
    usuarios.extend([n.strip() for n in nuevos])
    print("Los nuevos usuarios son: ", usuarios)

def usarInsert():
    pos = int(input("Ingrese la posición para poder insertar un usuario "))
    nombre = input("Ingrese el nombre del usuario: ")
    usuarios.insert(pos, nombre)
    print("Los nuevos usuarios insertados son: ", usuarios)

def usarRemove():
    nombre = input("Ingrese el nombre a eliminar: ")
    if nombre in usuarios:
        usuarios.remove(nombre)
        print("El usuario eliminado es: ", nombre)
    else:
        print("No existe este usuario en la lista")

def usarPop():
    pos = int(input("Ingrese la posición a eliminar: "))
    if 0 <= pos < len(usuarios):
        eliminado = usuarios.pop(pos)
        print("Se eliminó a: ", eliminado)
    else:
        print("No es valida esa posición")

def usarIndex():
    nombre = input("Ingrese el nombre que quiere buscar: ")
    if nombre in usuarios:
        print("El usuario está en la posición:", usuarios.index(nombre))
    else:
        print("El usuario no existe en la lista")

def usarCount():
    nombre = input("Ingrese el nombre a contar: ")
    print("El usuario aparece", usuarios.count(nombre), "veces en la lista")

def usarSort():
    usuarios.sort()
    print("Usuarios ordenados:", usuarios)

def usarReverse():
    usuarios.reverse()
    print("Usuarios invertidos: ", usuarios)


def menu():
    while True:
        print("\nMENÚ DE USUARIOS")
        print("1.Agregar usuario (append)")
        print("2.Mostrar usuarios")
        print("3.Agregar varios usuarios (extend)")
        print("4.Insertar usuario en posición (insert)")
        print("5.Eliminar usuario por nombre (remove)")
        print("6.Eliminar usuario por posición (pop)")
        print("7.Buscar posición de usuario (index)")
        print("8.Contar cuántas veces aparece un usuario (count)")
        print("9.Ordenar usuarios (sort)")
        print("10.Invertir orden de usuarios (reverse)")
        print("11.Finalizar programa")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            agregarUsuario()
        elif opcion == "2":
            mostrarUsuarios()
        elif opcion == "3":
            usarExtend()
        elif opcion == "4":
            usarInsert()
        elif opcion == "5":
            usarRemove()
        elif opcion == "6":
            usarPop()
        elif opcion == "7":
            usarIndex()
        elif opcion == "8":
            usarCount()
        elif opcion == "9":
            usarSort()
        elif opcion == "10":
            usarReverse()
        elif opcion == "11":
            print("Saliendo del programa...")
            break
        else:
            print("Opción inválida. Intente de nuevo.")

menu()
