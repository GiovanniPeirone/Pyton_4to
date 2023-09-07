import random
import colorsys
from colorama import Fore,Back
from time import sleep
from colorama import Cursor
print(Fore.GREEN + "Recursos Python")
print(Fore.BLUE)

def menu():
    lista = """
    ..............
    . 1.comenzar .
    . 2.salir    .
    ..............

    """
    print(lista)
menu()
print(Fore.YELLOW)
val1 = int(input(Fore.YELLOW + "ingrese la opcion:"))

if val1 >= 2:
    print("adios")
    exit
elif val1 <= 1:
    numeroR = random.randint(1,10)
    listaN = []
    while True:
        try:
            print()
            print(Fore.CYAN+ f"numeros anteriores:{listaN}")
            numeroUser = int(input(Fore.YELLOW + "Ingrese un numero ENTRE 1 Y 10:"))
            print()
            if numeroUser == numeroR:
                print(Fore.GREEN + "GANASTE")
                print(Fore.GREEN + f"El NUMERO GANADOR: {numeroUser}")
                break
            elif numeroUser > numeroR:
                print(Fore.RED + "el numero se mas chico")
            elif numeroUser < numeroR:
                print(Fore.RED + "el numero se mas grande")

            listaN.append(numeroUser)
        except ValueError:
            print(Fore.RED + Fore.RED)
            print("HAY UNA MANERA DE HACRLO MAL Y VOS LA HICISTE")





