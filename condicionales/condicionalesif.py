def examen(valor):
    if valor>=4:
        return True
    else:
        return False

nota=input("Introduce nota: ")

if examen(int(nota)):
    print("Aprobado")
else:
    print("Desaprobado")