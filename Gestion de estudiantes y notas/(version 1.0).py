print("Bienvenido Isi, al programa que lo ayudaré a ordenar a sus estudiantes y sus notas")
Nombre_docente = input("Antes de que arranque el programa, ¿cómo quiere que lo llame?: ")
print(f"Bienvenido {Nombre_docente}, ahora sí, puede usar el programa: ")
print("")

estudiantes = []

while True:
    Opcion = input("1: Agregar estudiante\n2: Eliminar estudiante (no implementado)\n3: Ver la lista de estudiantes\n4: Cerrar programa\nElija una opción: ")
    
    if Opcion == "1":
        print("Perfecto, le pediré los siguientes datos: ")
        Nombre_estudiante = input("Nombre: ")
        Apellido_estudiante = input("Apellido: ")
        Edad_estudiante = input("Edad: ")
        Calificacion_estudiante = input("Nota del estudiante: ")
        
        estudiante = {
            "Nombre": Nombre_estudiante,
            "Apellido": Apellido_estudiante,
            "Edad": Edad_estudiante,
            "Calificación": Calificacion_estudiante
        }
        estudiantes.append(estudiante)
        print("Estudiante agregado correctamente.")
        
    elif Opcion == "2":
        print("Aun no")
        
    elif Opcion == "3":
        if len(estudiantes) > 0:
            print("\nLista de estudiantes:")
            for Usuario, estudiante in enumerate(estudiantes, 1):
                print(f"Estudiante {Usuario}:")
                print(f"  Nombre: {estudiante['Nombre']}")
                print(f"  Apellido: {estudiante['Apellido']}")
                print(f"  Edad: {estudiante['Edad']}")
                print(f"  Calificación: {estudiante['Calificación']}\n")
        else:
            print("No hay estudiantes en la lista.")
    elif Opcion == "4":
        print("Gracias por utilizar el programa.")
        break  
    else:
        print("Opción no válida. Por favor, elija una opción del menú.")

#comentarios para no olvidarme:
#Opcion es una cadena de texto (resultado de la función input()), con números enteros (1, 2, 3), es por eso que 1, 2 y 3 se pone como texto