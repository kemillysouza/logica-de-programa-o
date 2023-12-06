#1
lista1 = []
def min_max(t):
    listacerta = []
    t.sort()
    listacerta.append(t[9])
    listacerta.append(t[0])
    return listacerta

for b in range(10):
    num = int(input("Digite um número:"))
    lista1.append(num)

valor= min_max(lista1)
print("Valor maior e menor:", valor)
#2
lista1 = []
def inverte(t):
    t.reverse()
    return t

for a in range(3):
    palavras = input('Digite um número:')
    lista1.append(palavras)

valor_final = inverte(lista1)
print(valor_final)
#3
lista1 = []
def inverte_duplo(x):
    str = ''
    listain =[]
    for a in range(0,5):  
        for b in (x[a]):
            str =  b + str 
        listain.append(str)
        str = ''
    listain.reverse()
    return listain

for a in range(5):
    palavras = input('Digite uma palavra:')
    lista1.append(palavras)

valor_final = inverte_duplo(lista1)
print(valor_final)
#4

lista1 = []
def intersecção(c1, c2):
    listacerta = []
    for a in range(0,5):
        lista_temporaria = [c1[a], c2[a]]
        listacerta.append(lista_temporaria)
    return listacerta

x1 = [1, 2, 3, 4, 5]
x2 = [5, 4, 3, 2, 1]

valor_final = intersecção(x1, x2)
print(valor_final)
#5 nao consegui fazer
#6
lista1 = []
def intersecção(c):
    vogais = ""
    demais = ""
    lista = []
    for a in c:
        if a == "a" and "e" and "i" and "o" and "u":
            vogais += a
        else:
            demais += a
      
    lista.append(vogais)
    lista.append(demais)

    return lista

x = input("Digite uma palavra:")

valor_final = intersecção(x)
print(valor_final)
#7
def  pares_impares(x):
    pares = []
    impares = []
    lista = []
    for a in range(0,5):
        if 0 == (x[a])%2:
           pares.append(x[a])
        else:
            impares.append(x[a])
      
    lista.append(pares)
    lista.append(impares)
    tupla = tuple(lista)

    return tupla

y = (1,2,3,4,5)

valor_final =  pares_impares
print(valor_final)
