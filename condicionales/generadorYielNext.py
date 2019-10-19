def generaPares(limite):
    num=1
        
    while num<limite:
        yield num*2
        num=num+1

print(type(generaPares(10)))

generadorPares=generaPares(10)

# for i in generadorPares:
#     print(i)

print(next(generadorPares))

print("Aqui iría mas código")

print(next(generadorPares))

print("Aqui iría mas código")

print(next(generadorPares))

