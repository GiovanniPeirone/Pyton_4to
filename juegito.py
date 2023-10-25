import random
from colorama import Fore
from os import system

#--------------------------------------------------------------------------------------

def menuAtaque():
    mA = '''
    1-Ataque
    2-Escapar
    '''
    print(mA)

#---------------------------------------------------------------------------------------

def e1():
    modeloE1 = '''
                                             .            .
       
                                         ---------------------/'''
    print(modeloE1)
    print("vida:",Enemigo1.vida)
    print("ataque:",Enemigo1.ataque)
    print("escudo:",Enemigo1.escudo)
    


def p1():
    modepoP1 = '''
          --
          --
         ----
         -  -
         -  - 
         ----
         -  -
         -  -
       ---  ---'''
    print(modepoP1)
    print("vida:",personaje1.vida)
    print("ataque:",personaje1.ataque)
    print("escudo:",personaje1.escudo)

def p2():
    modepoP2 = '''
          33
          33
         !--!
         !  !
         -  - 
         ----
         !  !
         !  !
       ---  ---'''
    print(modepoP2)
    print("vida:",personaje1.vida)
    print("ataque:",personaje1.ataque)
    print("escudo:",personaje1.escudo)
    
#--------------------------------------------------------------------------------

class personaje:

    

    def __init__(self, vida, ataque, escudo):
        self.vida = vida
        self.ataque = ataque
        self.escudo = escudo


class enemigo:

    def __init__(self, vida, ataque, escudo):
        self.vida = vida
        self.ataque = ataque
        self.escudo = escudo


#-------------------------------------------------------------------------------

personaje1 = personaje(100, 33, 0)
personaje2 = personaje(75, 50, 0)
Enemigo1 = enemigo(100, 20, 0)


while True:
    try:
        print("personaje1")
        print()
        p1()
        print("personaje2")
        print()
        p2()
    
        per = int(input("seleccione un personaje(1/2):"))

        if per == 1:
            per = personaje1
            m = p1()
            break

        elif per == 2:
            per = personaje2
            m = p2()
            break

        else:
            print("ese personaje no existe")

    except ValueError:
        print("tonto")

while True:
    try:
        system("cls")
        print("AAAAAAAAAAAAAAAAAAAAAA")
        e1()
        
        menuAtaque()

        o = int(input(":"))

        if o == 1:
            Enemigo1.vida = Enemigo1.vida - per.ataque

        if o == 2:
            system("cls")
            print("H a s   E s c a p a d o")
            break

        if Enemigo1.vida <= 0:
            system("cls")
            print("H a s  G a n a d o")
            break
    

    except ValueError:
        print("tonto")
    

    

    


        
