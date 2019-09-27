class Coche():
    def __init__(self):
        self.__largoChasis=250
        self.__anchoChasis=120
        self.__ruedas=4
        self.__enMarcha=False 
    
    def arrancar(self,arranquemos):
        self.__enMarcha=arranquemos
        
        if self.__enMarcha:
            chequeo=self.chequeoInterno()
            print(chequeo)
        
        if self.__enMarcha and chequeo:
            return "El coche se encuentra en marcha"
        elif self.__enMarcha==True and chequeo==False:
            return "El coche ha tenido algun problema, y no ha podido arrancar."            
        else:
            return "El coche se encuentra parado"          
        
    def estado(self):
        print("El coche tiene",self.__ruedas, "ruedas. Y un largo de",self.__largoChasis, 
              "Un ancho de", self.__anchoChasis,".")
    
    def chequeoInterno(self):
        print("Realizando el chequeo del Interno")
        
        self.gasolina="ok"
        self.aceite="Nook"
        self.puertas="cerradas"
        
        if(self.gasolina=="ok" and self.aceite=="ok" and self.puertas=="cerradas"):
            return True 
        else:
            return False
        
        
miCoche=Coche()

print(miCoche.arrancar(True))
miCoche.estado()

print("------------- A continuacion genero mi proximo objeto -------------")

miCoche2=Coche()
print(miCoche2.arrancar(False))

miCoche2.ruedas=2 #No modifica la propiedad de la clase por estar encapsulado
miCoche2.estado()

