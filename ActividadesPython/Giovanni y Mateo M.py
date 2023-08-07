import math

print("hoy vamos a hacer un programa de figuras")


menuInicial = '''
            //////////////////////////////
            //  Elija la figura         //
           //    -Rectangulo  1        //
          //    -Triangulo    2       //
         //    -circulo        3    //
         //     -salir    4          //
        //////////////////////////////
'''

def rectangulo():
    altura= float(input("ingrese ingrese la base del triangulo"))
    base= float(input("ingrese la altura del triangulo"))
    area= base*altura 
    print(F"el rsultado es {area}")

def triangulo():
    altura= float(input("ingrese la altura del triangulo"))
    base= float(input("ingrese la base del trianngulo"))
    area= base*altura /2 
    print(f"el resultado es {area}")

def circulo():
    radio= float(input("ingrese el radio del circulo"))
    base= math.pi*radio**2
    print(f"el resultado es {base }")


def menuInicialDef():
    print(menuInicial)
    opcion = int(input("Elija la opcion: "))
    if  opcion == 1:
        rectangulo()
        
    elif opcion == 2:
    
         triangulo()
    elif opcion == 3:
         circulo()

    elif opcion == 4:
        return (opcion)
    

while True:
    
    if menuInicialDef() == 4:
        break
    menuInicialDef()
print("fin del programa")    




