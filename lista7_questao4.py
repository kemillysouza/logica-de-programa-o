x=int(input("digite o comprimento do lado 1:"))
y=int(input("digite o comprimento do lado 2:"))
z=int(input("digite o comprimento do lado 3:"))
if (x>y+z):
    if((x==y) and (x!=z)) or ((x==z)and (x!=y)):
        resultado="triângulo isósceles"
        print("esse triangulo é",resultado)
    elif (x==y==z):
            resultado="triângulo equilatero"
            print("esse triangulo é",resultado)
    elif (x!=y) and (x!=z): 
        resultado="triângulo escaleno"
        print("esse triangulo é",resultado)
else:
    print("isso nao é um triângulo")              