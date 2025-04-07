clientes = {
    123: {
        "NOMBRE": "jhon", "APELLIDO": "mendez", "CORREO": "jhon@gmail.com", "TELEFONO": "32145859", "DIRECCION": "calle falsa 123", "PREFERENCIAL": False
    },
    456: {
        "NOMBRE": "juan", "APELLIDO": "pere", "CORREO": "juan@gmail.com", "TELEFONO": "32445859", "DIRECCION": "calle falsa 456", "PREFERENCIAL": True
    }
}

def imprimir_menu():
    menu = """
    ------REGISTRO DE CLIENTES UNISALLE----
    1. REGISTRAR UN CLIENTE
    2. ELIMINAR UN CLIENTE
    3. VISUALIZAR UN CLIENTE
    4. LISTAR CLIENTES
    5. LISTAR CLIENTES PREFERENCIALES
    6. SALIR DEL SISTEMA
    SELECCIONE UNA OPCIÓN:
    ---------
    """
    print(menu)

def registrar_cliente():
    try:
        datos = input("\nIngrese (separados por espacio) CEDULA, Nombre, Apellido, Correo, Telefono, Dirección, Preferencial(s/n): ").split()
        if len(datos) != 7:
            print("Error: Debe ingresar exactamente 7 datos.")
            return
        
        cedula = int(datos[0])
        nombre = datos[1]
        apellido = datos[2]
        correo = datos[3]
        telefono = datos[4]
        direccion = datos[5]
        preferencial = datos[6].strip().lower() == 's'

        if cedula in clientes:
            print(f"Error: Ya existe un cliente con la cédula {cedula}.")
            return

        clientes[cedula] = {
            "NOMBRE": nombre,
            "APELLIDO": apellido,
            "CORREO": correo,
            "TELEFONO": telefono,
            "DIRECCION": direccion,
            "PREFERENCIAL": preferencial
        }
        print(f"Cliente con cédula {cedula} registrado correctamente.")
    except ValueError:
        print("Error: La cédula y el teléfono deben ser números.")

def eliminar_cliente():
    try:
        cedulaCliente = int(input("\nIngrese la cédula del cliente: "))
        if cedulaCliente in clientes:
            del clientes[cedulaCliente]
            print(f"Cliente {cedulaCliente} eliminado correctamente.")
        else:
            print(f"Cliente {cedulaCliente} no encontrado.")
    except ValueError:
        print("Error: La cédula debe ser un número.")

def listar_clientes():
    print("----- Lista de clientes -----")
    for cedula, informacion in clientes.items():
        visualizar_cliente(cedula)

def listar_preferenciales():
    print("----- Lista de clientes preferenciales -----")
    for cedula, datos in clientes.items():
        if datos.get("PREFERENCIAL", False):
            visualizar_cliente(cedula)

def visualizar_cliente(cedula):
    if cedula in clientes:
        print(f"Cedula cliente: {cedula}")
        print(f"---Información: ")
        print(f"   NOMBRE: {clientes[cedula]['NOMBRE']}")
        print(f"   APELLIDO: {clientes[cedula]['APELLIDO']}")
        print(f"   CORREO: {clientes[cedula]['CORREO']}")
        print(f"   TELEFONO : {clientes[cedula]['TELEFONO']}")
        print(f"   DIRECCION: {clientes[cedula]['DIRECCION']}")
        print(f"   PREFERENCIAL : {'Preferencial' if clientes[cedula]['PREFERENCIAL'] else 'No preferencial'}")
    else:
        print(f"Cliente con cédula {cedula} no encontrado.")

def obtener_una_opcion():
    while True:
        try:
            opcion = int(input("Seleccione una opción: "))
            if 1 <= opcion <= 6:
                return opcion
            else:
                print("Opción no válida. Intente nuevamente.")
        except ValueError:
            print("Error: Debe ingresar un número.")

def pausar():
    input("\nDigite cualquier botón para continuar...")

def main():
    while True:
        print("\n")
        imprimir_menu()
        opcion = obtener_una_opcion()
        if opcion == 1:
            registrar_cliente()
            pausar()
        elif opcion == 2:
            eliminar_cliente()
            pausar()
        elif opcion == 3:
            cedula = int(input("\nIngrese la cédula del cliente: "))
            visualizar_cliente(cedula)
            pausar()
        elif opcion == 4:
            listar_clientes()
            pausar()
        elif opcion == 5:
            listar_preferenciales()
            pausar()
        elif opcion == 6:
            print("Saliendo del sistema")
            break

if __name__ == "__main__":
    main()