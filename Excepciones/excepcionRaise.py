def evaluarEdad(edad):
    if edad<0:
        raise TypeError("La edad ingresada no puede ser negativa")
    if edad<20:
        return print("Eres muy Joven")
    elif edad<40:
        return print("Eres joven")
    elif edad<60:
        return print("Eres maduro")
    elif edad<100:
        return print("Eres mayor")

evaluarEdad(int(input("Ingresa una edad a evaluar: ")))