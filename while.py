import math

print("Calculo raiz cuadrada")
num=int(input("Ingresar el numero que desa averiguar las raiz cuadrada "))

intentos=0

while num<0:
    print("No se puede obtener la raiz cuadrad de un numero negativo")
    
    if intentos>2:
        print("Demasiados intentos")
        break;
    intentos=intentos + 1
    num=int(input("ingrese numero nuevamente: "))

if intentos<2:
    print(f"La raiz cuadrada de {num} es " + str(math.4sqrt(num)))