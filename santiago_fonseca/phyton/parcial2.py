import json

estudiantes = {}
materias = ["sociales", "artes", "español", "ingles", "filosofia"]
num_estudiantes = 2
nota_minima = 30

def cargar_datos():
    global estudiantes
    try:
        with open("calificaciones.json", "r") as archivo:
            estudiantes = json.load(archivo)
        print("se cargo una base de datos ")
    except FileNotFoundError:
        print("no se encontro un archivo asi que se creara uno nuevo")

def guardar_datos():
    with open("calificaciones.json", "w") as archivo:
        json.dump(estudiantes, archivo, indent=6)
    print("Datos guardados correctamente.")

def ingresar_estudiantes():
    for i in range(num_estudiantes):
        nombre = input(f"Ingrese el nombre del estudiante {i+1}: ")
        estudiantes[nombre] = {}
        for materia in materias:
            estudiantes[nombre][materia] = 0.0

def ingresar_calificaciones():
    for nombre in estudiantes:
        print(f"\nNotas de: {nombre}")
        for materia in materias:
            while True:
                try:
                    nota = float(input(f"  Nota en {materia} (0-50): "))
                    if 0 <= nota <= 50:
                        estudiantes[nombre][materia] = nota
                        break
                    else:
                        print("  La nota debe estar entre 0 y 50. Intenta de nuevo.")
                except ValueError:
                    print("  Entrada inválida. Por favor ingresa un número válido.")

def promedio_estudiante(nombre):
    notas = estudiantes[nombre].values()
    promedio_p = sum(notas) / len(notas)
    return promedio_p

def promedio_materia(materia):
    total = sum(estudiantes[est][materia] for est in estudiantes)
    promedio_m = total / len(estudiantes)
    return promedio_m

def mostrar_aprobados_reprobados():
    print("\nAprobados y Reprobados:")
    for nombre in estudiantes:
        promedio = promedio_estudiante(nombre)
        estado = "Aprobado" if promedio >= nota_minima else "Reprobado"
        print(f"{nombre}: {promedio:.2f} - {estado}")

def estadisticas_generales():
    todas_notas = []
    for nombre in estudiantes:
        todas_notas.extend(estudiantes[nombre].values())

    mayor = max(todas_notas)
    menor = min(todas_notas)
    promedio_general = sum(todas_notas) / len(todas_notas)

    print(f"\nMayor calificación: {mayor}")
    print(f"Menor calificación: {menor}")
    print(f"Promedio general del grupo: {promedio_general:.2f}")

def menu():
    cargar_datos()
    bandera = True  
    while (bandera):
        print("\n--- Sistema de Calificaciones ---")
        print("1. Ingresar estudiantes")
        print("2. Ingresar calificaciones")
        print("3. Ver promedios por estudiante")
        print("4. Ver promedios por materia")
        print("5. Ver aprobados y reprobados")
        print("6. Ver estadísticas generales")
        print("7. Guardar y salir")

        try:
            opcion = int(input("Elige una opción: "))
        except ValueError:
            print("Opción no válida. Ingresa un número.")
            continue

        if opcion == 1:
            ingresar_estudiantes()
        elif opcion == 2:
            ingresar_calificaciones()
        elif opcion == 3:
            for nombre in estudiantes:
                promedio = promedio_estudiante(nombre)
                print(f"{nombre}: {promedio:.2f}")
        elif opcion == 4:
            for materia in materias:
                promedio = promedio_materia(materia)
                print(f"{materia}: {promedio:.2f}")
        elif opcion == 5:
            mostrar_aprobados_reprobados()
        elif opcion == 6:
            estadisticas_generales()
        elif opcion == 7:
            guardar_datos()
            break
        else:
            print("Opción no válida.")

menu()
