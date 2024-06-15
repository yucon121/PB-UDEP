#funciones del lab 15/06/2024
def primos(lista_num): #funcion primer caso
    primos_lista=[]
    for i in range(len(lista_num)):
        cont_div=0
        for j in range(1, lista_num[i]+1):
            if lista_num[i]%j==0:
                cont_div+=1
        if cont_div==2:
            primos_lista.append(lista_num[i])
    print(primos_lista)

#Funciones del segundo caso

def opciones_menu():
    print("Menu")
    print("1. Almacenar el ultimo digito de un numero ingresado por el usuario")
    print("2. Mostrar los registros sin repetir")
    print("3. Mostrar el numero mayor")
    print("4. Salir")

def almacenar_ult_dig(lista_vacia):
    cant= int(input("Ingrese la cantidad de numeros: "))
    for i in range(cant):
        num=int(input("Ingrese un numero entero: "))
        ult_dig=num%10
        lista_vacia.append(ult_dig)
        print(f"Ultimo digito {ult_dig} ha sido almacenado correctamente")

def registros_sin_repetir(lista_vacia):
    registros_unicos=[]
    for i in range(len(lista_vacia)):
        if lista_vacia[i] not in registros_unicos:
            registros_unicos.append(lista_vacia[i])
    print(f"Registros sin repetir: {registros_unicos}")

def num_mayor(lista_vacia):
    mayor=lista_vacia[0]
    for i in range(len(lista_vacia)):
        if lista_vacia[i]>mayor:
            mayor=lista_vacia[i]
    print(f"El numero mayor es: {mayor}")