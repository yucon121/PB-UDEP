#codigo que permite registar una cantidad N de eventos, y filtra el de mayor ingresos 
eventos=[]
N=int(input("Ingrese la cantidad de eventos a registrar: "))
for i in range(N):
    nombre=str(input("Ingrese el nombre del evento: "))
    fecha=str(input("Ingrese la fecha del evento: "))
    precio_ent=float(input("Ingrese el precio de la entrada al evento: "))
    cant_ven=int(input("Ingrese la cantidad de entradas vendidas: "))
    ing_tot=precio_ent*cant_ven
    eventos.append([nombre, fecha, precio_ent, cant_ven, ing_tot])
mayor=eventos[0][4]
evento_mayor=eventos[0][0]
for i in range(len(eventos)): #for venta in ventas:
    if eventos[i][4]>mayor: #if venta[4]>mayor:
        mayor=eventos[i][4] #mayor=venta[4]
        evento_mayor=eventos[i][0] #eventor_mayor=venta[0]
print(f"El evento con mayor ingreso es: {evento_mayor} con un ingreso de: {mayor}")