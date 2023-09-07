
def menu():
  lista = """
  ··············
  1.suma
  2.resta
  3. multiplicacion
  4. division
  5.salir
  ················
  """
  print(lista)
  opcion = int(input("ingrese el tipo de opercion: "))
  return opcion


def suma(a,b):
  return a + b

def resta(a,b):
  return a - b

def divison(a,b):
   return a / b


def multiplicacion(a,b):
  return a * b
  

while True:
   
    opcion = menu()
    if opcion == 5:
      break
    else:
      num1 = int(input("ingrese el valor de su primer numero: "))
      num2 = int(input("Ingese el valor de su segundo numero: "))
      if opcion == 1:
        print(suma(num1,num2))
        
      elif opcion == 2:
        print(resta(num1,num2))
      elif opcion == 3:
        print(multiplicacion(num1,num2))
      elif opcion == 4:
        print(divison(num1,num2))
      


 