import math

print("Bienvenido a la calculadora recibe una impedancia (parte real, parte imaginaria y la frecuencia de trabajo) y te dice si es:")
print("--------------------------")
print("*RESISTENCIA*\n*CAPACITOR*\n*INDUCTOR*")
print("--------------------------\n")
print("Porfavor, ingrese los numeros correspondientes de la impedancia:")

Real = float(input("Parte Real (Ohms): "))
Imaginario = float(input("Parte Imaginario (Ohms): "))
Frecuencia = float(input("Frecuencia de trabajo (Hz): "))

Capacitor = -1/(2*math.pi*Imaginario*Frecuencia)
Inductor = Imaginario/(2*math.pi*Frecuencia)

if (Imaginario<0):
    print(f"Se trata de un capacitor de: {Capacitor}F")
    print(f"El valor de la resistencia es de: {Real} Ohms")
    
elif Imaginario > 0:
    print(f"Se trata de un Inductor de: {Inductor} H")
    print(f"El valor de la resistencia es de: {Real} Ohms")
    
else:
    print(f"Se trata de un resistor de: {Real} Ohms")