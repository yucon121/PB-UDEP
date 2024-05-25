atletas=[]
cat=["Junior", "Amateur", "Experto", "Juvenil", "Promesa"]
N=int(input("Ingrese la cantidad de registros: "))
while len(atletas)<N:
    nom=str(input("Ingrese los nombres del atleta: "))
    ape=str(input("Ingrese el apellido del atleta: "))
    categoria=str(input("Ingrese la categoria del atleta: "))
    if categoria in cat:
        tiempo=float(input("Tiempo (en segundos): "))
        atletas.append([nom, ape, categoria, tiempo])
    else:
        print("Categoria no valida")
suma=0
for i in range(len(atletas)):
    suma += atletas[i][3]
promedio=suma/len(atletas)
for j in range(len(atletas)):
    if atletas[i][3]>promedio:
        print(atletas[i][0], atletas[i][1])