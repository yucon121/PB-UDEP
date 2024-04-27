#algoritmo que pide calcular la division entre 2 numeros, ingresando el dividendo y el divisor
#USANDO UNICAMENTE SUMAS Y RESTAS
dividendo=int(input("Ingrese el dividendo: "))
divisor=int(input("Ingrese el divisor: "))
cont=0
while dividendo>=divisor:
    dividendo=dividendo-divisor
    cont+=1
conciente=cont
residuo=dividendo
print(f"el cociente es {conciente} y el residuo es {residuo}")