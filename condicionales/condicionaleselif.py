nota=int(input("Ingrese nota: "))

if nota<4:
    print("Insuficiente")
elif nota<6:
    print("Suficiente")
elif nota<8:
    print("Bien")
elif nota<9:
    print("Notable")
else:
    print("Sobresaliente")