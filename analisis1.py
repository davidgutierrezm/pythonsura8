from cgitb import html, text
from distutils import text_file
from turtle import pd


import pandas as pd

# Cargar los datos
dataFrame = pd.read_csv('./empleados.csv')
#print(dataFrame)

# Cargar todos los datos
#print(dataFrame.to_string())

# Cargar los primeros N registros de un banco de datos
#print(dataFrame.head(50))

# Cargar los ulitmos N registros de un banco de datos
#print(dataFrame.tail(50))

# Obtener informacion de los datos cargados
#print(dataFrame.info())
#print(dataFrame.describe())

# Acceder a datos o registros especificos 
#print(dataFrame["nombres"].head())
#print(dataFrame["salario"].tail(20))

# Acceder a registros con su indice 
#print(dataFrame.iloc[20:30])
#print(dataFrame.loc[[10,20,30,40,100,200,300]])
 
#para comentar un bloque con tres comillas sencillas 
'''
tabla=(dataFrame.loc[[1,5,10],["nombres","salario"]])
html=tabla.to_html()
text_file=open("index.html","w")
text_file.write(html)
text_file.close()
'''

#Filtros con condiciones logicas
#print(dataFrame[dataFrame["salario"]>5500000].head(10))
print(dataFrame[(dataFrame["salario"] > 5500000) & (dataFrame["cargo"] == "analista2")])
