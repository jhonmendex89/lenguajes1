lista_estudaintes = {}

bandera = True

def estudiantes():
    name = str(input("Ingrese por favor solo el nombre del estudiante: "))
    apellido = str(input("Ingrese los apellidos por favor: "))
    edad = int(input("Ingrese la edad del estudiante: "))
    grado = int(input("¿En qué grado se encuentra el estudiante? escribe el numero : "))
    lista_estudaintes[name] = {"apellido": apellido, "edad": edad, "grado": grado, "notas": {}}
    
    while True:
        materia = int(input("Ingrese la materia o pulsea 0 para salir: "))
        if materia == 0 :
            break
        nota = float(input(f"Nota en {materia}: "))
        lista_estudaintes[name]["notas"][materia] = nota
    
    print(f"Estudiante {name} ingresó con éxito\n")

def mostrar_estudiantes():
    if not lista_estudaintes:
        print("\n No hay estudiantes ingresados, ingresalos porfavor ")
        return
    
    for name, valor in lista_estudaintes.items():
        print(f"Nombre: {name} {valor['apellido']}, edad: {valor['edad']}, Grado: {valor['grado']}")
        print("Notas:")
        for materia, nota in valor["notas"].items():
            print(f"  {materia}: {nota}")
        print("-")

while bandera:
    print("\n1. Agregar persona\n2. Mostrar estudiantes\n3. Salir")
    try:
        opcion = int(input("Seleccione una opción: "))
        if opcion == 1:
            estudiantes()
        elif opcion == 2:
            mostrar_estudiantes()
        elif opcion == 3:
            print("Okey, saliendo.")
            bandera = False
        else:
            print("Vuelve a poner un número del menú, por favor.")
    except ValueError:
        print("Error: Ingresa un número válido.")

# desallorado por santiago andres fonseca rojas