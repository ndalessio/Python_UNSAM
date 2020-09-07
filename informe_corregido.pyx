# -*- coding: utf-8 -*-
#import csv
#import sys

def leer_camion(nombre_archivo):
    f = open(nombre_archivo, 'rt', encoding= 'UTF-8')
    rows = csv.reader(f)
    headers = next(rows)
    contenido_camion = []
    
    for n_row, row in enumerate(rows, start = 1):
        record = dict(zip(headers, row))
        try:
            contenido_camion.append({'nombre': record['nombre'], 'cajones' : record['cajones'], 'precios' : record['precios']})
        except:
            print(f'Fila {n_row}: No pude interpretar: {row}')
    return contenido_camion

camion = leer_camion('../Data/camion.csv')
print(camion)
print("chau")
