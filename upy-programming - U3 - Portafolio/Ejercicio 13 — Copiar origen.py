#Copiar origen
with open("registro.txt","w") as f:
    f.write("linea 1\nlinea 2\nlinea 3\n")
    
with open("registro.txt","r") as origen, open("copia.txt","w") as destino:
    for linea in origen:
        destino.write(linea)

with open("copia.txt", "r") as f:
    print(f.read())