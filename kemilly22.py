#1
import random

def sorteia_dado(num1):
    num= random.randint(0,6)
    return num
num = 0
numero = sorteia_dado(num)
print(numero)
#2

#3
def contagens(n):
    if n > 0:
        quant= len(str(n))
    return quant

a= int(input("Digte algo: "))
print(contagens(a))
#4
def eh_bissesto(ano):
    if ano%4==0:
        print("True")
    else:
        print("False")
    
y=float(input("Digite um ano: "))
eh_bissesto(y)
#5

def conta_digitos(n, d):
    if 0 < int(d) and int(d)<= 9:
        quant= n.count(d)
    return quant

a=input("Digite um número: ")
b=input("Digite um número: ")
conta_digitos(a, b)
print("possui", conta_digitos(a, b), "quantidades")
#6
#7
def encaixa(a, b):
    a1 = str(a)
    b1 = str(b)
    quant1 = len(b1)
    quant2 = len(a1)
    quant3 = quant2 - quant1
    v1 = a1[quant3:quant2+1]
    if v1 == b1:
        print("Sim, o digito ", b1, "está presente nos ultimos digitos de,", a1)
    else:
        print("Não, o digito ", b1, "não está presente nos ultimos digitos de,", a1)

    return

x = int(input("Digite um número:"))
y = int(input("Digite um número:"))
final = encaixa(x,y)
print(final)
