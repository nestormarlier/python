myStr = "Hello World"

#print(dir(myStr))

# print(myStr.upper())
# print(myStr.lower())
# print(myStr.swapcase())
# print(myStr.capitalize())
# print (myStr.replace("Hello", "bye"))
# print (myStr.replace("Hello", "bye").upper())

# print(myStr.count('hello'))

# print(myStr.startswith('Hello'))
# print(myStr.endswith('World'))

# print(myStr.split('o')) #crea lista
# print(myStr.find('o')) #posicion donde aparece la primer "o"

# print(len(myStr))
# print(myStr.index('e'))#posicion de la letra "e" igual a 1 (0,1,2,3,etc)

# print(myStr.isnumeric())
# print(myStr.isalpha())

print(myStr[0])#muestra la letra de la posicion soilicitada
print(myStr[-1])#muestra la letra de la derecha a la izquierda cuando es negativo

print("Mi nombre es " + myStr)
print(f"Mi nombre es {myStr}") #a partir de Python 3.6 debo colo la "f" para que tome la variable"
print("Mi nombre es {0}".format(myStr))