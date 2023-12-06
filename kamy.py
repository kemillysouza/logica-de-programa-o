''' #1
lista1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
print(lista1)
listapar = []
listaimpar = []
for caracter in lista1:
    if caracter%2==0:
        listapar.append(caracter)
    else:
        listaimpar.append(caracter)

print(listapar)
print(listaimpar)'''
#2
'''x=0 
f=[ ]
for e in range(2):
    a=(int(input("digite a primeira nota:")))
    b=(int(input("digite a segunda nota:")))
    c=(int(input("digite a terceira nota:")))
    d=(int(input("digite a quarta nota:")))
    print("--------------")
    media=((a+b+c+d)/4)
    f.append(media)
    if media>=7:
        x=x+1
print(x)
#3
lista1=[ ]
lista2=[ ]
for i in range(5):
    a=(float(input("digite sua altura:")))
    b=(int(input("digite sua idade:")))
    lista1.append(a)
    lista2.append(b)
print(lista1[0], lista2[0])
print(lista1[1], lista2[1])
print(lista1[2], lista2[2])
print(lista1[3], lista2[3])
print(lista1[4], lista2[4])
#4
lista1=["a","b","c","d","e","f","g","h","i","j"]
lista2=[1,2,3,4,5,6,7,8,9,10]
lista3=[ ]
for i in range(0,10):
    lista3.append(lista1[i])
    lista3.append(lista2[i])
print(lista3)
#5
lista1=["a","b","c","d","e","f","g","h","i","j"]
lista2=[1,2,3,4,5,6,7,8,9,10]
lista3=["oi","oi","oi","oi","oi","oi","oi","oi","oi","oi",]
lista4=[ ]
for i in range(0,10):
    lista4.append(lista1[i])
    lista4.append(lista2[i])
    lista4.append(lista3[i])

print(lista4)'''
(perguntar questão 6 para o prf)