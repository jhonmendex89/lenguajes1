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

opcion = ""

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
  informacion = input("Digite nombre, apellido, correo, telefono, direccion, preferencial (True/False) separados por espacio: ").split(" ")
  cedula = int(input("Digite la cédula: "))
  clientes[cedula] = {
    "NOMBRE": informacion[0],
    "APELLIDO": informacion[1],
    "CORREO": informacion[2],
    "TELEFONO": informacion[3],
    "DIRECCION": informacion[4],
    "PREFERENCIAL": informacion[5].lower() == "true"
  }
  print("Cliente registrado con éxito.\n")

def eliminar_cliente():
  cedula = int(input("Digite la cédula del cliente a eliminar: "))
  if cedula in clientes:
    del clientes[cedula]
    print("Cliente eliminado.\n")
  else:
    print("Cliente no encontrado.\n")

def listar_clientes():
  print("----- Lista de clientes -----")
  for cedula, informacion in clientes.items():
    buscar_cliente(cedula)

def listar_preferenciales():
  print("----- Clientes preferenciales -----")
  for cedula, info in clientes.items():
    if info["PREFERENCIAL"]:
      buscar_cliente(cedula)

def buscar_cliente(cedulaCliente):
   if cedulaCliente in clientes:
      print(f"Cédula cliente: {cedulaCliente}")
      print(f"---Información: ")
      print(f"   NOMBRE: {clientes[cedulaCliente]['NOMBRE']}")
      print(f"   APELLIDO: {clientes[cedulaCliente]['APELLIDO']}")
      print(f"   CORREO: {clientes[cedulaCliente]['CORREO']}")
      print(f"   TELEFONO : {clientes[cedulaCliente]['TELEFONO']}")
      print(f"   DIRECCION: {clientes[cedulaCliente]['DIRECCION']}")
      print(f"   PREFERENCIAL : {'Preferencial' if (clientes[cedulaCliente]['PREFERENCIAL']) else 'No preferencial'}\n")
   else:
      print("Cliente no encontrado.\n")

def isNumeric(valor):
  try:
    int(valor)
    return True
  except:
    return False

def validar_opcion(dato):
  return isNumeric(dato)

if __name__ == '__main__':
    while True:
        menu()
        opcion = input()
        if not validar_opcion(opcion):
            print("Opción inválida.")
            continue
        opcion = int(opcion)
        if opcion == 1:
            registrar_cliente()
        elif opcion == 2:
            eliminar_cliente()
        elif opcion == 3:
            cedula = int(input("Digite la cédula a buscar: "))
            buscar_cliente(cedula)
        elif opcion == 4:
            listar_clientes()
        elif opcion == 5:
            listar_preferenciales()
        elif opcion == 6:
            print("Saliendo del sistema...")
            break
        else:
            print("Opción no válida.\n")
