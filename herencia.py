class vehiculo():
    
    def __init__(self,marca,modelo):
        self.marca=marca
        self.modelo=modelo
        self.enmarcha=False
        self.acelera=False
        self.frena=False
        
    def arrancar(self):
        
        self.enmarcha=True
        
    def acelerar(self):
        
        self.acelera=True
        
    def frenar(self):
        
        self.frenar=True
        
    def estado(self):
        print("Marca:", self.marca,"\n" "Modelo:",self.modelo)
        
class Moto(vehiculo):
    pass

miMoto=Moto("Honda","CBR")

miMoto.estado()
    
        