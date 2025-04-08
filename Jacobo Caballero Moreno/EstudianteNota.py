estudiantes = {}

def agregar_estudiante():
    cedula = int(input("Ingrese la cédula del estudiante: "))
    if cedula in estudiantes:
        print("El estudiante ya está registrado.")
        return
    nombre = input("Ingrese el nombre del estudiante: ")
    apellido = input("Ingrese el apellido del estudiante: ")
    edad = int(input("Ingrese la edad del estudiante: "))
    estudiantes[cedula] = {"nombre": nombre, "apellido": apellido, "edad": edad, "materias": {}}
    print("Estudiante agregado correctamente.")

def agregar_materia():
    cedula = int(input("Ingrese la cédula del estudiante: "))
    if cedula not in estudiantes:
        print("El estudiante no está registrado.")
        return
    materia = input("Ingrese el nombre de la materia: ")
    if materia in estudiantes[cedula]["materias"]:
        print("La materia ya existe para este estudiante.")
    else:
        estudiantes[cedula]["materias"][materia] = []
        print("Materia agregada.")

def agregar_nota():
    cedula = int(input("Ingrese la cédula del estudiante: "))
    if cedula not in estudiantes:
        print("El estudiante no está registrado.")
        return
    materia = input("Ingrese la materia a la que desea agregar nota: ")
    if materia not in estudiantes[cedula]["materias"]:
        print("La materia no existe para este estudiante.")
        return
    nota = float(input("Ingrese la nota: "))
    estudiantes[cedula]["materias"][materia].append(nota)
    print("Nota agregada.")

def consultar_promedio():
    cedula = int(input("Ingrese la cédula del estudiante: "))
    if cedula not in estudiantes:
        print("El estudiante no está registrado.")
        return
    if not estudiantes[cedula]["materias"]:
        print("El estudiante no tiene materias registradas.")
        return
    
    suma_total = 0
    cantidad_notas = 0
    for notas in estudiantes[cedula]["materias"].values():
        suma_total += sum(notas)
        cantidad_notas += len(notas)
    
    if cantidad_notas == 0:
        print("El estudiante no tiene notas registradas.")
    else:
        print(f"El promedio del estudiante es: {suma_total / cantidad_notas:.2f}")

def menu():
    while True:
        print("\n1. Agregar estudiante")
        print("2. Agregar materia")
        print("3. Agregar nota")
        print("4. Consultar promedio")
        print("5. Salir")
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            agregar_estudiante()
        elif opcion == "2":
            agregar_materia()
        elif opcion == "3":
            agregar_nota()
        elif opcion == "4":
            consultar_promedio()
        elif opcion == "5":
            print("Saliendo...")
            break
        else:
            print("Opción inválida, intente de nuevo.")

menu()