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

for i in range(4):
    print("hola")
    
for i in range(4):
    print(f"El valor de i es {i}")
    
for i in range(5,9):
    print(f"El valo de i es {i}")
    
for i in range(5,50,3):
    print(f"Valor {i}")
    
validomail=False

mail=input("Ingrese e-mail")

for i in range(len(mail)):
    if mail[i] == "@":
        validomail=True

if validomail:
    print(f"El mail {mail} es correcto")
else:
    print(f"El mail ingresado {mail} es incorrecto")
        