import funciones1506 as fs #caso 1 15/06/2024
import random
cant=int(input("Ingrese la cantidad de numeros: "))
num_alt=[]
for i in range(cant):
    num=random.randint(2,100)
    num_alt.append(num)
print(num_alt)
fs.primos(num_alt)