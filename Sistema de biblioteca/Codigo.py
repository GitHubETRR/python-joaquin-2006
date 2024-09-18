import os
import time

def limpiar_pantalla():
    os.system('clear')  

print("¡Bienvenido a la biblioteca de los Viani!")
Nombre_cliente = input("¿Cómo quiere que lo llame?: ")
limpiar_pantalla()

class Libro:
    def __init__(self, titulo, autor, fecha, codigo):
        self.titulo = titulo
        self.autor = autor
        self.fecha = fecha
        self.codigo = codigo 
        
    def mostrar_info(self):
        """Muestra la información del libro en formato legible."""
        print(f"Título: {self.titulo}, Autor: {self.autor}, Año: {self.fecha}, Código: {self.codigo}")

class Biblioteca:
    def __init__(self):
        self.libros = []
        
    def agregar_libro(self, libro):
        """Agrega un libro a la biblioteca."""
        self.libros.append(libro)
        print(f"Libro '{libro.titulo}' agregado correctamente.")
    
    def eliminar_libro(self, codigo):
        """Elimina un libro por código."""
        for libro in self.libros:
            if libro.codigo == codigo:
                self.libros.remove(libro)
                print(f"Libro con el código '{codigo}' eliminado correctamente.")
                return
        print(f"No se encontró el libro con el código '{codigo}'.")

    def buscar_por_titulo(self, titulo):
        """Busca libros por título."""
        libros_encontrados = [libro for libro in self.libros if titulo.lower() in libro.titulo.lower()]
        if libros_encontrados:
            print(f"Libros encontrados con el título '{titulo}':")
            for libro in libros_encontrados:
                libro.mostrar_info()
        else:
            print(f"No se encontraron libros con el título '{titulo}'.")

    def mostrar_todos_los_libros(self):
        """Muestra todos los libros en la biblioteca."""
        if self.libros:
            print("Libros en la biblioteca:")
            for libro in self.libros:
                libro.mostrar_info()
        else:
            print("La biblioteca está vacía.")

biblioteca = Biblioteca()

def menu_principal():
    while True:
        print(f"\n--- Menú de la Biblioteca ---\n")
        print(f"1. Agregar un libro")
        print(f"2. Eliminar un libro por código")
        print(f"3. Buscar un libro por título")
        print(f"4. Mostrar todos los libros")
        print(f"5. Salir\n")

        opcion = input(f"¿Qué se le ofrece, {Nombre_cliente}? (Ingrese el número de la opción): ")

        if opcion == "1":
            titulo = input("Ingrese el título del libro: ")
            autor = input("Ingrese el autor del libro: ")
            fecha = input("Ingrese el año de publicación: ")
            codigo = input("Ingrese el código del libro: ")
            nuevo_libro = Libro(titulo, autor, fecha, codigo)
            biblioteca.agregar_libro(nuevo_libro)

        elif opcion == "2":
            codigo = input("Ingrese el código del libro que desea eliminar: ")
            biblioteca.eliminar_libro(codigo)

        elif opcion == "3":
            titulo = input("Ingrese el título del libro que desea buscar: ")
            biblioteca.buscar_por_titulo(titulo)

        elif opcion == "4":
            biblioteca.mostrar_todos_los_libros()

        elif opcion == "5":
            print(f"¡Gracias por usar la Biblioteca de los Viani, {Nombre_cliente}! Hasta luego.")
            break

        else:
            print("Opción no válida. Por favor, elija una opción del 1 al 5.")

        input("\nPresione Enter para continuar...")
        limpiar_pantalla()

menu_principal()
