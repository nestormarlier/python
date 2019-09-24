def suma(num1,num2):
    return num1+num2

def resta(num1,num2):
    return num1-num2

def multiplicar(num1,num2):
    return num1*num2

def divide(num1,num2):
    try:
        return num1/num2
    except ZeroDivisionError:
        print("No se puede dividir por cero")
        return "Operación errónea"

while True:
    try:
        op1=int(input("Introduce el primer número: "))
        op2=int(input("Introduzca el segundo numero: "))
        
        break 
    except ValueError:
        print("Los valores introducidos son incorrectos")
        
            
operacion=input("Ingrese la operacion a realizar SUMA - RESTA - MULTIPLICACION - DIVISION: ")
print(operacion)

if operacion == "suma":
    print(suma(op1,op2))
elif operacion == "resta":
    print(resta(op1,op2))
elif operacion=="multiplicacion":
    print(multiplicar(op1,op2))
elif operacion=="division":
    print(divide(op1,op2))
else:
    print("Operación no contemplada")

print("Operación ejecutada. Continuación de ejecución del programa")