#arboles.py

# Ejercicio 2.22 Lectura de los árboles de un parque

import csv
from pprint import pprint

def leer_parque(nombre_archivo, nombre_parque):
    arboles_parque = []
    with open(nombre_archivo, 'rt', encoding="utf8") as file:
        filas = csv.reader(file)
        encabezados = next(filas)

        for fila in filas:
            record = dict(zip(encabezados, fila))
    
            if record["espacio_ve"] == nombre_parque:
                arboles_parque.append(record)
    return arboles_parque
        

arboles_parque = leer_parque('../Data/arbolado-en-espacios-verdes.csv', 'GENERAL PAZ')
pprint(arboles_parque) 

# Ejercicio 2.23: Determinar las especies en un parque

def lista_arboles():
    nombres_arboles = []
    for arbol in arboles_parque:
        nombres_arboles.append(arbol['nombre_com'])
    nombres_arboles = set(nombres_arboles)
    return nombres_arboles

arboles = lista_arboles()
arboles

# Ejercicio 2.24: Contar ejemplares por especie

from collections import Counter

arboles_general_paz = leer_parque('../Data/arbolado-en-espacios-verdes.csv', 'GENERAL PAZ')
arboles_los_andes = leer_parque('../Data/arbolado-en-espacios-verdes.csv', 'ANDES, LOS')
arboles_centenario = leer_parque('../Data/arbolado-en-espacios-verdes.csv', 'CENTENARIO')

def contar_ejemplares(parque): 
    todos_los_arboles = []
    for item in parque:
        nombre_arbol = item['nombre_com']
        todos_los_arboles.append(nombre_arbol)
    lista_arboles = Counter(todos_los_arboles)
    print('Los árboles más comunes son:', lista_arboles.most_common(3))
    pprint(lista_arboles)
    

contar_ejemplares(arboles_centenario)