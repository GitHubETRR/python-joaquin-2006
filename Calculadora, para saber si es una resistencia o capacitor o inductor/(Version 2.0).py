import math
import os
import time

def limpiar_pantalla():
    os.system('clear')

print("Bienvenido a la calculadora recibe una impedancia (parte real, parte imaginaria y la frecuencia de trabajo) y te dice si es:")
print("--------------------------")
print("*RESISTENCIA*\n*CAPACITOR*\n*INDUCTOR*")
print("--------------------------")
print("Espere........")
time.sleep(8)

while True:
    while True:
        limpiar_pantalla()
        print("Porfavor, ingrese los numeros correspondientes de la impedancia:\n")
                    
        Real = float(input("Parte Real (Ohms): "))
        Imaginario = float(input("Parte Imaginario (Ohms): "))
        Frecuencia = float(input("Frecuencia de trabajo (Hz): "))
                    
        if (Imaginario<0):
            if Frecuencia != 0:
                Capacitor = 1 / (2 * math.pi * abs(Imaginario) * Frecuencia)
                print(f"\nSe trata de un capacitor de: {Capacitor} F")  #
                print(f"El valor de la resistencia es de: {Real} Ohms\n")
                break
            else:
                print("\nError: La frecuencia no puede ser 0 para calcular un capacitor.")
                time.sleep(5)
            
        elif Imaginario > 0:
            Inductor = Imaginario/(2*math.pi*Frecuencia)
            print(f"\nSe trata de un Inductor de: {Inductor} H")
            print(f"El valor de la resistencia es de: {Real} Ohms\n")
            break
                        
        else:
            print(f"\nSe trata de un resistor de: {Real} Ohms\n")
            break
        
    while True:
        Opcion = input("¿Desea continuar?\n1) Sí\n2) No\nSu opción es: ")
        if Opcion == '1':
            break  
        elif Opcion == '2':
            print("Gracias por usar el programa.")
            exit()  
        else:
            print("Opción no válida. Por favor, ingrese 1 o 2.")