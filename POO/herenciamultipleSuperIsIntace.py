class Persona():
    def __init__(self,nombre,edad,lugarResidencia):
        self.nombre=nombre
        self.edad=edad
        self.lugarResidencia=lugarResidencia
        
    def descripcion(self):
        print("Nombre:", self.nombre, "\nEdad:", self.edad,"\nLugar de residencia:", self.lugarResidencia)

class Empleado(Persona):
    def __init__(self,salario,antiguedad, nombre,edad,lugarResidencia):
        
        super().__init__(nombre,edad,lugarResidencia)
        
        self.salario=salario
        self.antiguedad=antiguedad
        
    def descripcion(self):
        super().descripcion()
        
        print("Salario:", self.salario, "\nAntigüedad:", self.antiguedad)
        
julia=Empleado(1500,10,"Julia",5,"Longchamps")

julia.descripcion()


        
        
        