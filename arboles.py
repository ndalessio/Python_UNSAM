#%%
#Ejercicios clase 3

# 3.6 Arbolado porteño y comprensión de listas
# Ejercicio 3.18: Lectura de todos los árboles
# arboles.py
'''
Basándote en la función leer_parque(nombre_archivo, parque) del Ejercicio 2.22, escribí otra
leer_arboles(nombre_archivo) que lea el archivo indicado y devuelva una lista de diccionarios
con la información de todos los árboles en el archivo. La función debe devolver una lista 
conteniendo un diccionario por cada árbol con todos los datos.
Vamos a llamar arboleda a esta lista.
'''
import csv 

def leer_arboles(nombre_archivo):
    f = open(nombre_archivo, encoding='UTF-8')
    rows = csv.reader(f)
    headers = next(rows)
    print(headers)
    arboleda = [dict(zip(headers, row)) for row in rows]
    return arboleda

arboleda = leer_arboles('../Data/arbolado-en-espacios-verdes.csv')
#%%
#Ejercicio 3.19: Lista de altos de Jacarandá
'''
Usando comprensión de listas y la variable arboleda podés por ejemplo armar la lista de la altura de los árboles.

H=[float(arbol['altura_tot']) for arbol in arboleda]
Usá los filtros (recordá la Sección 3.4) para armar la lista de los altos de los Jacarandás solamente.
''' 
altura_jacaranda = [float(arbol['altura_tot']) for arbol in arboleda if arbol['nombre_com'] == 'Jacarandá']
print('Altura Jacarandá:', altura_jacaranda)

#%%
#Ejercicio 3.20: Lista de altos y diámetros de Jacarandá
'''
En el ejercicio anterior usaste una sola linea para seleccionar las alturas de los Jacarandás en parques porteños. 
Ahora te proponemos que armes una nueva lista que tenga pares (tuplas de longitud 2) conteniendo no solo el alto 
sino también el diámetro de cada Jacarandá en la lista.
'''
medidas_jacaranda = [(float(arbol['altura_tot']), int(arbol['diametro'])) for arbol in arboleda if arbol['nombre_com'] == 'Jacarandá']
print(medidas_jacaranda)

#%%
#Ejercicio 3.21: Diccionario con medidas

'''
Te pedimos que armes un diccionario en el que estas especies sean las claves y los valores asociados sean 
los datos que generaste en el ejercicio anterior. Más aún, organizá tu código dentro de una función 
medidas_de_especies(especies,arboleda) que recibe una lista de nombres de especies y una lista como la del 
Ejercicio 3.18 y devuelve un diccionario cuyas claves son estas especies y sus valores asociados sean las 
medidas generadas en el ejercicio anterior.

Vamos a usar esta función la semana próxima. A modo de control, si llamás a la función con las tres 
especies del ejemplo como parámetro (['Eucalipto', 'Palo borracho rosado', 'Jacarandá']) 
y la arboleda entera, deberías recibir un diccionario con tres entradas (una por especie), cada una con una lista 
asociada conteniendo 4112, 3150 y 3255 pares de números (altos y diámetros), respectivamente.
'''
#medidas2 = []
#for especie in especies:
#    medidas2.append([{especie:(float(arbol['altura_tot']), int(arbol['diametro']))} for arbol in arboleda if arbol['nombre_com'] == especie])

especies = ['Eucalipto', 'Palo borracho rosado', 'Jacarandá']

def medidas_de_especies(especies, arboleda):
    medidas = []
    medidas.append([{e:(float(arbol['altura_tot']), int(arbol['diametro']))}for e in especies for arbol in arboleda if arbol['nombre_com'] == e])
    return medidas

medidas = medidas_de_especies(especies, arboleda)
print(medidas)
#%%
# Ejercicios Clase 4

import matplotlib.pyplot as plt
import numpy as np
'''
import os
os.path.join('Data', 'arbolado-en-espacios-verdes.csv')
arboleda = leer_arboles(nombre_archivo)
medidas = medidas_de_especies(especies, arboleda)
'''

#Ejercicio 4.30: Histograma de altos de Jacarandás
plt.hist(altura_jacaranda, bins = 20)

#%%
#Ejercicio 4.31: Scatterplot (diámetro vs alto) de Jacarandás

medidas_jacaranda = np.array(medidas_jacaranda)
plt.scatter(medidas_jacaranda[:,0], medidas_jacaranda[:,1], alpha=0.3)
plt.xlabel("diametro (cm)")
plt.ylabel("alto (m)")
plt.title("Relación diámetro-alto para Jacarandás")

#%%
#Ejercicio 4.32: Scatterplot para diferentes especies
#Acá no supe como hacerlo...


