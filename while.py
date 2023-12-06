b = input("Digite uma cadeira binária (0s e 1s):")
i = len(b)
x = 0
while i>0:
 x = x + int(b[i-len(b)])*2**(i-1)
 i = i - 1
print(x)