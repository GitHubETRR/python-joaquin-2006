class Contacto:
    def __init__(self, nombre, telefono, email):
        self.nombre = nombre
        self.telefono = telefono
        self.email = email
    
    def mostrar_informacion(self):
        print(f"Nombre: {self.nombre}")
        print(f"Teléfono: {self.telefono}")
        print(f"Email: {self.email}")

class Agenda:
    def __init__(self):
        self.contactos = {}
    
    def añadir_contacto(self, nombre, telefono, email):
        if nombre in self.contactos:
            print("Error: El contacto ya existe.")
        else:
            nuevo_contacto = Contacto(nombre, telefono, email)
            self.contactos[nombre] = nuevo_contacto
            print(f"Contacto '{nombre}' añadido.")
    
    def eliminar_contacto(self, nombre):
        if nombre in self.contactos:
            del self.contactos[nombre]
            print(f"Contacto '{nombre}' eliminado.")
        else:
            print("Error: El contacto no existe.")
    
    def buscar_contacto(self, nombre):
        if nombre in self.contactos:
            self.contactos[nombre].mostrar_informacion()
        else:
            print("Error: Contacto no encontrado.")
    
    def mostrar_todos_contactos(self):
        if self.contactos:
            print("\nLista de contactos:")
            for contacto in self.contactos.values():
                contacto.mostrar_informacion()
                print("-----------------------")
        else:
            print("No hay contactos en la agenda.")
    
    def actualizar_contacto(self, nombre, nuevo_telefono=None, nuevo_email=None):
        if nombre in self.contactos:
            if nuevo_telefono:
                self.contactos[nombre].telefono = nuevo_telefono
            if nuevo_email:
                self.contactos[nombre].email = nuevo_email
            print(f"Contacto '{nombre}' actualizado.")
        else:
            print("Error: Contacto no encontrado.")


# Menú interactivo
def menu_agenda():
    mi_agenda = Agenda()
    
    while True:
        print("\nAgenda de Contactos")
        print("1. Añadir contacto")
        print("2. Eliminar contacto")
        print("3. Buscar contacto")
        print("4. Mostrar todos los contactos")
        print("5. Actualizar contacto")
        print("6. Salir")
        
        opcion = input("Elige una opción: ")
        
        if opcion == '1':
            nombre = input("Nombre: ")
            telefono = input("Teléfono: ")
            email = input("Email: ")
            mi_agenda.añadir_contacto(nombre, telefono, email)
        
        elif opcion == '2':
            nombre = input("Nombre del contacto a eliminar: ")
            mi_agenda.eliminar_contacto(nombre)
        
        elif opcion == '3':
            nombre = input("Nombre del contacto a buscar: ")
            mi_agenda.buscar_contacto(nombre)
        
        elif opcion == '4':
            mi_agenda.mostrar_todos_contactos()
        
        elif opcion == '5':
            nombre = input("Nombre del contacto a actualizar: ")
            nuevo_telefono = input("Nuevo teléfono (o presiona Enter para mantener el actual): ")
            nuevo_email = input("Nuevo email (o presiona Enter para mantener el actual): ")
            mi_agenda.actualizar_contacto(nombre, nuevo_telefono or None, nuevo_email or None)
        
        elif opcion == '6':
            print("Saliendo de la agenda.")
            break
        
        else:
            print("Opción no válida. Intente de nuevo.")

menu_agenda()

