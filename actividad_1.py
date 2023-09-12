f = open("peso_estatura_genero.csv", "rt") # si en vez de w ponemos rt es para leer el archivo 
f.seek(0) # seek es para indicarle en que posicion del archivo queremos que empiece a leer, en este caso le decimos que empiece a leer desde la posicion 0
tabla = [] 
for l in f.readlines():  # readlines lee linea por linea la diferencai con readline es que readline lee solo una linea y readlines lee todas las lineas del archivo
    line = []
    line = l.split(",")
    line[-1] = line[-1].rstrip("\n") # rstrip elimina el caracter que le pasemos por parametro en este caso \n en el espacio final de la linea ya que espesificamos que el separador es la coma, el -1 es para que lo haga en la ultima posicion de la lista
    tabla.append(line)
print(tabla[0])

for line in tabla:
    print(line)
f.close()