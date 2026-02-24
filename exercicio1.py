temperatura=float (input("Digite a temperatura atual: "))
#se
if temperatura>80:
    print("ALERTA CRÍTICO! Temperatura acima de 80°C.")
#senao se 
elif temperatura>-60:
    print("Aviso: Temperatura elevada entre 60-80°C.")
#senao
else:
    print ("Temperatura normal abaixo de 60°C.")
