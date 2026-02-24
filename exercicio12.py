estoque=int(input("Digite o estoque atual: "))
#se
if estoque<=50:
    print("Estoque baixo!")
    print("Sugestão: fazer pedido de reposição")
#senao
else:
    print("Estoque ok")
