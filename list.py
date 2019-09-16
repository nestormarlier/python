nombres=["Nestor",38,"Estefy",32,"Julia",4,"Mia",10]

print(nombres)
print("---------------------------------------")
print(nombres[3]) # numero 32
print("---------------------------------------")
print(nombres[-8])
print("---------------------------------------")
milista=["Mia","Julia","Estefy","Nestor","Julia","Julia"]
print("---------------------------------------")
print (milista[0:3])#posicion 0 al 2
print (milista[:3])#del principio a la posicion 3-1=2
print (milista[1:2])#de la posicion 1 a la 1=2-1
print (milista[1:3])#de la posicion 1 a la 2=3-1

milista.append("Sandra")
print(milista[:])

milista.insert(2, "Juan Pablo") #inserta en la posicion [2] el valor
print(milista)
print(len(milista))
milista.extend(["Liliana","Mariano","Valen"])#debe ponerse entre corchetes
print(milista)

print(milista.index("Mariano"))
print("Julia"in milista)
milista.remove("Julia")
print(milista)
print(milista.pop())
print(milista)
milista2=[3,6,"Perro",False,5.99]

print(milista+milista2)
milista3=["Perro","Gato","raton",5,False]*3
print(milista3)

print(milista.count("Julia"))
print(milista3.count("Perro"))