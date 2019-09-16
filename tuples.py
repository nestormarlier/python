mitupla=("DNI",28891325,1532591550,"Nestor","Marlier")

print(mitupla[3])

milista=list(mitupla)

print(milista)
print(mitupla)
print(mitupla[1])
print(milista[1])

mituple=tuple(milista)
print(mituple)

print("Nestor" in mituple)

print(mituple.count("Marlier"))

print(len(mituple))

mituple2=12,"Mia", 30,"sep",2009
print(mituple2)

mituple3=("Nestor",1,8,1981)
nombre,dia,mes,anio=mituple3
print(dia)
print(mes)
print(anio)
print(nombre)