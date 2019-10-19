class Vehiculo():
    
    def __init__(self,marca,modelo):
        self.marca=marca
        self.modelo=modelo
        self.enmarcha=False
        self.frenando=False
        self.acelerando=False
        
    def estado(self):
        print("Marca:",self.marca,"\nModelo:",self.modelo,"\nEn marcha:",self.enmarcha,
              "\nFrenando:",self.frenando,"\nAcelerando:",self.acelerando)


class Moto(Vehiculo):
    
    def __init__(self,marca,modelo):
        
        super().__init__(marca,modelo)
        self.willy=""
    
    def estado(self):
        
        super().estado()
        print("\n",self.willy)
    
    def hacerWilly(self):
        self.willy="Haciendo Willy"
    
               
miCoche=Vehiculo("Ford","Fiesta")

miCoche.estado()

miMoto=Moto("Honda","CBR")
    
miMoto.hacerWilly()    

miMoto.estado()