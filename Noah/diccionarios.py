clientes = {
    123: {
        "Nombre": "Noah",
        "Apellido": "Van Otterdijk",
        "Correo": "notter29@icloud.com",
        "Telefono": "3054817414",
        "Direccion": "Transversal 72 D Bis #42c - 21 sur",
        "Preferencial": False
    },
    456: {
        "Nombre": "Daily",
        "Apellido": "Canoa",
        "Correo": "Dcano07@gmail.com",
        "Telefono": "3245407651",
        "Direccion": "Calle 45 #78 - 3",
        "Preferencial": False
    }
}

def menu():
    menu = """
    -----REGISTRO DE CLIENTES UNISALLE-----
           1. REGISTRAR UN CLIENTE
           2. ELIMINAR UN CLIENTE
           3. BUSCAR UN CLIENTE
           4. LISTAR CLIENTES
           5. LISTAR CLIENTES PREFERENCIALES
           6. SALIR DEL SISTEMA
    ---------SELECCIONE UNA OPCION---------
    """
    print(menu)

def registrar_cliente():
    while True:
        print("\n--- Registrar Cliente ---")
        try:
            cedula = int(input("Ingrese la cédula del cliente: "))
        except ValueError:
            print("Por favor ingrese un número válido para la cédula.")
            continue

        if cedula in clientes:
            print("Ya existe un cliente registrado con esta cédula. Intente con otra.")
            continue

        nombre = input("Nombre del cliente: ").strip()
        apellido = input("Apellido del cliente: ").strip()
        correo = input("Correo electrónico: ").strip()
        telefono = input("Teléfono: ").strip()
        direccion = input("Dirección: ").strip()

        preferencial = input("¿El cliente es preferencial? (s/n): ").strip().lower() == 's'

        clientes[cedula] = {
            "Nombre": nombre,
            "Apellido": apellido,
            "Correo": correo,
            "Telefono": telefono,
            "Direccion": direccion,
            "Preferencial": preferencial
        }

        print(f"Cliente {nombre} {apellido} registrado correctamente.")
        continuar = input("¿Desea registrar otro cliente? (s/n): ").strip().lower()
        if continuar != 's':
            break

def eliminar_cliente():
    cedula = int(input("Digite la cédula del cliente que desea eliminar: "))
    if cedula in clientes:
        cliente = clientes[cedula]
        print(f"Cliente encontrado: {cliente['Nombre']} {cliente['Apellido']}")
        confirmacion = input("Si desea eliminar el cliente digite 'si', de lo contrario coloque 'no': ").strip().lower()
        if confirmacion == "si":
            del clientes[cedula]
            print(f"Cliente con cédula {cedula} eliminado correctamente.")
        else:
            print("Eliminación cancelada.")
    else:
        print(f"No se encontró un cliente con la cédula {cedula}.")

def listar_clientes():
    print("----- Lista de Clientes -----")
    for cedula, informacion in clientes.items():
        print(f"Cédula cliente: {cedula}")
        print(f"---Información---")
        print(f"   Nombre: {informacion['Nombre']}")
        print(f"   Apellido: {informacion['Apellido']}")
        print(f"   Correo: {informacion['Correo']}")
        print(f"   Teléfono: {informacion['Telefono']}")
        print(f"   Dirección: {informacion['Direccion']}")
        print(f"   Preferencial: {'Sí' if informacion['Preferencial'] else 'No'}")

def listar_preferenciales():
    print("----- Lista de Clientes Preferenciales -----")
    clientes_preferenciales = [cliente for cliente in clientes.values() if cliente["Preferencial"]]

    if not clientes_preferenciales:
        print("No hay clientes preferenciales registrados.")
    else:
        for cedula, informacion in clientes.items():
            if informacion["Preferencial"]:
                print(f"Cédula cliente: {cedula}")
                print(f"---Información---")
                print(f"   Nombre: {informacion['Nombre']}")
                print(f"   Apellido: {informacion['Apellido']}")
                print(f"   Correo: {informacion['Correo']}")
                print(f"   Teléfono: {informacion['Telefono']}")
                print(f"   Dirección: {informacion['Direccion']}")
                print(f"   Preferencial: {'Sí' if informacion['Preferencial'] else 'No'}")

def buscar_cliente(cedulaCliente):
    if cedulaCliente in clientes:
        print(f"Cédula cliente: {cedulaCliente}")
        print(f"---Información---")
        print(f"   Nombre: {clientes[cedulaCliente]['Nombre']}")
        print(f"   Apellido: {clientes[cedulaCliente]['Apellido']}")
        print(f"   Correo: {clientes[cedulaCliente]['Correo']}")
        print(f"   Teléfono: {clientes[cedulaCliente]['Telefono']}")
        print(f"   Dirección: {clientes[cedulaCliente]['Direccion']}")
        print(f"   Preferencial: {'Sí' if clientes[cedulaCliente]['Preferencial'] else 'No'}")
    else:
        print(f"No se encontró un cliente con la cédula {cedulaCliente}.")

def validar_opcion(opcion):
    try:
        int(opcion)
        return True
    except ValueError:
        return False

if __name__ == "__main__":
    while True:
        menu()
        opcion = input("Seleccione una opción: ")

        if not validar_opcion(opcion):
            print("Por favor, ingrese un número válido.")
            continue

        opcion = int(opcion)
        if opcion == 1:
            registrar_cliente()
        elif opcion == 2:
            eliminar_cliente()
        elif opcion == 3:
            try:
                cedula = int(input("Ingrese la cédula del cliente que desea buscar: "))
                buscar_cliente(cedula)
            except ValueError:
                print("Por favor, ingrese un número válido para la cédula.")
        elif opcion == 4:
            listar_clientes()
        elif opcion == 5:
            listar_preferenciales()
        elif opcion == 6:
            print("Saliendo del sistema. ¡Gracias por usar el registro de clientes UNISALLE!")
            break
        else:
            print("Opción inválida. Por favor, seleccione una opción entre 1 y 6.")