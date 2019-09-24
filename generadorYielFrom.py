def devuelveCiudades(*ciudades):
    for elemento in ciudades:
        yield elemento
        
generatorCiudades=devuelveCiudades("Buenos Aires","La Pampa", "Entre Rios", "San Luis", "Corrientes", "Misiones")

print(next(generatorCiudades))

print("+ Código")

print(next(generatorCiudades))

print("+ Código")

print(next(generatorCiudades))

def devuelveNombres(*nombres):
    for elemento in nombres:
        for subelemento in elemento:
            yield subelemento

generatorNombres=devuelveNombres("Nestor", "Estefy", "Mia","Julia")

for i in generatorNombres:
    print(i)
    
#YIELD FROM LO PODEMOS USAR PARA EVITAR ESCRIBIR EL FOR ANIDADO

def devuelveAnimales(*animales):
    for elemento in animales:
        yield from elemento #me evito programar el subelemento como el codigo anterior
        
generatorAnimales=devuelveAnimales("Perro", "Gato","Raton","Pajaro")

# for i in generatorAnimales:
#     print(i)

print(next(generatorAnimales))
print("......")
print(next(generatorAnimales))
print("......")
print(next(generatorAnimales))

def devuelvePaises(*paises):
    for elemento in paises:
        yield from elemento

generatorPaises=devuelvePaises("Argentina","Bolivia","Chile","Paraguay","Uruguay","Brasil","Venezuela","Colombia","Perú")

print(next(generatorPaises))
print(next(generatorPaises))
print(next(generatorPaises))
print(next(generatorPaises))
print(next(generatorPaises))
print(next(generatorPaises))
print(next(generatorPaises))
