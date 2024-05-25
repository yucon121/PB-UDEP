#Codigo que permite registrar a los invitados de la semana de la ingenieria, el codigo filtra los datos segun la edad y carrera
invitados=[]
prog=["Ingenieria Industrial y de Sistemas", "Ingenieria Civil", "Ingenieria Mecanico-Electrica", "Arquitectura"]
inicio=True
while inicio==True:
    nom=str(input("Ingrese el nombre del invitado(sin apellidos): "))
    ape=str(input("Ingrese los apellido del invitado: "))
    edad=int(input("Ingrese la edad del invitado: "))
    prog_aca=str(input("Ingrese el programa academico del invitado: "))
    if edad<18:
        print("Es menor de edad, registro no valido")
    elif prog_aca not in prog:
        print("Su programa academico no es parte de la UDEP, registro no valido")
    elif edad<18  and prog_aca not in prog:
        print("Es menor de edad y su programa academico no es parte de UDEP, registro no valido")
    else:
        print("Registro exitoso")
        invitados.append([nom, ape, edad, prog_aca])
    continuar=input("¿Desea registrar otro invitado? (S/N): ")
    if continuar=="n" or continuar=="N":
        inicio=False
print("Personas registradas en Ingenieria Industrial y de Sistemas:")
for i in range(len(invitados)):
    if invitados[i][3]=="Ingenieria Industrial y de Sistemas":
        print(invitados[i])