import os
import time
import json 

def limpiar_pantalla():
        os.system('clear')

print("Hola bienvenido al programa donde puedes guardar tus series favoritas!\n")

Series = []

while True:
    try:
        Opcion = int(input("Opcion n°1: Cargar una nueva serie\nOpcion n°2: Ver todas las series cargadas\nOpcion n°3: Salir\nTu opcion elegida es: "))
    except ValueError:
        print("Por favor, ingresa un número válido.")
        continue

    if Opcion == 1:
        limpiar_pantalla()
        print("Te pediré los siguientes datos\n")
        Nombre_serie = input("Nombre de la serie: ")
        Capitulos = input("Cantidad de capítulos: ")
        Temporadas = input("Cantidad de temporadas: ")

        Serie = {
            "Nombre de la serie": Nombre_serie,
            "Cantidad de capitulos": Capitulos,
            "Cantidad de temporadas": Temporadas,
        }
        Series.append(Serie)
        print("Serie agregada\n")

    elif Opcion == 2:
        limpiar_pantalla()
        if len(Series) > 0:
            print("Lista de series:\n")
            for indice, Serie in enumerate(Series, 1):
                print(f"Serie #{indice}:")
                print(f"Nombre: {Serie['Nombre de la serie']}")
                print(f"Capítulos: {Serie['Cantidad de capitulos']}")
                print(f"Temporadas: {Serie['Cantidad de temporadas']}\n")
        else:
            print("No hay series en la lista.")
        input("Presiona Enter para continuar...\n")

    elif Opcion == 3:
        print("Gracias por usar el programa")
        with open("Mis_series.txt", "w") as F:
            json.dump(Series, F, indent=4)  
        break

    else:
        print("Opción no válida, por favor elige una opción del 1 al 3.")

