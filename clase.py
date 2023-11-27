class Coche: 
    ruedas = 4 

    def __init__(self, aceleracion, color, marca):
        self.color = color 
        self.aceleracion = aceleracion
        self.velocidad = 0 

    def acelerar (self):
     self.velocidad + self.aceleracion

    def frenar(self):
        v = self.velocidad - self.aceleracion
        if v<0:
            v = 0 
            self.velocidad = v     
obj1 = Coche(5,"rojo", "marca", )
print("color del coche:", obj1.color)
print("acelarion del coche:", obj1.aceleracion)
print("velocidad del coche:", obj1.velocidad)

obj2 = Coche(5,"rojo", "marca", )
print("color del coche:", obj2.color)
print("acelarion del coche:", obj2.aceleracion)
print("velocidad del coche:", obj2.velocidad)

ac = obj1.aceleracion - obj2.aceleracion

print(ac)
