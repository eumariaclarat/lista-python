total=0
maior=0
linha_maior=0
#for:para in range:intervalo
for i in range(1, 6):
    producao=int(input(f"Digite a produção da linha {i}: "))
    total= total + producao
    #se
    if producao>maior:
        maior=producao
        linha_maior=i
print("Produção total:",total)