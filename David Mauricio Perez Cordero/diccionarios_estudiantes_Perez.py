"""
#SOBRE ESCRITURA DE DICCIONARIO:

estudiante[1]={"español":[agregar]}
//sobre escribe el diccionario queda unicamente 1:{"español":nota_agregada}

estudiante[int(agregar[0])] = {"nombre": agregar[1], "apellido": agregar[2], "edad": agregar[3]}
//sobre escribe uno a uno cada valor del diccionario

#EDITADO DEL DICCIONARIO:

estudiante[1]["materias"][dato] = []
//quiere decir que en el diccionario estudiante del código 1, anidado al diccionario materias,
//la materia con el dato ingresado va a tener una nota de vacío ([dato] = [])
"""
""" 
estudiante[codigo_estudiante]["materias"].setdefault(materia, []).extend(notas)
//setdefault() devuelve el valor de la clave especificada. Si la clave no existe, inserta la clave con el valor especificado.
//extend() agrega los elementos de la lista notas a la lista de la materia especificada en el diccionario estudiante
Caso 1: Materia existe
materia = "matemáticas"
notas = [95]

# Después de ejecutar:
estudiante[1001]["materias"].setdefault("matemáticas", []).extend([95]) 
"matemáticas": [85, 90, 95]  # Se añaden las notas

Caso 2: Materia no existe
materia = "física"
notas = [75, 80]

# Después de ejecutar:
estudiante[1001]["materias"].setdefault("física", []).extend([75, 80])
"física": [75, 80]  # Se crea la materia con las notas
"""


# Definición del diccionario estudiante
estudiante ={
1:{"nombre":"Juan","apellido":"Perez","edad":22, "materias":{"matematicas":[], "español":[]}} }

#agregar estudiante 
"""
def agregar_estudiante():
    ciclos = int(input("¿Cuántas Estudiantes desea agregar? "))
    for _ in range(ciclos):
        agregar = input("ingrese el CODIGO, nombre , apellido y edad del estudiente separado por espacio:").split(" ")
        estudiante[int(agregar[0])] = {"nombre": agregar[1], "apellido": agregar[2], "edad": agregar[3]}
        codigo = int(agregar[0])
        nombre = agregar[1]
        apellido = agregar[2]
        edad = agregar[3]
        print(estudiante)
"""
def agregar_estudiante():
    try:
        # Validar número de estudiantes a agregar
        try:
            ciclos = int(input("¿Cuántos estudiantes desea agregar? "))
        except ValueError:
            raise ValueError("Debe ingresar un número entero para la cantidad de estudiantes")

        for _ in range(ciclos):
            try:
                datos = input("\nIngrese CÓDIGO, Nombre, Apellido y Edad (separados por espacio): ").split()
                
                # Validar cantidad de datos
                if len(datos) != 4:
                    raise ValueError("Formato incorrecto. Debe ingresar exactamente 4 valores")
                
                # Convertir y validar código
                codigo = int(datos[0])
                
                # Validar edad como número
                try:
                    edad = int(datos[3])
                except ValueError:
                    raise ValueError("La edad debe ser un número entero")
                
                # Verificar si el código ya existe
                if codigo in estudiante:
                    print(f"\n⚠️ El código {codigo} ya está registrado para:")
                    print(f"Nombre: {estudiante[codigo]['nombre']}")
                    print(f"Apellido: {estudiante[codigo]['apellido']}")
                    print(f"Edad: {estudiante[codigo]['edad']}")
                    
                    # Pedir confirmación
                    while True:
                        confirmacion = input("\n¿Desea sobrescribir este estudiante? (si/no): ").lower()
                        
                        if confirmacion == "no":
                            print("✅ Registro original mantenido")
                            break
                        elif confirmacion == "si":
                            # Sobrescribir estudiante
                            estudiante[codigo] = {
                                "nombre": datos[1].capitalize(),
                                "apellido": datos[2].capitalize(),
                                "edad": edad,
                                "materias": estudiante[codigo].get("materias", {})
                            }
                            print("✅ Estudiante actualizado exitosamente")
                            break
                        else:
                            print("⚠️ Opción inválida. Por favor ingrese 'si' o 'no'")
                else:
                    # Crear nuevo registro
                    estudiante[codigo] = {
                        "nombre": datos[1].capitalize(),
                        "apellido": datos[2].capitalize(),
                        "edad": edad,
                        "materias": {}
                    }
                    print(f"✅ Estudiante {datos[1]} {datos[2]} agregado exitosamente")

            except ValueError as e:
                print(f"⚠️ Error en el registro: {str(e)}")
            except Exception as e:
                print(f"⚠️ Error inesperado: {str(e)}")

        print("\nRegistro actualizado de estudiantes:")
        print(list(estudiante.keys()))

    except ValueError as e:
        print(f"\n⚠️ Error inicial: {str(e)}")
    except Exception as e:
        print(f"\n⚠️ Error crítico: {str(e)}")
        

