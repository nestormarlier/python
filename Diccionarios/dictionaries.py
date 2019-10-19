midiccionario={"Francia":"Paris","Reino Unido":"Londres","España":"Valencia","España":"Madrid","Argentina":"Buenos Aires"}

print(midiccionario["Argentina"])
midiccionario["Italia"]="Lisboa"
print(midiccionario)
midiccionario["Italia"]="Roma"
print(midiccionario)
del midiccionario["Reino Unido"]
print(midiccionario)

midiccionario2={"Nestor":"Marlier",23:"Jordan","Mosqueteros":3}
print(midiccionario2)

mitupla=("Argentina", "Chile", "Paraguay", "Uruguay","Bolivia", "Brasil")

midiccionarioPaises={mitupla[0]:"Buenos Aires",mitupla[1]:"Santiago"
                     ,mitupla[2]:"Asuncion",mitupla[3]:"Montevideo"
                     ,mitupla[4]:"Sucre",mitupla[5]:"Brasilia"}

print(midiccionarioPaises)
print(midiccionarioPaises[mitupla[2]])
print(midiccionarioPaises["Paraguay"])

midiccionario3={23:"Jordan","Nombre":"Michael","Equipo":"Chicago","Anillos":[1991,1992,1193,1996,1997,1998]}

print(midiccionario3)
print(midiccionario3["Anillos"])

midiccionarioDoble={23:"Jordan","Nombre":"Michael","Equipo":"Chicago","Anillos":{"Temporadas":[1991,1992,1193,1996,1997,1998]}}
print(midiccionarioDoble["Anillos"])

print(midiccionarioDoble.keys())
print(midiccionarioDoble.values())
print(len(midiccionarioDoble))