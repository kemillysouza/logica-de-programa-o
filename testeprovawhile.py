result = ""
q = int(input("Digite um número inteiro positivo: "))
while q!= 0:
 result = str(q%2) + result
 q = q // 2
print(result)