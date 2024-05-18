#codigo de gestion de notas
inicio=True
notas=[]
while inicio==True:
    print("Menu de calificaciones")
    print("1. Registrar N calificaciones")
    print("2. Mostrar calificaciones sin repetir")
    print("3. Mostrar la calificacion mas baja")
    print("4. Mostrar la calificacion mas alta")
    print("5. Mostrar promedio de calificaciones")
    print("6. Salir")
    resp=int(input("Eliga una opcion: "))
    match resp:
        case 1:
            N=int(input("Ingrese la cantidad de calificaciones a registrar: "))
            for i in range(N):
                nota=float(input("Ingresa la calificacion: "))
                notas.append(nota)
        case 2:
            descarte=[]
            for i in range(len(notas)):
                if nota[i] not in descarte:
                    descarte.append(nota[i])
        case 3:
            if len(notas)>0:
                mayor=notas[0]
                for i in range(len(notas)):
                    if notas[i]>mayor:
                        mayor=notas[i]
                print(f"Calificacion mas alta: {mayor}")
            else:
                print("La lista esta vacia")
        case 4:
            if len(notas)>0:
                menor=notas[0]
                for i in range(len(notas)):
                    if notas[i]<menor:
                        menor=notas[i]
                print(f"La calificacion menor es {menor}")
            else:
                print("La lista esta vacia")
        case 5:
            if len(notas)>0:
                suma=0
                for i in range(len(notas)):
                    suma=suma+notas[i]
                promedio=suma/len(notas)
                print(f"El promedio es: {promedio} ")
        case 6:
            inicio=False
        case _:
            print("Opcion no valida")
