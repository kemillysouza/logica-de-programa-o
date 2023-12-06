a=int(input("digite um valor:"))
b=int(input("digite outro valor:"))
c=int(input("digite mais um outro valor:"))
# o menor numero 
menor = a 
if b<a and b<c: 
    menor = b 
if c<a and c<b:
    menor = c 
print("o menor numero digitado foi:",menor) 
# o numero maior 
maior = a
if b>a and b>c:
    maior=b
if c>a and c>b:
    maior=c
print ("o maior numero digitado foi:",maior)    

   
 