#agregar materia
"""
def agregar_materia():
 ciclos = int(input("¿Cuántas Materias desea agregar? "))
 for _ in range(ciclos):# _ no se usa en ninguna parte del bulce, no interesa la varibale placeholder   
  dato=input("ingrese la materia:").lower()
  estudiante[1]["materias"][dato] = []
  print(estudiante)
    """
def agregar_materia():
    try:
        # Solicitar código de estudiante
        codigo = int(input("\nIngrese el código del estudiante: "))
        
        # Verificar si el estudiante existe
        if codigo not in estudiante:
            raise KeyError(f"El estudiante {codigo} no está registrado")
        
        # Verificar si existe clave 'materias'
        if "materias" not in estudiante[codigo]:
            estudiante[codigo]["materias"] = {}  # Crear si no existe

        # Pedir cantidad de materias
        try:
            ciclos = int(input("¿Cuántas materias desea agregar? "))
        except ValueError:
            raise ValueError("Debe ingresar un número entero para la cantidad de materias")

        for _ in range(ciclos):
            try:
                materia = input("Ingrese el nombre de la materia: ").lower()
                
                # Verificar si la materia ya existe
                if materia in estudiante[codigo]["materias"]:
                    print(f"⚠️ La materia {materia} ya existe - omitiendo...")
                    continue
                
                # Agregar materia con lista vacía
                estudiante[codigo]["materias"][materia] = []
                print(f"✅ Materia {materia} agregada correctamente")
                
            except Exception as e:
                print(f"⚠️ Error al procesar materia: {str(e)}")

        print(f"\nEstado actualizado del estudiante {codigo}:")
        print(estudiante[codigo])

    except ValueError as e:
        print(f"\n⚠️ Error de valor: {str(e)}")
    except KeyError as e:
        print(f"\n⚠️ Error: {str(e)}")
    except Exception as e:
        print(f"\n⚠️ Error inesperado: {str(e)}")


#agregar nota
"""
*El método .values() sirve para obtener una lista de todos los valores de un diccionario.

*El método extend() sirve para concatenar listas, es decir, para añadir los elementos de una lista al final de otra. 

*La función len sirve para contar el número de elementos de un objeto, 
como una lista, tupla, rango, cadena, diccionario, conjunto o conjunto helado. 

def agregar_nota():
 materia=input("ingrese la materia a la que desea agregar la nota:").lower()
 notas_str=input("ingrese la nota que desea agregar: ").split(" ")
 notas = [float(notas) for notas in notas_str]
 estudiante[1]["materias"][materia].extend(notas)
 print(estudiante)
"""

"""
 Explicación de las validaciones:
Verificación de estudiante registrado
if 1 not in estudiante:
Evita errores si el estudiante 1 no existe.

Verificación de estructura de materias
if "materias" not in estudiante[1]:
Valida que el estudiante tenga el campo "materias".

Validación de materia existente
if materia not in estudiante[1]["materias"]:
Evita agregar notas a materias no registradas.

Validación de notas vacías
if not notas_str:
Detecta si el usuario no ingresó ninguna nota.

Conversión segura a números
Bloque interno try-except para detectar valores no numéricos.
"""

