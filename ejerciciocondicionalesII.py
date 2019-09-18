print("Sistema de becas")

print("-------------<>--------------")

distancia=int(input("Ingrese los Km de distancia que tiene hasta nuestro centro de estudio (Km): "))
nroHnos=int(input("Ingrese la cantidad de hermanos que posee: "))
salarioFamiliar=int(input("Ingrese el salario familiar por mes que posee: "))

if distancia>40 and nroHnos>2 and salarioFamiliar<20000:
    print("Usted tiene derecho a beca solicitada")
elif distancia<40:
    print("Usted vive a menos de 40 km")
elif nroHnos<3:
    print("Usted no posee mas de dos hermanos")
elif salarioFamiliar>20000:
    print("Su salario es mayor a $20.000.-")