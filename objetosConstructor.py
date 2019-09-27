class Coche():
    largoChasis=250
    anchoChasis=120
    ruedas=4
    enMarcha=False 
    
    def arrancar(self):
        self.enMarcha=True
        
    def estado(self):
        if(self.enMarcha):
            return "El coche se encuentra en marcha"
        else:
            return "El coche esta parado"
        
miCoche=Coche()

print("El largo del coche es:", miCoche.largoChasis)
print(f"El coche tiene {miCoche.ruedas} ruedas")

miCoche.arrancar()

print(miCoche.estado())

print("------------- A continuacion genero mi proximo objeto -------------")

miCoche2=Coche()

print(miCoche2.largoChasis)
print(miCoche2.ruedas)
print(miCoche2.estado())