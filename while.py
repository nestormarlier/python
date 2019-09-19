import math

numero=int(input("Ingrese el numero que desea averiguar su raiz cuadrada: "))

intentos=0

while numero<0:
    print("No existe la raiz cuadrada de un numero negativo")
    
    if intentos==2:
        print("Ha tenido demasiados intentos")
        break
    
    numero=int(input("Ingrese el numero que desea averiguar su raiz cuadrada: "))
    if numero<0:
        intentos=intentos+1

if intentos<2:
    solucion=math.sqrt(numero)
    print(f"El valor de la raiz cuadrada de {numero} es " + str(solucion))
    