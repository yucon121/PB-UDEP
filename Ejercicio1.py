#Codigo que pide un numero que sea mayor igual a 2 pero menor a 11, y saca el factorial del mismo
num=int(input("Ingresa el numero: "))
if 2<=num<11:
    cont=1
    for i in range(1,num+1):
        cont=cont*i
    print(f"El factorial de {num} es {cont}")
else:
    print(f"{num} no esta dentro del intervalo")
