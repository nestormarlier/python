class Coche():
    largoChasis=255
    anchoChasis=120
    ruedas=4
    enmarcha=False
    
    def arrancar(self):
        self.enmarcha=True
    
    def estado(self):
       if(self.enmarcha):
            return"El coche está en marcha"   
       else:
            return"El coche está parado"
        
miCoche=Coche()
miCoche2=Coche()
        
print("El largo del coche es:",miCoche.largoChasis)
print("El coche tiene ",miCoche.ruedas ,"ruedas")

miCoche.arrancar()
print(miCoche.estado())
print("------------- Este es el otro coche ------------------------------")
print("El ancho del auto es:",miCoche2.anchoChasis)
print(miCoche2.estado())
