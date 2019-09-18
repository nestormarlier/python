for i in ["a",2,"m"]:
    print("Hola")
    
for i in ["Verano","Otoño","Invierno","Primavera"]:
    print(i)
    
for estaciones in ["Verano","Otoño","Invierno","Primavera"]:
    print("Las estaciones del año son: " + estaciones)

for i in ["Pildoras", "Informaticas", 3]:
    print("Hola",end=" ")

for i in "juan@pildorasinformaticas.es":
    print("Hola", end=" ")
    
email=input("Ingrese su mail: ")
mail=False 
arroba=False

for i in email:
    if "@" == i:
        arroba=True
    else:
        if "." == i:
            mail=True
            
                  
if mail and arroba:
    print("Es un mail correcto")
else:
    print("Es un mail incorrecto")


