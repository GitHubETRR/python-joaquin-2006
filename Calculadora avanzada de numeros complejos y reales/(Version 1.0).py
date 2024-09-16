print("Bienvenido Isi, al programa que funciona como calculadora y lo ayudará con operaciones matemáticas")
Nombre_docente = input("Antes de que arranque el programa, ¿cómo quiere que lo llame?: ")
print(f"Bienvenido {Nombre_docente}, ahora sí, puede usar la calculadora:")

while True:
    Opcion = input("1: Sumar\n2: Restar\n3: Multiplicación\n4: Exponente\n5: División (real)\n6: División (entera)\n7: Operador módulo\n8: Salir\nTu opción elegida fue: ")
    
    if Opcion == '1':  
        print("Opción: Sumar")
        numeros = input("Ingresa los números que quieres sumar, separados por espacio: ")
        lista_numeros = [float(n) for n in numeros.split()]  
        resultado = sum(lista_numeros)
        print(f"El resultado de la suma es: {resultado}")

    elif Opcion == '2':  
        print("Opción: Restar")
        numeros = input("Ingresa los números que quieres restar con el signo negativo o postivo, separados por espacio: ")  
        lista_numeros = [float(n) for n in numeros.split()]  
    
        if len(lista_numeros) > 0:
            resultado = lista_numeros[0]  
            for n in lista_numeros[1:]:  
                resultado = resultado - n
            print(f"El resultado de la resta es: {resultado}")
        else:
            print("No ingresaste ningún número para restar.")
    
    elif Opcion == '3':
        print("Opcion: multiplicacion")
        numeros = input("Ingresa los números que quieres multiplicar, separados por espacio: ")  
        lista_numeros = [float(n) for n in numeros.split()]  
        
        if len(lista_numeros) > 0:
            resultado = lista_numeros[0]  
            for n in lista_numeros[1:]:  
                resultado = resultado * n
            print(f"El resultado de la multiplicacion es: {resultado}")
        else:
            print("no ingresaste ninung numero para multiplicar")
    
    elif Opcion == '4':
        print("Opcion: exponente")
        numeros = input("el primer numero es la base y el segundo es el expoenente, luego el tercer numero sera el exponente del resultado anterior y asi sucesivamente, separados por espacio: ")  
        lista_numeros = [float(n) for n in numeros.split()] 
        
        if len(lista_numeros) > 0:
            resultado = lista_numeros[0]  
            for n in lista_numeros[1:]:  
                resultado = resultado ** n
            print(f"El resultado de la resta es: {resultado}")
        else:
            print("No ingresaste ningún número para usar el exponente.")
    
    elif Opcion == '5':
        print("Opcion: division (real)")
        numeros = input("el primer numero sera dividido por el segundo numero, y el tercer numero divide el resultado anterior y asi sucesivamente, separados por espacio: ")  
        lista_numeros = [float(n) for n in numeros.split()] 
        
        if len(lista_numeros) > 0:
            resultado = lista_numeros[0]  
            for n in lista_numeros[1:]:  
                resultado = resultado / n
            print(f"El resultado de la division es: {resultado}")
        else:
            print("No ingresaste ningún número para usar realizar la division.")

    elif Opcion == '6':
        print("Opcion: division (entera)")
        numeros = input("el primer numero sera dividido por el segundo numero, y el tercer numero divide el resultado anterior y asi sucesivamente, separados por espacio: ")  
        lista_numeros = [float(n) for n in numeros.split()] 
        
        if len(lista_numeros) > 0:
            resultado = lista_numeros[0]  
            for n in lista_numeros[1:]:  
                resultado = resultado // n
            print(f"El resultado de la division es: {resultado}")
        else:
            print("No ingresaste ningún número para usar realizar la division.")
            
    elif Opcion == '7':
        print("Opcion: operador modulo")
        numeros = input("el primer numero sera dividido por el segundo numero, y el tercer numero divide el resultado anterior y asi sucesivamente, separados por espacio: ")  
        lista_numeros = [float(n) for n in numeros.split()] 
        
        if len(lista_numeros) > 0:
            resultado = lista_numeros[0]  
            for n in lista_numeros[1:]:  
                resultado = resultado % n
            print(f"El resto de la division es: {resultado}")
        else:
            print("No ingresaste ningún número para usar realizar la division.")
            
    elif Opcion == '8':  
        print("Saliendo del programa")
        break
    
    else:
        print("Opción no válida, por favor elija una opción del menú.")
