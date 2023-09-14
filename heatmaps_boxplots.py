
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures
import seaborn as sns
import sklearn.preprocessing
from sklearn.preprocessing import StandardScaler

df = pd.read_csv("agencia.csv")


# Scatter plot
plt.scatter(df["precio_auto"], df["kilometraje"], color="b", label="Correlacion", marker="*", s=30)

plt.xlabel("Precio")
plt.ylabel("Kilometraje")
plt.title("Precio vs Kilometraje")

plt.legend(loc="best")
plt.grid(True)

# Create the LinearRegression model
model = LinearRegression()

# Fit the model to the data
model.fit(df[["precio_auto"]], df["kilometraje"])

# Predict the values of the trendline
y_pred = model.predict(df[["precio_auto"]])

# Plot the trendline
plt.plot(df["precio_auto"], y_pred, color="red")


df = df.drop("id", axis = 1)
df.describe()   

# Rename the problematic column to a simpler name
df.rename(columns={"Puntos en compras (1-100)": "Puntos_en_compras"}, inplace=True)

# Now you can use the updated column name in your code
fig, axs = plt.subplots(1, 3, figsize=(14, 4))

sns.boxplot(data=df, y="edad", x="genero", ax=axs[0])
sns.boxplot(data=df, y="kilometraje", x="genero", ax=axs[1])
sns.boxplot(data=df, y="precio_auto", x="genero", ax=axs[2])

