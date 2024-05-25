#Codigo que permite registrar libros con su titulo, autor, precio y su cantidad en stock, y filtra el de menor precio
libros=[]
N=int(input("Ingrese la cantidad de libros a registrar: "))
for i in range(N):
    print(f"libro {i+1}")
    titulo=str(input("Ingrese el titulo del libro: "))
    autor=str(input("Ingrese el autor del libro: "))
    precio=float(input("Ingrese el precio del libro: "))
    cant_stock=int(input("Ingrese la cantidad de stock del libro: "))
    libros.append([titulo, autor, precio, cant_stock])
menor=libros[0][2]
titulo_menor=libros[0][0]
for i in range(len(libros)):
    if libros[i][2]<menor:
        menor=libros[i][2]
        titulo=libros[i][0]
print(f"el titulo del libro con menor precio es: {titulo_menor} con un precio de: {menor}")