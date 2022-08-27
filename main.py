from ColaSecuencial import ColaSecuencial
from ColaEncadenada import ColaEncadenada

if __name__ == "__main__":
    unaCola = ColaSecuencial(5)
    opcion = -1
    while opcion != "0":
        print("Seleccione")
        print("[0] Salir")
        print("[1] Insertar numero")
        print("[2] Suprimir numero")
        opcion = input("--> ")

        if opcion == "1":
            elemento = int(input("Ingresa el numero: "))
            unaCola.insertar(elemento)
        
        elif opcion == "2":
            print(unaCola.suprimir())
        