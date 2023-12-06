#1
a=0
b=0
c=0
d=0
e=0
f=0
soma = 0
valores = [a, b, c, d, e, f]
valoresfinais=[]
while True:
    resposta = int(input("Qual o melhor sistema operacional, 1- Windows Server, 2- Unix, 3- Linux, 4- Netware, 5- Mac OS, 6- Outro e 0- Para encerrar a votação:"))
    if resposta == 0:
        break
    else:
        if resposta == 1:
            valores[0] += 1
            soma += 1

        elif resposta == 2:
            valores[1] += 1
            soma += 1
    
        elif resposta == 3:
            valores[2] +=1
            soma += 1

        elif resposta == 4:
            valores[3] += 1
            soma += 1

        elif resposta == 5:
            valores[4] += 1
            soma += 1

        elif resposta == 6:
            valores[5] += 1
            soma += 1
        
        else:
            print("Esse número não é valído")

f1 = valores[5]/soma
valoresfinais.append(f1)
e1 = valores[4]/soma
valoresfinais.append(e1)
d1 = valores[3]/soma
valoresfinais.append(d1)
c1 = valores[2]/soma
valoresfinais.append(c1)
b1 = valores[1]/soma 
valoresfinais.append(b1)           
a1 = valores[0]/soma
valoresfinais.append(a1)
valoresfinais.sort()

print("Sistema Operacional     Votos     %")
print("-------------------     -----    ---")
print("Windows Server             ",        valores[0], "  ", "{:.0%}".format(a1))
print("Unix                       ",        valores[1],  "   ","{:.0%}".format(b1))
print("Linux                      ",        valores[2], "   ","{:.0%}".format(c1))
print("Netware                    ",        valores[3], "   ","{:.0%}".format(d1))
print("Mac OS                     ",        valores[4], "   ","{:.0%}".format(e1))
print("Outro                      ",        valores[5], "   ","{:.0%}".format(f1))

if valoresfinais[5]==a1:
    vencedor ="Windowa Server"
elif valoresfinais[5]==b1:
    vencedor = "Unix"
elif valoresfinais[5]==c1:
    vencedor = "linux"
elif valoresfinais[5]==d1:
    vencedor = "Netware"
elif valoresfinais[5]==e1:
    vencedor = "Mac OS"
elif valoresfinais[5]==f1:
    vencedor = "Outro"

valores.sort()
quat = valores[5]
print ("O Sistema Operacional mais votado foi o", vencedor,"com", quat,"votos, correspondendo a", "{:.0%}".format(valoresfinais[5]))
#2
from random import randint
l1 = []
for i in range(100):
    x = randint(1,6)
    l1.append(x)
    print(x)
    y =l1.count(1)
    z =l1.count(2)
    a =l1.count(3)
    b =l1.count(4)
    c =l1.count(5)
    d =l1.count(6)
print(
"Esses são os 100 lançamentos do dado,"
,l1,".")
print("Quantidade de números 1={}, n° 2={}, n° 3={}, n° 4={}, n° 5={} e n° 6={}".format(y, z, a, b, c, d))
#3

modelos = []
consumo = []
litro = []
quatlitros = []
for a in range(0,5):
    carro = input("Digite um modelo de carro:")
    modelos.append(carro)
    gasolina = float (input("Digite o consumo de gasolina desse modelo:"))
    litro.append(gasolina)
    gasto = (5.25/gasolina) * 1000
    consumo.append(gasto)
    consumo2 = consumo
    quatlitro = (1000 * 5.25) / gasto
    quatlitros.append(quatlitro)
for b in range(0,5):
    print("Veiículo", (b+1))
    print("Nome:", modelos[b])
    print("Km por litro:", litro[b])

print("Relatório final")

print("1 -", modelos[0], "-", litro[0], "-", quatlitros[0], "litros - R$", '{:.02f}'.format(consumo[0]))
print("2 -", modelos[1], "-", litro[1], "-", quatlitros[1], "litros - R$", '{:.02f}'.format(consumo[1]))
print("3 -", modelos[2], "-", litro[2], "-", quatlitros[2], "litros - R$", '{:.02f}'.format(consumo[2]))
print("4 -", modelos[3], "-", litro[3], "-", quatlitros[3], "litros - R$", '{:.02f}'.format(consumo[3]))
print("5 -", modelos[4], "-", litro[4], "-", quatlitros[4], "litros - R$", '{:.02f}'.format(consumo[4]))

