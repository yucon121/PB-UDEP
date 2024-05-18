import random
inicio=True
lista=[]
descarte=[]
multiplos=[]
residuo=[]
while inicio == True:
    print("Menu")
    print("1. Insertar 20 numeros aleatorios entre un rango de 1 - 200")
    print("2. Mostrar los valores que fueron descartados del almacenamiento")
    print("3. Mostrar los valores que no terminan en 3 pero son multiplos de 3")
    print("4. Eliminar todas las coincidencias correspondientes a un numero ingresado")
    print("5. Salir")
    resp=int(input("Elija una opcion: "))
    match resp:
        case 1:
            while len(lista)<20:
                num=random.randint(1,2000)
                if num%10!=1 and num%10!=4 and num%6!=0:
                    lista.append(num)
                else:
                    descarte.append(num)
            print(lista)
        case 2:
            print(descarte)
        case 3:
            for i in range(len(lista)):
                if lista[i]%10!=3 and lista[i]%3==0:
                    multiplos.append(lista[i])
            print(f"Multiplos de 3 que no terminan en 3: {multiplos}")
        case 4:
            eliminar=int(input("Ingrese el numero que desea eliminar: "))
            if eliminar in lista:
                for i in range(len(lista)):
                    if lista[i]!=eliminar:
                        residuo.append(lista[i])
                lista=residuo
                print(f"Lista actualizada: {lista}")
            else:
                print("El numero ingresado no se encuentra en la lista")
        case 5:
            inicio=False
        case _:
            print("Opcion no valida")