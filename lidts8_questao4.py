from codecs import BufferedIncrementalEncoder


coluna=int(input("digite o valor da coluna"))
linha=int(input("digite  o valor da linha"))
if coluna%2==0:
    x= "Branco"
else:
    x="preto"
if linha%2==0:
    y="branco" 
else:
    y="preto" 

print(x,y)   