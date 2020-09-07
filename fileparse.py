# -*- coding: utf-8 -*-
# fileparse.py
# Ejercicio 5.3: Parsear un archivo CSV fileparse.py

import csv
#%%
'''
def parse_csv(nombre_archivo):
    #
    #Parsea un archivo CSV en una lista de registros
    #
    with open(nombre_archivo) as f:
        rows = csv.reader(f)

        # Lee los encabezados
        headers = next(rows)
        registros = []
        for row in rows:
            if not row:    # Saltea filas sin datos
                continue
            registro = dict(zip(headers, row))
            registros.append(registro)

    return registros
'''
#%%
# Ejercicio 5.4: Selector de Columnas fileparse.py
# Ejercicio 5.5: Conversión de tipo
# Ejercicio 5.6: Trabajando sin encabezados
# Modificá la función parse_csv() de modo que permita, opcionalmente, convertir el tipo de los datos recuperados antes de devolverlos.
# Ejercicio 5.6: Trabajando sin encabezados

def parse_csv(nombre_archivo, select = None, types=None, has_headers=True):
    '''
    Parsea un archivo CSV en una lista de registros.
    Se puede seleccionar sólo un subconjunto de las columnas, determinando el parámetro select, que debe ser una lista de nombres de las columnas a considerar.
    '''
    with open(nombre_archivo) as f:
        filas = csv.reader(f)
        
        # Cheqeo si tiene headers
        if has_headers:

        # Lee los encabezados del archivo
            encabezados = next(filas)
    
            # Si se indicó un selector de columnas, buscar los índices de las columnas especificadas.
            # Y en ese caso achicar el conjunto de encabezados para diccionarios
    
            if select:
                indices = [encabezados.index(nombre_columna) for nombre_columna in select]
                encabezados = select
            else:
                indices = []
    
            registros = []
            for fila in filas:
                if not fila:    # Saltear filas vacías
                    continue
                # Filtrar la fila si se especificaron columnas
                if indices:
                    fila = [fila[index] for index in indices]
                
                if types:
                    fila = [func(val) for func, val in zip(types, fila)]
                    
                # Armar el diccionario
                registro = dict(zip(encabezados, fila))
                registros.append(registro)
        
        # Si no tiene header:
        if not has_headers:
        
            registros = []
            for fila in filas:
                if not fila:    # Saltear filas vacías
                    continue
                if fila:
                    fila = (fila[0], fila[1])
                if types:
                    fila = (types[0](fila[0]), types[1](fila[1]))
            
                registros.append(fila)

    return registros


camion = parse_csv('Data/camion.csv', types=[str, int, float])
precios = parse_csv('Data/precios.csv', types=[str, float], has_headers=False)


'''
  for s in camion:
        precio = [tupla[1] for tupla in precios if tupla[0] == s['nombre']  ]
        lista = ((s['nombre'], s['cajones'], '$' + str(s['precio']), precio[0] - s['precio']))
        print('%10s %10d %10s %10.2f' % lista)          
 '''           