#Precios
productos = [("lapiz",8),("borrador",3),("tajador",5),("cuaderno",10)]

with open ("productos.txt","w") as f:
    f.write("producto precio \n")
    for nombre, precio in productos:
        f.write(nombre + " " + str(precio) + "\n")

with open ("productos.txt","r") as f:
    for linea in f:
        print(linea)