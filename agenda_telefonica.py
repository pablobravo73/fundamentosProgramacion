agenda = {}

def agregar_contacto(nombre, telefono):
    if nombre in agenda:
        print(f'El contacto {nombre} ya existe en la agenda.')
        return
    elif not telefono.isdigit() or len(telefono) != 10:
        print('El número de teléfono debe contener exactamente 10 dígitos.')
        return
    else:
        agenda[nombre] = telefono
    print(f"Contacto {nombre} agregado.")

def eliminar_contacto(nombre):
    if nombre in agenda:
        del agenda[nombre]
        print(f"Contacto {nombre} eliminado.")
    else:
        print(f"No se encontró el contacto {nombre}.")

def actualizar_contacto(nombre, nuevo_telefono):
    if nombre in agenda:
        agenda[nombre] = nuevo_telefono
        print(f"Contacto {nombre} actualizado.")
    else:
        print(f"No se encontró el contacto {nombre}.")

def buscar_contacto_por_nombre(nombre):
    if nombre in agenda:
        print(f"Nombre: {nombre}, Teléfono: {agenda[nombre]}")
        return True
    else:
        print(f"No se encontró el contacto {nombre}.")
        return False

def buscar_contacto_por_numero(telefono):
    encontrado = False
    for nombre, num in agenda.items():
        if num == telefono:
            print(f"Nombre: {nombre}, Teléfono: {telefono}")
            encontrado = True
    if not encontrado:
        print(f"No se encontró ningún contacto con el número {telefono}.")

def mostrar_contactos():
    if agenda:
        print("Lista de contactos:")
        for nombre, telefono in agenda.items():
            print(f"Nombre: {nombre}, Teléfono: {telefono}")
    else:
        print("La agenda está vacía.")

def ingresar_multiples_contactos():
    while True:
        nombre = input("Ingrese el nombre del contacto: ")
        telefono = input("Ingrese el teléfono del contacto: ")
        agregar_contacto(nombre, telefono)
        decide = input('¿Desea agregar otro contacto?: si/no ')
        if decide.lower() != 'si':
            break

while True:
    print(
    '''
    ------------
    | Opciones |
    ------------

    1. Agregar contacto
    2. Eliminar contacto
    3. Actualizar contacto  
    4. Buscar contacto por nombre
    5. Mostrar todos los contactos
    6. Agregar múltiples contactos
    7. Buscar contacto por numero
    8. Salir
    ''')

    opcion = input("Ingrese el número de la opción que desee: ")

    if opcion == "1":
        nombre = input("Ingrese el nombre del contacto: ")
        telefono = input("Ingrese el teléfono del contacto: ")
        agregar_contacto(nombre, telefono)
    elif opcion == "2":
        nombre = input("Ingrese el nombre del contacto que desea eliminar: ")
        eliminar_contacto(nombre)
    elif opcion == "3":
        nombre = input("Ingrese el nombre del contacto que desea actualizar: ")
        nuevo_telefono = input("Ingrese el nuevo teléfono: ")
        actualizar_contacto(nombre, nuevo_telefono)
    elif opcion == "4":
        nombre = input("Ingrese el nombre del contacto que desea buscar: ")
        buscar_contacto_por_nombre(nombre)
    elif opcion == "5":
        mostrar_contactos()
    elif opcion == "6":
        ingresar_multiples_contactos()
    elif opcion =='7':
        telefono = input("Ingrese el numero del contacto que desea buscar: ")
        if not telefono.isdigit() or len(telefono) != 10:
            print(f'{telefono} no es una opción válida')
        else:
            buscar_contacto_por_numero(telefono)
    elif opcion == "8":
        print("¡Hasta luego!")
        break
    else:
        print("Opción no válida. Por favor, elija una opción válida.")
