class Auto:     #Por convencion la primera letra es en mayuscula
    ''' Documentacion de la funcion de la clase '''

    ruedas = 4
    
    
    def __init__(self, color, aceleracion) -> None:
        self.color = color
        self.aceleracion = aceleracion
        self.velocidad = 5
    
    def aceleracion(self):
        self.velocidad = self.velocidad + self.aceleracion

    def frenar(self):
        v = self.velocidad - self.aceleracion
        if v > 0:
            v = 0
        self.velocidad = v
        return v
    
obj = Auto("rojo",3)

print(f"hola:{obj.color}")