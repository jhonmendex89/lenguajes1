# Diccionario principal para almacenar los estudiantes
estudiantes = {}

def agregar_estudiante():
    nombre = input("Ingrese el nombre del estudiante: ")
    apellido = input("Ingrese el apellido del estudiante: ")
    edad = int(input("Ingrese la edad del estudiante: "))
    
    estudiantes[nombre] = {
        'apellido': apellido,
        'edad': edad,
        'materias': {}
    }
    print(f"Estudiante {nombre} {apellido} agregado correctamente.")

def agregar_materia():
    nombre = input("Ingrese el nombre del estudiante: ")
    if nombre in estudiantes:
        materia = input("Ingrese el nombre de la materia: ")
        estudiantes[nombre]['materias'][materia] = []
        print(f"Materia {materia} agregada al estudiante {nombre}.")
    else:
        print("Estudiante no encontrado.")

def agregar_nota():
    nombre = input("Ingrese el nombre del estudiante: ")
    if nombre in estudiantes:
        materia = input("Ingrese el nombre de la materia: ")
        if materia in estudiantes[nombre]['materias']:
            nota = float(input("Ingrese la nota: "))
            estudiantes[nombre]['materias'][materia].append(nota)
            print(f"Nota {nota} agregada a la materia {materia}.")
        else:
            print("Materia no encontrada para este estudiante.")
    else:
        print("Estudiante no encontrado.")

def consultar_promedio():
    nombre = input("Ingrese el nombre del estudiante: ")
    if nombre in estudiantes:
        materia = input("Ingrese el nombre de la materia: ")
        if materia in estudiantes[nombre]['materias']:
            notas = estudiantes[nombre]['materias'][materia]
            if notas:
                promedio = sum(notas) / len(notas)
                print(f"Promedio en {materia}: {promedio:.2f}")
            else:
                print("No hay notas registradas para esta materia.")
        else:
            print("Materia no encontrada para este estudiante.")
    else:
        print("Estudiante no encontrado.")

def menu():
    while True:
        print("\n--- MENÚ PRINCIPAL ---")
        print("1. Agregar Estudiante")
        print("2. Agregar Materia a Estudiante")
        print("3. Agregar Nota a Materia")
        print("4. Consultar Promedio")
        print("5. Salir")
        
        opcion = input("Seleccione una opción: ")
        
        if opcion == '1':
            agregar_estudiante()
        elif opcion == '2':
            agregar_materia()
        elif opcion == '3':
            agregar_nota()
        elif opcion == '4':
            consultar_promedio()
        elif opcion == '5':
            print("Saliendo del sistema...")
            break
        else:
            print("Opción no válida. Intente nuevamente.")

# Iniciar el programa
if __name__ == "__main__":
    menu()