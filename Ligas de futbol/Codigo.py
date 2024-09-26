import os

def Limpiar_pantalla():
    os.system('clear')  # Para Windows, usa 'cls'

class Liga:
    def __init__(self, Nombre, Pais, Cantidad):
        self.Nombre = Nombre
        self.Pais = Pais
        self.Cantidad = Cantidad
        
    def Mostrar(self):
        print(f"Nombre: {self.Nombre}\nPaís: {self.Pais}\nCantidad de equipos: {self.Cantidad}")

class Competencia:
    def __init__(self):
        self.Ligas = []
    
    def Agregar_liga(self, Liga):
        self.Ligas.append(Liga)
        print("Liga agregada correctamente")
    
    def Eliminar_liga(self, Nombre):
        for liga in self.Ligas:
            if liga.Nombre == Nombre:
                self.Ligas.remove(liga)
                print("Liga eliminada")
                return
        print(f"No se encontró la liga con nombre '{Nombre}'")
    
    def Mostrar_Ligas(self):
        if self.Ligas:
            print("En la competencia tenemos estas ligas:")
            for liga in self.Ligas:
                liga.Mostrar()
        else:
            print("La competencia está vacía")

competencia = Competencia()

def Menu():
    while True:
        Limpiar_pantalla()  # Limpia la pantalla al inicio del menú
        print("Bienvenidos a la competencia de fútbol, aquí puedes ver, agregar o eliminar ligas")
        print("-----------------------------")
        print("1) Ver ligas\n2) Agregar liga nueva\n3) Eliminar liga\n4) Salir")
        print("-----------------------------")
        opcion = int(input("La opción es: "))
        
        if opcion == 1:
            competencia.Mostrar_Ligas()
        
        elif opcion == 2:
            Nombre = input("Ingresa el nombre de la liga: ")
            Pais = input("El país donde se juega la liga: ")
            Cantidad = input("¿Cuántos equipos participan?: ")
            Nueva_liga = Liga(Nombre, Pais, Cantidad)
            competencia.Agregar_liga(Nueva_liga)
        
        elif opcion == 3:
            Nombre = input("Ingresa el nombre de la liga que deseas eliminar: ")
            competencia.Eliminar_liga(Nombre)
        
        elif opcion == 4:
            print("Gracias por su atención. ¡Hasta pronto!")
            break
        else:
            print("Opción no válida, por favor intenta nuevamente.")

Menu()
