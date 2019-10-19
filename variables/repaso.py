print("Repasaremos todo lo aprendido")

print("STRING")
print('STRING')
print('''STRING''')
print(type("STRING"))
print(".....................................................")
print("INTEGER")
print(33323)
print(type(33323))
print(".....................................................")
print("FLOAT")
print(43.6)
print(type(43.6))
print(".....................................................")
print("LIST")
print([10,20,45,66,89,92])
print(type([0]))
print(".....................................................")
print("TUPLES")
print(("Nestor","Marlier","28.891.325"))
print(type((1,4,5)))
print(".....................................................")
print("DICTIONARIES")
print({
    "nombre":"Nestor",
    "apellido":"Marlier",
    "dni": 28891325,
})
print(type(({})))

def mensaje():
    print("esta es una funcion")

mensaje()
mensaje()
mensaje()

def suma(v1,v2):
    print(v1+v2)

v1=input("Ingrese primer valor: ")
v2=input("Ingrese segundo valor: ")

suma(int(v1),int(v2))

mi_lista=["Nestor", "Estefy", "Mia", "Julia"]

print (mi_lista[32])



