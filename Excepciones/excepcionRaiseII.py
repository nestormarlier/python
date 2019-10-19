import math

def calculaRaiz(valor):
    
    if valor<0:
        raise ValueError("No puede ingresarse un número negativo")
    else:
        return math.sqrt(valor)

num=int(input("Ingrese el número que desea averiguar la Raiz cuadrada: "))

try:
    print(calculaRaiz(num))
except ValueError as ErrorDeNumeroNegativo:
    print(ErrorDeNumeroNegativo)

print("Programa terminado")

