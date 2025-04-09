estudiantes = {}

def menu():
    while True:
        print("\nMENU")
        print("1. Agregar estudiante")
        print("2. Agregar materia")
        print("3. Agregar nota")
        print("4. Consultar promedio de un estudiante")
        print("5. Ver resumen de un estudiante")
        print("6. Salir")
        opcion = input("Ingrese una opción: ")
        
        if opcion == "1":
            agregar_estudiante()
        elif opcion == "2":
            agregar_materia()
        elif opcion == "3":
            agregar_nota()
        elif opcion == "4":
            consultar_promedio()
        elif opcion == "5":
            ver_resumen()
        elif opcion == "6":
            print("Nos vemos Profe!")
            break
        else:
            print("bro ingresa un parametro valido")

def agregar_estudiante():
    cedula = input("Digite la cédula del estudiante: ")
    nombre = input("Digite el nombre del estudiante: ")
    apellido = input("Digite el apellido: ")
    edad = int(input("Digite la edad: "))
    estudiantes[cedula] = {"nombre": nombre, "apellido": apellido, "edad": edad, "notas": {}}
    print(f"Estudiante {nombre} agregado correctamente.")

def agregar_materia():
    cedula = input("Digite la cédula del estudiante: ")
    if cedula in estudiantes:
        materia = input("digite el nombre de la materia: ")
        if materia not in estudiantes[cedula]["notas"]:
            estudiantes[cedula]["notas"][materia] = []
            print(f"Materia {materia} agregada correctamente a {estudiantes[cedula]['nombre']}.")
        else:
            print("La materia ya existe.")
    else:
        print("Estudiante no encontrado.")

def agregar_nota():
    cedula = input("Digite la cédula del estudiante: ")
    if cedula in estudiantes:
        materia = input("Digite el nombre de la materia: ")
        if materia in estudiantes[cedula]["notas"]:
            nota = float(input(f"Digite la nota para {materia}: "))
            estudiantes[cedula]["notas"][materia].append(nota)
            print(f"Nota agregada correctamente a {materia} para {estudiantes[cedula]['nombre']}.")
        else:
            print("La materia no existe, agrégala primero.")
    else:
        print("Estudiante no encontrado.")

def consultar_promedio():
    cedula = input("Digite la cédula del estudiante: ")
    if cedula in estudiantes:
        notas_totales = []
        for materia, notas in estudiantes[cedula]["notas"].items():
            if notas:
                notas_totales.extend(notas)
        if notas_totales:
            promedio = sum(notas_totales) / len(notas_totales)
            print(f"El promedio de {estudiantes[cedula]['nombre']} es: {promedio:.2f}")
        else:
            print(f"{estudiantes[cedula]['nombre']} no tiene notas registradas.")
    else:
        print("Estudiante no encontrado.")

def ver_resumen():
    cedula = input("Digite la cédula del estudiante: ")
    if cedula in estudiantes:
        estudiante = estudiantes[cedula]
        print("\nResumen del estudiante")
        print(f"Nombre: {estudiante['nombre']} {estudiante['apellido']}")
        print(f"Edad: {estudiante['edad']}")
        print("Materias y notas:")
        if estudiante["notas"]:
            for materia, notas in estudiante["notas"].items():
                print(f"  {materia}: {notas}")
        else:
            print("  No tiene materias registradas.")
    else:
        print("Estudiante no encontrado.")

print("Bienvenido profe a la base de datos de los estudiantes")
menu()
