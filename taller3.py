#aloritmo que permite ingresar una determinada de numeros mientras el usuario desee seguir ingresando numeros, y saca el promedio de los mismos
suma=0
cont=0
resp="aun no responde"
while resp!="S":
    num=int(input("Ingrese un numero: "))
    suma+=num
    cont+=1
    resp=str(input("¿Desea terminar? (S/N): "))
prom=suma/cont
print(f"el promedio es {prom}")