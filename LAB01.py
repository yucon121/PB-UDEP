#Se pide hacer un codigo que permita registrar una lista de empleados con su nombre, departamento y años de experiencia
#Los que tengan menos de 2 años de experiencia deberan ser mandados a una sublista para darles una capacitacion
cantidad=int(input("Ingrese la cantidad de empleados: "))
empleados=[]
for i in range(cantidad):
    nombre=str(input("Nombre de empleado: "))
    departamento=str(input("Departamento: "))
    experiencia=int(input("Años de experiencia: "))
    empleados.append([nombre, departamento, experiencia])
print("Empleados asistentes a capacitacion: ")
for i in range(len(cantidad)):
    if empleados[i][2]<2:
        print(empleados[i][0])