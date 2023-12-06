numeroa = int(input("Digite um número:"))
numerob = int(input("Digite um número:"))

if(numeroa>numerob):
    if(numeroa % numerob == 0):
        print(numeroa, "é multiplo de:", numerob) 
    
    else:
        print(numeroa, "não é o multiplo de:", numerob)
else:
    if(numerob % numeroa == 0):
        print(numerob, "é multiplo de:", numeroa)

    else:
        print(numerob,"não é multiplo de:", numeroa)