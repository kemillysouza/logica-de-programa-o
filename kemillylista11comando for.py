#1
soma=0
n= int (input("escreva um numero inteiro positivo:"))
for i in range (n):
    n+1/(1+1)
    soma=soma+n
    print(soma)
#2
sub=0
n= int (input("escreva um numero inteiro positivo:"))
for i in range (1,n):
    sub=sub +((n-i)/(i+1))
print(sub)
#3
a=0
n=int(input("escreva um numero inteiro positivo:"))
if n>=0:
    for i in range (1,n+1,2):
        a=a+1/i
print(a)
#4
a=0
n=int(input("escreva um numero inteiro positivo:"))
for i in range (1,n+1):
    if (i%2==0):
        a=a - (1/i)
    else:
        a=a +(1/i)
print (a)
