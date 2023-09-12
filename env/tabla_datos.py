import pandas as pd  # Importamos la librería pandas
import random
import numpy as np

df = pd.read_csv("peso_estatura_genero.csv")
df = pd.read_csv("peso_estatura_genero.csv")
df.Estatura = df.Estatura*2.54
df.Peso = df.Peso/2.2



df.columns  # muestra los nombres de las columnas
df.head() # muestra las primeras 5 filas
tail = df.tail(10)# muestra las ultimas 10 filas
filtro_190 = df[(df["Estatura"] > 190) & (df["Peso"] < 100)] # muestra las filas que cumplen la condicion


#media
print(df["Estatura"].mean())
print(filtro_190["Estatura"].mean())

#Media Recortada
sorted_df =df["Estatura"].sort_values() # sort_values ordena los valores de menor a mayor
sorted_df = sorted_df.reset_index(drop=True) # reset_index es para que no se muestre el indice original

p = 5
sum = 0
for i in range(p, len(sorted_df)-p):
    sum += sorted_df[i]
mean_recort = sum/(len(sorted_df)-2*p)
print(mean_recort) # the recorted mean is used to avoid outliers in order to get a more accurate mean


sorted_df[p:-p].mean() # the same as above but using pandas
print(sorted_df[p:-p].mean())

#media ponderada, es decir, la media de los pesos de cada fila ponderada por el peso de cada fila esto se hace para que las filas con mayor peso tengan mas peso en la media
weights = [ random.random() for i in range(len(df))] # random.random() genera un numero aleatorio entre 0 y 1 
sum2 = 0
for x in weights:
    sum2 += x
media_pond = df["Estatura"].values.flatten().dot(weights) #The point product of two arrays. Unlike numpy.dot the product might be a higher-rank tensor than the input arrays.
media_pond = media_pond/sum2
print("Media ponderada")
print(media_pond)

#moda 
moda = df["Genero"].mode() # mode() devuelve la moda de la columna que le pasemos por parametro en este caso Estatura, la moda es el valor que mas se repite en la columna
print("Moda")
print(moda)

#mediana 
mediana = df["Estatura"].median() # median() devuelve la mediana de la columna que le pasemos por parametro en este caso Estatura, la mediana es el valor que se encuentra en la mitad de la columna
print("Mediana")
print(mediana)

#Varianza
varianza = df["Estatura"].var() # var() devuelve la varianza de la columna que le pasemos por parametro en este caso Estatura, la varianza es la media de los cuadrados de las diferencias entre cada valor y la media
print("Varianza")
print(varianza) # la varianza es el cuadrado de la desviacion estandary se usa para medir la dispersion de los datos

#Desviacion estandar
desviacion_estandar = df["Estatura"].std() # std() devuelve la desviacion estandar de la columna que le pasemos por parametro en este caso Estatura, la desviacion estandar es la raiz cuadrada de la varianza
print("Desviacion estandar")
print(desviacion_estandar) # la desviacion estandar es una medida de la dispersion de los datos, nos dice que tan alejados estan los datos de la media por ejemplo si la desviacion estandar es 0 significa que todos los datos son iguales 

# un percentil es un valor de una variable estadistica que deja por debajo un porcentaje dado de los datos es decir si el percentil es 50% significa que el 50% de los datos son menores que el percentil

#Cuartiles son los percentiles 25, 50 y 75 es decir el 25% de los datos son menores que el primer cuartil, el 50% de los datos son menores que el segundo cuartil y el 75% de los datos son menores que el tercer cuartil
cuartiles = df["Estatura"].quantile([0.25, 0.5, 0.75]) # quantile() devuelve los cuartiles de la columna que le pasemos por parametro en este caso Estatura
print("Cuartiles")
print(cuartiles)