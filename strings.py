'''#1
f=(input("digite uma frase ou palavra:"))
g=(input("qual letra você quer ver se aparece ou não:"))
if f.count(g)>0:
    print("aparece")
else:
 print("nao aparece")

#2
p=(input("digite uma palavra ou uma frase:"))
g=(input("qual letra deseja ver se aparece:"))
h=p.count(g)
print("a letra ",g," aparece",h,  "vezes na frase/palavra:")

#3
nome=(input("digite seu nome:"))
for i in nome:
    print(i)
    
#4
nome="kemilly"
quantidade=len(nome)
p=0
i=0
while p<quantidade+1:
    print(nome[0:i])
    i=i+1
    p=p+1

#5
nome="kemilly"
quantidade=len(nome)
p=0
i=0
while p<quantidade+1:
    print(nome[0:i])
    i=i-1
    p=i+1   
#6
n=(input("digite uma frase/palavra:"))
p=(input("digite a letra que quer retirar:"))
h=n.replace(p)
print(h)
#7
p=(input("digite palavra:"))
s2=""
for letra in p:
    if letra =="a" or letra=="e" or letra=="i" or letra=="o" or letra=="u":
        s2=s2+letra+letra
    else:
        s2=s2+letra
print(s2)
8#
s1=(input("digite uma frase/palavra:"))
s2=(input("digite uma palavra/frase:"))
t1=len(s1)
t2=len(s2)
print("o tamanho da primeira frase/palavra é de",t1,"caracteres")
print("o tamanho da primeira frase/palavra é de",t2,"caracteres")
if t1!=t2:
    print("o tamanho/conteudo das duas strings são diferentes")
else:
    print("o tamanho/conteudo das duas strings sao os mesmos/iguais")

#9
n=(input("digite uma frase/palavra:"))
p=n.count(" ")
a=n.count("a")
e=n.count("e")
i=n.count("i")
o=n.count("o")
u=n.count("u")
print("a frase possui",p,"espaços em branco",a,"a",e,"e",i,"i",o,"o",u,"u")'''
#10
janeiro = "01"
fevereiro = "02"
março = "03"
abril = "04" 
maio = "05"
junho = "06"
julho = "07"
agosto = "08"
setembro = "09"
outubro = "10"
novembro = "11"
dezenbro = "12"

data = input("Digite a sua data de nascimento (Ex:07/01/2013):")
dia = data[0:2]
mes = data[3:5]
ano = data[6:10]
if mes == janeiro:
    print("Você nasceu em", dia, "de janeiro de", ano)
elif mes == fevereiro:
    print("Você nasceu em", dia, "de fevereiro de", ano)
elif mes == março:
    print("Você nasceu em", dia, "de março de", ano)
elif mes == abril:
    print("Você nasceu em", dia, "de abril de", ano)
elif mes == maio:
    print("Você nasceu em", dia, "de maio de", ano)
elif mes == junho:
    print("Você nasceu em", dia, "de junho de", ano)
elif mes == julho:
    print("Você nasceu em", dia, "de julho de", ano)
elif mes == agosto:
    print("Você nasceu em", dia, "de agosto de", ano)
elif mes == setembro:
    print("Você nasceu em", dia, "de setembro de", ano)
elif mes == outubro:
    print("Você nasceu em", dia, "de outubro de", ano)
elif mes == novembro:
    print("Você nasceu em", dia, "de novembro de", ano)
else:
    print("Você nasceu em", dia, "de dezembro de", ano)
#11

cpf = input("Digite o seu CPF para ser verificado:")
quat = len(cpf)-2
num = 0
num1 = 0
num2 = 1
multi = 10
soma = 0
while num<quat:
    cpf1 = cpf[num1:num2]
    soma += int(cpf1) * multi
    num1 += 1
    num2 += 1
    multi -= 1
    num += 1
resto = soma % 11
result1 = 11 - resto
if result1 == int(cpf[9:10]):
    dig1 = True
elif resto >= 10:
    if int(cpf[9:10]) == 0:
        dig1 = True
else:
    dig1 = False

if dig1==True:
    print("O CPF é válido")

else:
    print("O CPF é falso")