def agregar_nota():
    try:
        # Solicitar código del estudiante
        codigo_estudiante = int(input("\nIngrese el código del estudiante: "))
        
        # Verificar si el estudiante existe
        if codigo_estudiante not in estudiante:
            raise KeyError(f"El estudiante {codigo_estudiante} no está registrado.")
        
        # Obtener materia
        materia = input("Ingrese la materia a la que desea agregar la nota: ").lower()
        
        # Verificar si el estudiante tiene materias registradas
        if "materias" not in estudiante[codigo_estudiante]:
            raise KeyError("El estudiante no tiene materias registradas.")
        
        # Verificar si la materia existe
        if materia not in estudiante[codigo_estudiante]["materias"]:
            raise KeyError(f"La materia '{materia}' no existe.")
        
        # Obtener y validar notas
        notas_str = input("Ingrese las notas separadas por espacio: ").split()
        if not notas_str:
            raise ValueError("No se ingresaron notas.")
        
        # Convertir a números
        notas = []
        for nota_str in notas_str:
            try:
                notas.append(float(nota_str))
            except ValueError:
                raise ValueError(f"Valor inválido: '{nota_str}' no es un número válido.")
        
        # Agregar notas
        estudiante[codigo_estudiante]["materias"][materia].extend(notas)
        print(f"\n✅ Notas agregadas a {materia} del estudiante {codigo_estudiante}")
        print(f"Notas actualizadas: {estudiante[codigo_estudiante]['materias'][materia]}")

    except ValueError as e:
        if "invalid literal for int()" in str(e):
            print("\n⚠️ Error: El código de estudiante debe ser un número entero")
        else:
            print(f"\n⚠️ Error: {str(e)}")
    except KeyError as e:
        print(f"\n⚠️ Error: {str(e)}")
    except Exception as e:
        print(f"\n⚠️ Error inesperado: {str(e)}")

#consultar promedio
"""
suma_notas = []
materia_p=input("ingrese la materia que desea consultar:").lower()
notas= estudiante[1]["materias"][materia_p]  # Lista de notas
for nota in notas:
    suma_notas.append(nota)
promedio_materia= sum(suma_notas)/len(suma_notas)
print(f"el promedio de la materia {materia_p} es: {promedio_materia}")
"""
def consultar_promedio():
    while True:
        try:
            # Solicitar código de estudiante
            codigo = int(input("\nIngrese el código del estudiante: "))
            
            # Verificar existencia del estudiante
            if codigo not in estudiante:
                print("⚠️ El estudiante no está registrado")
                continue
                
            # Verificar si tiene materias
            if "materias" not in estudiante[codigo] or not estudiante[codigo]["materias"]:
                print("⚠️ El estudiante no tiene materias registradas")
                continue

            # Selección de materia
            while True:
                materia = input("Ingrese la materia a consultar: ").lower()
                
                if materia in estudiante[codigo]["materias"]:
                    notas = estudiante[codigo]["materias"][materia]
                    break
                print("⚠️ Materia no encontrada. Materias disponibles:")
                print(", ".join(estudiante[codigo]["materias"].keys()))

            # Calcular promedio materia
            if notas:
                prom_materia = sum(notas)/len(notas)
                print(f"\n📊 Promedio de {materia.capitalize()}: {prom_materia:.1f}")
            else:
                print(f"\n⚠️ No hay notas en {materia.capitalize()}")
                continue

            # Preguntar promedio general
            while True:
                opcion = input("\n¿Ver promedio general? (s/n): ").lower()
                
                if opcion == 's':
                    # Calcular todas las notas
                    todas_notas = []
                    for m in estudiante[codigo]["materias"].values():
                        todas_notas.extend(m)
                    
                    if todas_notas:
                        prom_general = sum(todas_notas)/len(todas_notas)
                        print(f"\n📈 Promedio general: {prom_general:.1f}")
                    else:
                        print("⚠️ No hay notas en ninguna materia")
                    break
                    
                elif opcion == 'n':
                    break
                else:
                    print("⚠️ Opción inválida")

            # Nueva consulta
            while True:
                continuar = input("\n¿Consultar otro promedio? (s/n): ").lower()
                
                if continuar == 'n':
                    print("🏠 Volviendo al menú principal...")
                    return
                elif continuar == 's':
                    break
                else:
                    print("⚠️ Opción inválida")
            
            # Reiniciar bucle si eligió continuar
            continue

        except ValueError:
            print("⚠️ Error: El código debe ser numérico")
        except KeyError as e:
            print(f"Error en estructura de datos: {str(e)}")
        except Exception as e:
            print(f"⚠️ Error inesperado: {str(e)}")
            return

