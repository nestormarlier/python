for letra in "Python":
    
    if letra == "h":
        continue #continua con el bucle salteando la letra "h" del ciclo for
    print ("Viendo la letra " + letra)


nombre = "Pildoras informaticas"
contador = 0
for letra in nombre:
    if letra == " ":
        continue
    contador+=1
    
    
print("La cantidad de letras son: " + str(contador))