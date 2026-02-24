real=float(input("Produção real: "))
esperada=float(input("Produção esperada: "))

eficiencia= real/esperada * 100
print("Eficiência:",eficiencia,"%")
#se
if eficiencia>=90:
    print("Excelente")
#senao se 
elif eficiencia>=70:
    print("Boa")
#senao
else:
    print("Precisa melhorar")