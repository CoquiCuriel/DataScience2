"""
El CSV contiene información sobre la producción de bioetanol en Argentina, 
en base a la caña de azucar y en base al maiz.
Intentaré mostrar información relevante en base a los datos recopilados.
DataSet de datos.gob.ar
"""


import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("bioetanol.csv", header=0,names=['Fecha', 'Caña_Azucar', 'Maiz'])
#print(df)

# Resumen de los datos del DataFrame
print("Resumen rápido de los datos del DataFrame")
print(df.describe())

# Guardamos el resumen en un diccionario por si necesitamos acceder a algún dato
resumen = df.describe().to_dict()
print(f"Cantidad de registros: -> {int(resumen['Maiz']['count'])}")

# Total de producción de bioetanol en base a la Caña de azucar
ultimo = int(df.Fecha.count())
print(f"El total de producción de bioetanol en base a la caña de azucar:\
      \nen el periodo {df.Fecha[0]} al {df.Fecha[ultimo-1]} fue de: {df.Caña_Azucar.sum()} m3\n")

# Total de producción de bioetanol en base al Maiz
print(f"El total de producción de bioetanol en base al Maiz:\
      \nen el periodo {df.Fecha[0]} al {df.Fecha[ultimo-1]} fue de: {df.Maiz.sum()} m3")

# Graficas de producción
fig, axs = plt.subplots(2,1, layout='constrained', figsize=(6,6))

# ---- axs[0] -------------
axs[0].set_title("Producción de bioetanol")
axs[0].plot(df.Fecha, df.Caña_Azucar, ".-m")
axs[0].plot(df.Fecha, df.Maiz, ".-g")

for labelx in axs[0].get_xticklabels():
    labelx.set_rotation(45)
    labelx.set_fontsize(8)
    labelx.set_horizontalalignment('right')

axs[0].set_ylabel("M3")
axs[0].legend(["Caña de azucar", "Maiz"])
axs[0].axis([-1, 29, 0, 70000])
axs[0].grid(True)

#---- axs[1] ---------------
# Gráfico de barras con totales

base = ['Caña de azucar', 'Maiz']
totales = [df.Caña_Azucar.sum(), df.Maiz.sum()]
axs[1].bar(base, totales, 0.5)
axs[1].set_title("Sumatorias de producción")
axs[1].set_ylabel("Millones de M3")

# Para finalizar descargamos la imagen
plt.savefig("Comparativa de producción.png", dpi=150)
plt.show()