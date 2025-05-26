clientes = {
    123:{
        "NOMBRE" : "jhon",
        "APELLIDO" : "mendez",
        "CORREO" : "jhon@gmail.com",
        "TELEFONO" : "32145859",
        "DIRECCION" : "calle falsa 123",
        "PREFERENCIAL" : False
       },
    456:{
        "NOMBRE" : "juan",
        "APELLIDO" : "pere",
        "CORREO" : "juan@gmail.com",
        "TELEFONO" : "32445859",
        "DIRECCION" : "calle falsa 456",
        "PREFERENCIAL" : True
    }
}


def menu():
  menu = """
  ------REGISTRO DE CLIENTES UNISALLE----
  1. REGISTRAR UN CLIENTE
  2. ELIMINAR UN CLIENTE
  3. BUSCAR UN CLIENTE
  4. LISTAR CLIENTES
  5. LISTAR CLIENTES PREFERENCIALES
  6. SALIR DEL SISTEMA
  SELECCIONE UNA OPCION:
  ---------
  """
  print(menu)

def registrar_cliente():
    print("ingresa datos y separa con comas \n NOMBRE,APELLIDO,CORREO,TELEFONO,DIRECCION,PREFERENCIAL(SI O NO)")
    datos = input("datos: ").split(",")
    cedula = input("digite la cedula del cliente porfavor: ")
    if not cedula.isdigit():
        print("La cédula debe ser un número.")
        return
    cedula = int(cedula)
    if cedula in clientes:
        print("este cliente ya existe")
        return 
    if len(datos) != 6:
        print("Error: Faltan datos")
        return
    clientes[cedula] = {
        "NOMBRE": datos[0].strip(),
        "APELLIDO": datos[1].strip(),
        "CORREO": datos[2].strip(),
        "TELEFONO": datos[3].strip(),
        "DIRECCION": datos[4].strip(),
        "PREFERENCIAL": datos[5].strip().lower() in ["si", "true"]
    }
    print("ya ingresaste el nuevo usuario \n")

def eliminar_cliente():
    cedula = input("ingresa al cliente que quieres eliminar por medio de la cedula: ")
    if cedula.isdigit():
        cedula = int(cedula)
        if cedula in clientes:
            del clientes[cedula]
            print("persona eliminada")
        else:
            print("cliente no encontrado")
    else:
        print("Cédula inválida")
       

def listar_clientes():
    print("----- lista de cliente-----")
    for cedula, informacion in clientes.items():
        buscar_cliente(cedula)

def listar_preferenciales():
    print("-------------- lista de personas prefereniales -----------------")
    for cedula, info in clientes.items():
       if info["PREFERENCIAL"]:
          buscar_cliente(cedula)

def buscar_cliente(cedulaCliente):
    if cedulaCliente in clientes:
        print(f"Cedula cliente: {cedulaCliente}")
        print(f"---Información: ")
        print(f"   NOMBRE: {clientes[cedulaCliente]['NOMBRE']}")
        print(f"   APELLIDO: {clientes[cedulaCliente]['APELLIDO']}")
        print(f"   CORREO: {clientes[cedulaCliente]['CORREO']}")
        print(f"   TELEFONO : {clientes[cedulaCliente]['TELEFONO']}")
        print(f"   DIRECCION: {clientes[cedulaCliente]['DIRECCION']}")
        print(f"   PREFERENCIAL : {   'Preferencial' if (clientes[cedulaCliente]['PREFERENCIAL']) else 'no preferencial'  }  ")
    else:
       print("no se encontro el cliente")

def validar_opcion(op): return op in "123456"

if __name__ == '__main__':
   bandera = True
   while bandera:
        menu()
        opcion = input("selecciona una opción porfavor: ")
        if not validar_opcion(opcion):
            print("Opción inválida")
            continue

        if opcion == "1":
          registrar_cliente()
        elif opcion == "2":
            eliminar_cliente()
        elif opcion == "3":
            cedula = input("Ingrese la cédula del cliente: ")
            buscar_cliente(int(cedula))
        elif opcion == "4":
          listar_clientes()
        elif opcion == "5":
          listar_preferenciales()
        elif opcion == "6":
            bandera = False 
            print("Saliendo muchas gracias")    