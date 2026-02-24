peso=float(input("Digite o peso do produto (0.95): "))
tem_defeito=input("O produto tem defeito? (s/n): ")
#se
if peso>=0.95 and peso<=1.05:
    #se
    if tem_defeito=="n":
        print("Premium: peso ideal e sem defeitos")
    #senao
    else:
        print("Standard: pequenas variações")
#senao
else:
    print("Rejeitado: fora dos padrões")
