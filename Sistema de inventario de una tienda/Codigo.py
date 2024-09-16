import os
import time

def limpiar_pantalla():
    os.system('clear')  

print("¡Bienvenido a la tienda Viani!")
Nombre_cliente = input("¿Cómo se llama caballero/a?: ")
limpiar_pantalla()

Objetos = {"Gaseosa": 10, "Galletita": 20, "Chocolate": 10, "Fruta": 20, "Verdura": 20}
Precios = {"Gaseosa": 1000, "Galletita": 250, "Chocolate": 500, "Fruta": 300, "Verdura": 300}
Compras_cliente = {}

print(f"¡Bienvenido {Nombre_cliente}, por favor pase y vea lo que ofrece la tienda Viani!")

while True:
    Opcion = int(input("1) Ver objetos\n2) Ver precios\n3) Tus compras\n4) Ver gastos\n5) Salir de la tienda\n\n¿Qué se le ofrece?: "))
    
    if Opcion == 1:
        limpiar_pantalla()
        print("-------------------------------")
        for objeto, cantidad in Objetos.items():
            print(f"{objeto}: {cantidad} unidades")
        print("-------------------------------")
        
    elif Opcion == 2:
        limpiar_pantalla()
        for objeto, precio in Precios.items(): 
            print(f"{objeto}: ${precio}")
        print("-------------------------------")
    
    elif Opcion == 3:
        limpiar_pantalla()
        print(f"¿Qué quiere llevar, {Nombre_cliente}?")
        while True:
            Objeto_comprado = input("Ingresa el nombre del producto: ").capitalize()
            
            if Objeto_comprado in Objetos:
                print(f"{Objeto_comprado} tiene {Objetos[Objeto_comprado]} unidades disponibles.")
                Cantidad_comprada = int(input(f"¿Cuántas quiere comprar de {Objeto_comprado}?: "))
                
                if Cantidad_comprada <= Objetos[Objeto_comprado]:
                    Objetos[Objeto_comprado] -= Cantidad_comprada
                    
                    if Objeto_comprado in Compras_cliente:
                        Compras_cliente[Objeto_comprado] += Cantidad_comprada
                    else:
                        Compras_cliente[Objeto_comprado] = Cantidad_comprada
                    
                    print(f"Compraste un total de {Cantidad_comprada} {Objeto_comprado}(s)")
                    break
                else:
                    print(f"\nDisculpa {Nombre_cliente}, pero no tenemos suficientes unidades de {Objeto_comprado}.")
            else: 
                print("\nEl objeto no existe en la tienda. Por favor elija otro.")
    
    elif Opcion == 4: 
        limpiar_pantalla()
        if Compras_cliente:
            print("Tus compras:")
            for item, cantidad in Compras_cliente.items():
                print(f"{item}: {cantidad} unidades")
        else:
            print("No has comprado nada.")
        print("-------------------------------")
        
    elif Opcion == 5:
        print("¡Gracias por su visita!")
        break
    
    else:
        print("Opción incorrecta, por favor elija una opción válida.")
