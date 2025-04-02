clientes = {
    
    123:{
    "Nombre" : "Noah",
    "Apellido" : "Van Otterdijk",
    "Correo" : "notter29@icloud.com",
    "Telefono" : "3054817414",
    "Direccion" : "Transversal 72 D Bis #42c - 21 sur",
    "Preferencial" : False
    },
    456:{
    "Nombre" : "Daily",
    "Apellido" : "Canoa",
    "Correo" : "Dcano07@gmail.com",
    "Telefono" : "3245407651",
    "Direccion" : "Calle 45 #78 - 3",
    "Preferencial" : False
    }
    
}

opcion = ""

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
  pass

def eliminar_cliente():
    
    cedula = int(input("Digite la cédula del cliente que desea eliminar: "))
    if cedula in clientes:
        cliente = clientes[cedula] 
        print(f"Cliente encontrado: {cliente['Nombre']} {cliente['Apellido']}")
        confirmacion = input("Si desea eliminar el cliente digite si de lo contrario coloque no").strip().lower()
        if confirmacion == "si":
            del clientes[cedula]  
            print(f"Cliente con cédula {cedula} eliminado correctamente.")
        else:
            print("Eliminación cancelada.")
    else:
        print(f"No se encontró un cliente con la cédula {cedula}.")
  
    

def listar_clientes():
  print("----- lista de clientes-----")
  for cedula, informacion in clientes.items():
    print(f"Cedula cliente: {cedula}")
    print(f"---Información--- ")
    print(f"   Nombre: {informacion['Nombre']}")
    print(f"   Apellido: {informacion['Apellido']}")
    print(f"   Correo: {informacion['Correo']}")
    print(f"   Telefono : {informacion['Telefono']}")
    print(f"   Direccion: {informacion['Direccion']}")
    print(f"   Preferencial : {   informacion['Preferencial'] }  ")

def listar_preferenciales():
  pass

def buscar_cliente(cedulaCliente):
    if cedulaCliente in clientes:
      print(f"Cedula cliente: {cedulaCliente}")
      print(f"---Información---")
      print(f"   Nombre: {clientes[cedulaCliente]['Nombre']}")
      print(f"   Apellido: {clientes[cedulaCliente]['Apellido']}")
      print(f"   Correo: {clientes[cedulaCliente]['Correo']}")
      print(f"   Telefono : {clientes[cedulaCliente]['Telefono']}")
      print(f"   Direccion: {clientes[cedulaCliente]['Direccion']}")
      print(f"   Preferencial : {   'Preferencial' if (clientes[cedulaCliente]['Preferencial']) else 'no preferencial'  }  ")


def validar_opcion(dato):
  while(isNumeric(dato)):
    return True





if __name__ == '__main__':
   """while():
        if(opcion == 1):
          pass
        elif(opcion==2):
          pass
        elif(opcion==3):
          pass
        elif(opcion==4):
          listar_clientes()
          pass
        elif(opcion==5):
          pass
        elif(opcion==6):
          pass
        opcion = input()
        if(validar_opcion() != True):
          break
        menu()"""

##buscar_cliente(456)
eliminar_cliente()
listar_clientes()