print("Programa para generar números pares")

def numerosPares(cantpares):
    listaNum=[2]
    for i in range(cantpares-1):
        listaNum.append(listaNum[i]+2)
       
    return print(listaNum)

numerosPares(int(input("Qué cantidad de números pares desea generar?")))

def numerosPares2(limite):
    num=1
    listaPares=[]
    
    while limite>num:
        
        listaPares.append(num*2)
        
        num=num+1
    return listaPares


print(numerosPares2(10))