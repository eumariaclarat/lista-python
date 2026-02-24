meta=1000
quantidade=int(input("Digite a quantidade produzida hoje: "))
#se
if quantidade>=meta:
    print("Meta atingida!")
#senao
else:
    falta= meta-quantidade
    print("Meta não atingida.")
    print("Faltam",falta,"unidades.")
