clientes = {}

def menu():
    print("""
    ------REGISTRO DE CLIENTES UNISALLE----
    1. REGISTRAR UN CLIENTE
    2. ELIMINAR UN CLIENTE
    3. BUSCAR UN CLIENTE
    4. LISTA DE CLIENTES
    5. LISTA DE CLIENTES PREFERENCIALES
    6. SALIR DEL SISTEMA
    ---------------------------------------
    """)

def registrar_cliente():
    try:
        cedula = int(input("Digite la cédula del cliente: "))
        if cedula in clientes:
            print("Este cliente ya está registrado.")
            return
        nombre = input("Nombre: ")
        apellido = input("Apellido: ")
        correo = input("Correo: ")
        telefono = input("Teléfono: ")
        direccion = input("Dirección: ")
        preferencial = input("¿Es cliente preferencial? (s/n): ").lower() == 's'

        clientes[cedula] = {
            "NOMBRE": nombre,
            "APELLIDO": apellido,
            "CORREO": correo,
            "TELEFONO": telefono,
            "DIRECCION": direccion,
            "PREFERENCIAL": preferencial
        }
        print("Cliente registrado con éxito.")
    except ValueError:
        print("Cédula no válida. Debe ser un número.")

def eliminar_cliente():
    try:
        cedula = int(input("Digite la cédula del cliente a eliminar: "))
        if cedula in clientes:
            del clientes[cedula]
            print("Cliente eliminado con éxito.")
        else:
            print("Cliente no encontrado.")
    except ValueError:
        print("Cédula inválida.")

def buscar_cliente(cedulaCliente=None):
    if cedulaCliente is None:
        try:
            cedulaCliente = int(input("Digite la cédula del cliente a buscar: "))
        except ValueError:
            print("Cédula inválida.")
            return

    if cedulaCliente in clientes:
        print(f"CÉDULA: {cedulaCliente}")
        print(f"   NOMBRE: {clientes[cedulaCliente]['NOMBRE']}")
        print(f"   APELLIDO: {clientes[cedulaCliente]['APELLIDO']}")
        print(f"   CORREO: {clientes[cedulaCliente]['CORREO']}")
        print(f"   TELEFONO: {clientes[cedulaCliente]['TELEFONO']}")
        print(f"   DIRECCION: {clientes[cedulaCliente]['DIRECCION']}")
        print(f"   PREFERENCIAL: {'Sí' if clientes[cedulaCliente]['PREFERENCIAL'] else 'No'}")
    else:
        print("Cliente no encontrado.")

def listar_clientes():
    print("----- LISTA DE CLIENTES -----")
    if not clientes:
        print("No hay clientes registrados.")
    for cedula in clientes:
        buscar_cliente(cedula)

def listar_preferenciales():
    print("----- CLIENTES PREFERENCIALES -----")
    encontrados = False
    for cedula, datos in clientes.items():
        if datos["PREFERENCIAL"]:
            buscar_cliente(cedula)
            encontrados = True
    if not encontrados:
        print("No hay clientes preferenciales registrados.")

if __name__ == '__main__':
    while True:
        menu()
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            registrar_cliente()
        elif opcion == "2":
            eliminar_cliente()
        elif opcion == "3":
            buscar_cliente()
        elif opcion == "4":
            listar_clientes()
        elif opcion == "5":
            listar_preferenciales()
        elif opcion == "6":
            print("Saliendo del sistema...")
            break
        else:
            print("Opción no válida. Intente nuevamente.")