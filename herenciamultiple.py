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
        print("Marca: ", self.marca,"\n" "Modelo: ",self.modelo, "\n" "En marcha: ", self.enmarcha, "\n" 
              "Acelerando: ", self.acelera, "\n" "Frenando: ", self.frena)
        
class Moto(vehiculo):
    willy=""
    def hacerWilly(self):
        self.willy="Voy haciendo Willy"
    
    def estado(self):
        print("Marca: ", self.marca,"\n" "Modelo: ",self.modelo, "\n" "En marcha: ", self.enmarcha, "\n" 
          "Acelerando: ", self.acelera, "\n" "Frenando: ", self.frena, "\n" , self.willy)

miMoto=Moto("Honda","CBR")

#miMoto.hacerWilly()

miMoto.estado()
    
        