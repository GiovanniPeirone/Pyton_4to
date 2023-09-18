from colorama import Fore
def menu():
    menu = '''
    -----------------------
    ! 1 - Inisiar secion  ¡
    ! 2 - Registrase      ¡
    ! 3 - Salir           ¡
    -----------------------
    '''
    print(Fore.GREEN + menu)
while True:
    menu()
    opcionMenu = int(input("::"))
    if opcionMenu >= 3:
        print(Fore.CYAN + "Adios")
        break
    elif opcionMenu == 2:
        while True:
            try:
                cuenta = {}

                print(Fore.CYAN + "Registrase") 

                nombre = str(input(Fore.YELLOW + "Ingrese el nombre::"))
                contraseña = str(input(Fore.YELLOW + "Ingrese la contraseña::"))

                cuenta["nombre"] = nombre 
                cuenta["contraseña"] = contraseña

                if cuenta["nombre"] and cuenta["contraseña"] == cuenta["nombre"] and cuenta["contraseña"]:
                    print("Estacuenta ya exixte")
                else:
                    cuentas =  cuenta
                    print(Fore.BLUE + "Registo exitoso")
                    break
            except ValueError:
                print(Fore.RED + "MAL")
    elif opcionMenu == 1:
        while True:
            try:

                print(Fore.CYAN + "Inisiar secion")
                nombreI = str(input(Fore.YELLOW + "Ingrese el nombre::"))
                contraseñaI = str(input(Fore.YELLOW + "Ingrese la contraseña::"))
                if nombreI == cuenta["nombre"] and contraseñaI == cuenta["contraseña"]:
                    print(Fore.BLACK + "Bienvenido")
                    break
                else:
                    print(Fore.RED + "Contraseña o Nombre de usuario incorrectos")
            except ValueError:
                print(Fore.RED + "MAL")
    if opcionMenu == -1:
        print(cuentas)
    


