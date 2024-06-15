import funciones1506 as fs
registros=[]
inicio=True
while inicio==True:
    fs.opciones_menu()
    seleccion=int(input("Elija una opcion: "))
    match seleccion:
        case 1:
            fs.almacenar_ult_dig(registros)
        case 2:
            fs.registros_sin_repetir(registros)
        case 3:
            fs.num_mayor(registros)
        case 4:
            inicio=False
            print("Programa terminado")
        case _:
            print("Opcion no valida")