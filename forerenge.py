'''k=10
j=0
for i in range(1,6):
    k=k+i
    if i/2>=2:
        j=j+3
    if i*3<7:
        j=j+5
    else:
        j=j+1
print(j+k)'''

f0=0
f1=1
for i in range(1,6):
    t=f1
    f1=f1+f0
    f0=t 
print(f1)
