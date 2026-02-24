boas=0
defeitos_seguidos=0
#enquanto
while defeitos_seguidos<5:
    peca=input("Digite 'b' para boa ou 'd' para defeituosa: ")
    #se
    if peca=="b":
        boas= boas + 1
        defeitos_seguidos=0
    #senao se
    elif peca=="d":
      defeitos_seguidos= defeitos_seguidos + 1
    #senao  
    else:
        print("digite apenas 'b' ou 'd'")

print("Total de peças boas no lote:",boas)
