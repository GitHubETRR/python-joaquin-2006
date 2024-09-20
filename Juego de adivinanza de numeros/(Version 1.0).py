import random

Numero_secreto = random.randint(1, 100)
intentos = 0

print("!Bienvenido al juego de adivinanza¡")
print("He pensado en un numero entre 1 y 100")
print("Tiene que adivinar cual es")

while True:
    Numero_eligido = int(input("¿Que numero pense?: "))
    intentos += 1
    
    if Numero_eligido < Numero_secreto:
        print("El numero es mayor")
    elif Numero_eligido > Numero_secreto:
        print("El numero es menor")
    elif Numero_eligido == Numero_secreto:
        print(f"¡Felicidades, adivinaste el numero en un total de: {intentos}")
        break
    else:
        print("No es un numero valido")