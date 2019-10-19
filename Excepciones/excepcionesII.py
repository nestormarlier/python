def divide():
    
    try:
        op1=float(input("introduce el primer numero: "))
        op2=float(input("introduce el segundo numero: "))
    
        print("La division es " + str(op1/op2))
    except ValueError:
        
        print("El valor introducido es erróneo")
    
    except ZeroDivisionError:
        
        print("El valor no es divisile por cero")
        
    finally:
        print("Cálculo completado")
    
divide()