hora=int(input("Digite a hora: "))
#se
if hora>=6 and hora<12:
    print("Manhã")
#senao se
elif hora>=12 and hora<18:
    print("Tarde")
#senao
else:
    print("Noite")
