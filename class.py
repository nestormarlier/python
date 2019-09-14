class coche():
    largo=240
    ancho=222
    ruedas=4
    enmarcha=False

def arrancar(self):
    self.enmarcha=True

def estado(self):
    if self.enmarcha==True:
        return "El coche esta en marcha"
    else:
        return "El coche esta parado"

micoche=coche()


