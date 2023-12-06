'''#1
n=(input(str("digite um numero:")))
p=n.count(str(3))
h=n.count(str(4))
print(p,h)'''
#2 pedir para o prof
#3
#4
s1 =  (input("Digite uma palavra:"))
s2 =  (input("Digite outra palavra:"))
s3 =""
i = 0 
i2 = 1
cont = 0
quat = len(s1) + len(s2) + 1
while cont < quat:
    s3 = s3 + s1[i:i2] + s2[i:i2]
    i += 1 
    i2 += 1
    cont +=1
print(s3)

5#

numero =  input("Digite um número:")
s1 = ""
for num in numero:
    numint = int(num)
    num1 = numint + 1
    num2 = str(num1)
    if num1 >= 10:
        s1 = s1 + num2[1:3]
    else:
        s1 = s1 + num2
print(s1)

#6
palavra = input("Digite uma palavra:")
s1 = ""
for num in palavra:
    if num == "0" or num == "1" or num =="2" or num =="3" or num =="4" or num =="5" or num =="6" or num =="7" or num =="8" or num =="9":
        s1 = s1 + num + num
    else:
        s1 = s1 + num
 
print(s1)

 #7
s1 = ""
s2 = ""
palavra1 =  input("Digite um palavra:")
palavra2 =  input("Digite outro palavra:")
quat = len(palavra2)
position = 0
i = quat + 1
l = quat
while position < quat+1:
   letra = palavra2[l:i]
   l -= 1
   i -= 1
   position+=1
   s1 = s1 + letra
 
if s1 == palavra1:
    v1=True
else:
    v1=False

quat = len(palavra1)
position = 0
i = quat + 1
l = quat
while position < quat+1:
   letra = palavra1[l:i]
   l -= 1
   i -= 1
   position+=1
   s2 = s2 + letra  

if s2 == palavra2:
    v2=True
else:
    v2=False

if v1 and v2:
    print(s1, "é o reverso de", s2)
else:
    print(s1, "não é o reverso de", s2)


