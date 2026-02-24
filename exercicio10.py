valor=int(input("Digite o valor do sensor: "))
#se
if valor<1:
    print("Sensor com problema")
#senao se
elif valor>100:
    print("Sensor com problema")
#senao
else:
    print("Sensor OK")
