peso=float(input("Digite o peso da peça: "))
#se
if peso<=0.5:
    print("Leve")
#senao se
elif peso<=2:
    print("Média")
#senao se
elif peso<=5:
    print("Pesada")
#senao
else:
    print("Muito pesada")
