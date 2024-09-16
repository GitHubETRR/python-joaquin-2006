import math
import os
import time 

def limpiar_pantalla():
    os.system('clear')

print("Bienvenido Isi, al programa que funciona como calculadora y lo ayudará con operaciones matemáticas")
Nombre_docente = input("Antes de que arranque el programa, ¿cómo quiere que lo llame?: ")
limpiar_pantalla()
print(f"Bienvenido {Nombre_docente}, ahora sí, puede usar la calculadora de 4 maneras:\n")
time.sleep(3)

while True:
    Opcion = input("1) Operaciones matematicas\n2) Formato rectangular a formato Polar o Cartesiano\n3) Devolver el numero complejo en formato rectangular\n4) Terminar programa\n\nEliga cual quiere utilizar: ")
    if Opcion == "1":
        limpiar_pantalla()
        print("Eligio la opcion 1: Operaciones matematicas")
        while True:
            Opcion = input("1: Sumar\n2: Restar\n3: Multiplicación\n4: Exponente\n5: División (real)\n6: División (entera)\n7: Operador módulo\n8: Salir\nTu opción elegida fue: ")
            
            if Opcion == '1':  
                limpiar_pantalla()
                print("Opción: Sumar")
                while True:
                    numeros = input("Ingresa los números que quieres sumar, separados por espacio: ")
                    lista_numeros = [float(n) for n in numeros.split()] 
                    if len(lista_numeros) > 0:
                        resultado = sum(lista_numeros)
                        print(f"El resultado de la suma es: {resultado}\n")
                        break
                        time.sleep(5)
                        limpiar_pantalla()
                    else:
                        print("no ingresaste ningun numero")
                        time.sleep(2)
                        limpiar_pantalla()
        
            elif Opcion == '2': 
                limpiar_pantalla()
                print("Opción: Restar")
                while True:
                    numeros = input("Ingresa los números que quieres restar con el signo negativo o postivo, separados por espacio: ")  
                    lista_numeros = [float(n) for n in numeros.split()]  
                    if len(lista_numeros) > 0:
                        resultado = lista_numeros[0]  
                        for n in lista_numeros[1:]:  
                            resultado = resultado - n
                        print(f"El resultado de la resta es: {resultado}\n")
                        print("Espere....")
                        time.sleep(5)
                        limpiar_pantalla()
                        break
                    else:
                        print("No ingresaste ningún número para restar.")
                        time.sleep(2)
                        limpiar_pantalla()
            
            elif Opcion == '3':
                limpiar_pantalla()
                print("Opcion: multiplicacion")
                while True:
                    numeros = input("Ingresa los números que quieres multiplicar, separados por espacio: ")  
                    lista_numeros = [float(n) for n in numeros.split()]  
                    
                    if len(lista_numeros) > 0:
                        resultado = lista_numeros[0]  
                        for n in lista_numeros[1:]:  
                            resultado = resultado * n
                        print(f"El resultado de la multiplicacion es: {resultado}\n")
                        print("Espere.....")
                        time.sleep(5)
                        limpiar_pantalla()
                        break
                    else:
                        print("no ingresaste ninung numero para multiplicar")
                        time.sleep(2)
                        limpiar_pantalla()
            
            elif Opcion == '4':
                limpiar_pantalla()
                print("Opcion: exponente")
                while True:
                    numeros = input("el primer numero es la base y el segundo es el expoenente, luego el tercer numero sera el exponente del resultado anterior y asi sucesivamente, separados por espacio: ")  
                    lista_numeros = [float(n) for n in numeros.split()] 
                    
                    if len(lista_numeros) > 0:
                        resultado = lista_numeros[0]  
                        for n in lista_numeros[1:]:  
                            resultado = resultado ** n
                        print(f"El resultado de la resta es: {resultado}\n")
                        print("Espere.....")
                        time.sleep(5)
                        limpiar_pantalla()
                        break
                    else:
                        print("No ingresaste ningún número para usar el exponente.")
                        time.sleep(2)
                        limpiar_pantalla()
            
            elif Opcion == '5':
                limpiar_pantalla()
                print("Opcion: division (real)")
                while True:
                    numeros = input("el primer numero sera dividido por el segundo numero, y el tercer numero divide el resultado anterior y asi sucesivamente, separados por espacio: ")  
                    lista_numeros = [float(n) for n in numeros.split()] 
                    
                    if len(lista_numeros) > 0:
                        resultado = lista_numeros[0]  
                        for n in lista_numeros[1:]:  
                            resultado = resultado / n
                        print(f"El resultado de la division es: {resultado}\n")
                        print("Espere.....")
                        time.sleep(5)
                        limpiar_pantalla()
                        break
                    else:
                        print("No ingresaste ningún número para usar realizar la division.")
                        time.sleep(2)
                        limpiar_pantalla()
        
            elif Opcion == '6':
                limpiar_pantalla()
                print("Opcion: division (entera)")
                while True:
                    numeros = input("el primer numero sera dividido por el segundo numero, y el tercer numero divide el resultado anterior y asi sucesivamente, separados por espacio: ")  
                    lista_numeros = [float(n) for n in numeros.split()] 
                    
                    if len(lista_numeros) > 0:
                        resultado = lista_numeros[0]  
                        for n in lista_numeros[1:]:  
                            resultado = resultado // n
                        print(f"El resultado de la division es: {resultado}\n")
                        print("Espere.....")
                        time.sleep(5)
                        limpiar_pantalla()
                        break
                    else:
                        print("No ingresaste ningún número para usar realizar la division.")
                        time.sleep(2)
                        limpiar_pantalla()
                    
            elif Opcion == '7':
                limpiar_pantalla()
                print("Opcion: operador modulo")
                while True:
                    numeros = input("el primer numero sera dividido por el segundo numero, y el tercer numero divide el resultado anterior y asi sucesivamente, separados por espacio: ")  
                    lista_numeros = [float(n) for n in numeros.split()] 
                
                    if len(lista_numeros) > 0:
                        resultado = lista_numeros[0]  
                        for n in lista_numeros[1:]:  
                            resultado = resultado % n
                        print(f"El resto de la division es: {resultado}\n")
                        print("Espere.....")
                        time.sleep(5)
                        limpiar_pantalla()
                        break
                    else:
                        print("No ingresaste ningún número para usar realizar la division.")
                        time.sleep(2)
                        limpiar_pantalla()
                    
            elif Opcion == '8': 
                limpiar_pantalla()
                print("Saliendo del programa: (Operaciones matematicas)\n")
                break
            
            else:
                print("Opción no válida, por favor elija una opción del menú.")
                time.sleep(2)
                limpiar_pantalla()
    elif Opcion == "2":
        limpiar_pantalla()
        print("Eligio la opcion 2: Formato rectangular a formato Polar o Cartesiano.\n")
        print("Escriba los numeros del primer numero que corresponda")
        
        Real_1 = float(input("Escribi el numero Real:"))
        Imaginario_1 = float(input("Escribi el numero Imaginario:"))
        
        print("")
        print("Escriba los numeros del segundo numero que corresponda")
        
        Real_2 = float(input("Escribi el numero Real:")) 
        Imaginario_2 = float(input("Escribi el numero Imaginario:"))
        
        Real_total = Real_1 + Real_2
        Imaginario_total = Imaginario_1 + Imaginario_2
        
        while True:
            limpiar_pantalla()
            Opcion_2 = input("Escriba 0 Para ver en formato cartesiano, o 1 para ver en formato polar: ")

            if Opcion_2 == "0":
                print(f"Cartesiano:{Real_total} + j{Imaginario_total}\n")
                break
            
            elif Opcion_2 == "1":
                modulo = math.sqrt(Real_total ** 2 + Imaginario_total ** 2)
                fase = math.atan2(Imaginario_total, Real_total)
                fase_2 = math.degrees(fase)
                print(f"Polar (modulo): {modulo}")
                print(f"Polar (Angulo en rads): {fase}")
                print(f"Polar (Angulo en): {fase_2}°\n")
                break
            
            else:
                print("La opcion que eligio, no es correcta")
                time.sleep(2)
                
    elif Opcion == "3":
        limpiar_pantalla()
        print("Eligio la opcion 3: Devolver el numero complejo en formato rectangular\n")
        
        Modulo = float(input("Escriba el modulo: "))
        Fase = float(input("Escriba su fase: "))
        
        Parte_real = math.cos(Fase*math.pi/180)*Modulo
        Parte_Imaginaria = math.sin(Fase*math.pi/180)*Modulo
        
        print(f"La parte real es: {Parte_real}")
        print(f"La parte imaginaria es: j{Parte_Imaginaria}\n")
        
    elif Opcion == "4":
        print("Programa finalizado")
        break
    else:
        print("La opcion que eligio es incorrecta")
        time.sleep(2)
        limpiar_pantalla()