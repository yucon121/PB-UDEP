pelis=[]
inicio=True
while inicio==True: #Menu de opcion segun los requerimientos
    print("Menu")
    print("1. Registrar peliculas")
    print("2. Buscar una pelicula por su genero")
    print("3. Peliculas con puntuacion mayor al promedio")
    print("4. salir")
    resp=int(input("Ingrese una opcion: "))
    match resp:
        case 1: #registro de peliculas
            N=int(input("Ingrese la cantidad de peliculas a registrar: "))
            for i in range(N):
                titu=str(input(f"Ingrese el titulo de la pelicula {i+1}: "))
                año=str(input(f"Ingrese el año de estreno de la pelicula {i+1}: "))
                puntuacion=float(input(f"Ingrese la puntuacion de la pelicula {i+1}: "))
                genero=str(input(f"Ingrese el genero de la pelicula {i+1}: "))
                pelis.append([titu, año, puntuacion, genero])
        case 2: #busqueda de peliculas
            if len(pelis)>0:
                gender=str(input("Ingrese el genero de pelicula que desea buscar: "))
                for i in range(len(pelis)):
                    if gender in pelis[i]:
                        print(pelis[i])
            else:
                print("No hay peliculas registradas")
        case 3: #promedio de puntuacion y busqueda a traves del mismo
            suma=0
            for i in range(len(pelis)):
                suma=suma+pelis[i][2]
            prom=suma/len(pelis)
            print(f"Promedio de puntuacion de peliculas registradas: {prom}")
            print("peliculas con puntuacion mayor al promedio: ")
            for i in range(len(pelis)):
                if pelis[i][2]>prom:
                    print(pelis[i])
        case 4: #fin del menu
            inicio=False
        case _: #en caso el usuario no ingrese una opcion existente
            print("Opcion no valida")