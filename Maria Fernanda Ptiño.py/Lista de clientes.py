#Diccionario para almacenar los clientes
clientes = {
}

def obtener_opcion():
    while True: 
        try:
            opcion = input('Seleccione una opción: ').strip()
            if opcion == '':  # Si está vacío
                continue
            opcion = int(opcion)
            if 1 <= opcion <= 6:
                return opcion
            print('Por favor, ingrese una opción válida (1-6).')
        except ValueError:
            print('Error: Debe ingresar un número. Intente nuevamente.')

def mostrar_menu():
    print('✨✨ ------------------------------✨✨')
    print('------- Bienvenido al registro -------')
    print('✨✨ ------------------------------✨✨')
    print('[1] ➕   Registrar un cliente') 
    print('[2] 🗑️   Eliminar un cliente')
    print('[3] 🖋️   Buscar un cliente')
    print('[4] 🔎   Lista de clientes')
    print('[5] 🔎   Lista de clientes preferenciales')
    print('[6] 👣   Salir')
    print('✨✨ ------------------------------✨✨')
def pausar():
    input("\nPresione Enter para continuar...")



def registrar_clientes():
    try:
        cedula = int(input('\nIngrese la cédula del cliente: '))
        if cedula in clientes:
            print('⚠️ El cliente ya existe. Ingrese otra cédula.')
        else:
            nombre = input('Ingrese el nombre: ').title()
            apellido = input('Ingrese el apellido: ').title()
            correo = input ('Ingrese el correo: ').title ()
            telefono = input ('Ingrese el telefono: ').title ()
            direccion = input ('Ingrese la direccion: ').title ()
            #Lower: Convierte todos los caracteres de una cadena a minúsculas.Es útil para comparar cadenas de texto de manera insensible a mayúsculas y minúsculas
            preferencial = input('¿Es cliente preferencial? (s/n): ').lower() 
            if preferencial == 's':  #saber si el cliente es preferencial
                preferencial = True
            else:
                preferencial = False
            # Agregar el cliente al diccionario
            clientes [cedula] = {
                'nombre': nombre,
                'apellido': apellido,
                'correo': correo,
                'telefono': telefono,
                'direccion': direccion,
                'preferencial': preferencial
        
            }
            print(f'✅ Cliente {nombre} {apellido} agregado exitosamente!')
    except ValueError:
        print('❌ Error: La cédula debe ser un número entero.')
    pausar()

def eliminar_cliente():
    try:
        cedula = int(input('\nIngrese la cédula del cliente: '))
        if cedula not in clientes:
            print('⚠️ El cliente No existe. Por favor registre el cliente primero.')
            return
        #del: eliminar elementos de un diccionario (o cualquier otra estructura de datos mutable, como listas). En el caso de los diccionarios, se puede
        # usar del para eliminar una clave y su valor asociado.
        del clientes[cedula] 
        print(f'✅ Cliente con cédula {cedula} eliminado exitosamente!')    
    except ValueError:
        print('❌ Error: La cédula debe ser un número entero.')
    pausar()

def buscar_cliente():
    try:
        cedula = int(input('\nIngrese la cédula del cliente: '))
        if cedula not in clientes:
            print('⚠️ El cliente no existe. Por favor registre el cliente primero.')
            return
        
        cliente = clientes[cedula]  # Obtiene todos los datos del cliente
        if cliente:
            print('✨✨ ------------------------------✨✨')
            print('------- Clientes Encontrado -------')
            print('✨✨ ------------------------------✨✨')
            for cedula, cliente in clientes.items():
                print(f"Cliente: {cliente['nombre']} {cliente['apellido']}")
                print(f"Correo: {cliente['correo']}")
                print(f"Teléfono: {cliente['telefono']}")
                print(f"Dirección: {cliente['direccion']}")
                print(f"Preferencial: {'✅ Sí' if cliente['preferencial'] else '❌ No'}")
                print('-----------------------------------')     
    except ValueError:
        print('❌ Error: La cédula debe ser un número entero.')
    pausar()

def listar_clientes(): 
    if not clientes:
        print('⚠️ No hay clientes registrados.')
    else:
            print('✨✨ ------------------------------✨✨')
            print('------- Lista de clientes -------')
            print('✨✨ ------------------------------✨✨')
            for cedula, cliente in clientes.items():
                print(f"Cliente: {cliente['nombre']} {cliente['apellido']}")
                print(f"Correo: {cliente['correo']}")
                print(f"Teléfono: {cliente['telefono']}")
                print(f"Dirección: {cliente['direccion']}")
                print(f"Preferencial: {'Sí' if cliente['preferencial'] else 'No'}")
                print('-----------------------------------')
                pausar ()

def listar_clientes_preferenciales():
    preferenciales = [cliente for cliente in clientes.values() if cliente['preferencial']] #Filtra los clientes que tienen el valor True en la clave 'preferencial'.
#Solo los clientes preferenciales serán incluidos en la nueva lista.

    if not preferenciales:
        print('⚠️ No hay clientes preferenciales registrados.')
    else:
        print('✨✨ ------------------------------✨✨')
        print('------- Lista de clientes -------')
        print('✨✨ ------------------------------✨✨')
        for cliente in preferenciales:
            print(f"Cliente: {cliente['nombre']} {cliente['apellido']}")
            print(f"Correo: {cliente['correo']}")
            print(f"Teléfono: {cliente['telefono']}")
            print(f"Dirección: {cliente['direccion']}")
            print('-----------------------------------')
    pausar()


def main():
    while True:
        mostrar_menu()
        opcion = obtener_opcion()
        
        if opcion == 1:
            registrar_clientes()
        elif opcion == 2:
            eliminar_cliente()
        elif opcion == 3:
            buscar_cliente()
        elif opcion == 4:
            listar_clientes()
        elif opcion == 5:
            listar_clientes_preferenciales()
        elif opcion == 6:
            print('\n👋 ¡Hasta luego! Gracias por usar el sistema.')
            break

if __name__ == "__main__":
    main()