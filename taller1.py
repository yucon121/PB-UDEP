n=int(input("Ingresa el numero 1: "))
m=int(input("Ingresa el numero 2: "))
suma_imp=0
if n != m:
    if n>m:
        for i in range(m,n):
            if i%2 !=0:
                suma_imp+=i
    else:
        for i in range(n,m):
            if i%2 !=0:
                suma_imp+=i
    print(f"El resultado es: {suma_imp}")
else:
    print("ha ingresado numeros iguales")