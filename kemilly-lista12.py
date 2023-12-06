#1
fator=1
n=int (input("digite o numero que voce deseja fatorar:"))
for i in range(1,n+1):
    fator= fator*i
print(fator)
#2
a=1
b=1
graos = int (input("digite o numero de quadrados utilizados:"))
for i in range (1,graos):
    a=(2*a)
    for i in range(1):
      b=(a+b)
print(a)
print(b)
#3
produto=0
numero=int(input("digite o numero a ser multiplicado:"))
numero2=int(input("digite a quantidade de vezes a ser multiplicado:"))
for i in range(1,numero2+1):
    produto= produto+numero 
print(produto)
#4
qunt= int(input("digite o numero de termos:"))
print("0",end=" , ")
ant1=0
ant2 =1
for i in range(3, qunt+1):
    atual=ant1+ant2
    print(atual,end=(","))
    ant1=ant2
    ant2=ant1
    