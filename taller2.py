N=int(input("Ingrese el valor de N: "))
serie=0
for i in range(1,N+1):
    if i%2==0:
        serie-=1/i
    else:
        serie+=1/i
print(f"el resultado de la serie es: {serie}")