def imprimir_menu():
    print('✨✨ ------------------✨✨')
    print('--- Bienvenido al sistema de Estudiantes ---')
    print('✨✨ ------------------✨✨')
    print('[1] Agregar estudiante') 
    print('[2] Agregar nota')
    print('[3] Agregar materia')    
    print('[4] Consultar promedio')
    print('[5] Consultar estudiantes')
    print('[6] salir')
    print('✨✨ ------------------✨✨')
    
def obtener_una_opcion():
    while True:
        try:
            opcion= int(input('Seleccione una opción: '))
            if opcion>=1  and opcion <=5:
                return opcion
            else:
                print('Por favor, ingrese una opción válida.')
        except:
            print('Error. Intente Nuevamente.')

def consultar_promedio():
    while True:
        try:
            # Solicitar código de estudiante
            codigo = int(input("\nIngrese el código del estudiante (0 para salir): "))
            
            if codigo == 0:
                print("🏠 Volviendo al menú principal...")
                return
            
            # Verificar existencia del estudiante
            if codigo not in estudiante:
                print("⚠️ El estudiante no está registrado")
                continue
                
            estudiante_data = estudiante[codigo]
            
            print("\n" + "═"*40)
            print(f"📚 REPORTE COMPLETO - Estudiante {codigo}")
            print(f"├─ Nombre: {estudiante_data['nombre']}")
            print(f"├─ Apellido: {estudiante_data['apellido']}")
            print(f"└─ Edad: {estudiante_data['edad']}")
            
            # Verificar materias
            if "materias" not in estudiante_data or not estudiante_data["materias"]:
                print("\n⚠️ El estudiante no tiene materias registradas")
                continue
                
            print("\n📖 MATERIAS Y PROMEDIOS:")
            todas_notas = []
            
            for materia, notas in estudiante_data["materias"].items():
                print(f"├─ 📘 {materia.capitalize()}")
                print(f"│  ├─ Notas: {notas}")
                
                if notas:
                    promedio = sum(notas)/len(notas)
                    print(f"│  └─ Promedio: {promedio:.1f}")
                    todas_notas.extend(notas)
                else:
                    print("│  └─ Sin notas registradas")
            
            # Promedio general
            if todas_notas:
                promedio_general = sum(todas_notas)/len(todas_notas)
                print(f"\n📊 PROMEDIO GENERAL: {promedio_general:.1f}")
            else:
                print("\n⚠️ No hay notas en ninguna materia")
            
            print("═"*40)

        except ValueError:
            print("⚠️ Error: Debes ingresar un número entero válido")
        except KeyError as e:
            print(f"⚠️ Error en la estructura de datos: {str(e)}")
        except Exception as e:
            print(f"⚠️ Error inesperado: {str(e)}")
        
        # Preguntar por nueva consulta
        if input("\n¿Desea consultar otro estudiante? (s/n): ").lower() != 's':
            print("🏠 Volviendo al menú principal...")
            break

def main():
    while True:
        print("\n")
        imprimir_menu()
        opcion= obtener_una_opcion()
        if opcion ==1:
            agregar_estudiante()
        elif opcion ==2:
            agregar_nota()
        elif opcion ==3:
            agregar_materia()
        elif opcion ==4:
            consultar_promedio()
        elif opcion ==5:
            consultar_promedio()
        elif opcion ==6:
            print("Gracias por usar el sistema. ¡Hasta luego!")
            break
if __name__ == "__main__":
    main()