# -*- coding: utf-8 -*-
# Clase 5 
# ejercicios_python/fileparse.py
# Ejercicio 5.1: Estructurar un programa como una colección de funciones informe_funciones.py
# Ejercicio 5.2: Crear una función de alto nivel para la ejecución del programa. informe_funciones.py
# Ejercicio 5.3: Parsear un archivo CSV fileparse.py
# Ejercicio 5.4: Selector de Columnas fileparse.py
# Ejercicio 5.5: Conversión de tipo fileparse.py
# Ejercicio 5.6: Trabajando sin encabezados  xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
# 5.3 Módulos
# Ejercicio 5.7: Importar módulos
# Ejercicio 5.8: Usemos tu módulo fileparse.py
# Ejercicio 5.9: Un poco más allá
# 5.4 Búsqueda binaria
# Búsqueda sobre listas ordenadas
# Ejercicio 5.10: Búsqueda lineal sobre listas ordenadas.
#%%
#Ejercicio 5.7: Importar módulos
'''
import rebotes
import hipoteca
import informe 
import fileparse

camion = fileparse.parse_csv('Data/camion.csv',select=['nombre','cajones','precio'], types=[str,int,float])
lista_precios = fileparse.parse_csv('Data/precios.csv',types=[str,float], has_headers=False)
precios = dict(lista_precios)
# precios['Naranja']
'''
#%%
from fileparse import parse_csv  #de esta forma evitamos tener que escribir fileparse.parse_csv()
camion = parse_csv('Data/camion.csv', select=['nombre','cajones','precio'], types=[str,int,float])

#%%
#Ejercicio 5.9: Un poco más allá
import costo_camion
costo_camion.costo_camion('Data/camion.csv')

#%%
# Búsqueda sobre listas ordenadas
# Ejercicio 5.10: Búsqueda lineal sobre listas ordenadas.
'''
Modificá la función busqueda_lineal(lista, e) de la Sección 3.3 para el caso de listas ordenadas, de forma que la 
función pare cuando encuentre un elemento mayor a e. Llamá a tu nueva función busqueda_lineal_lordenada(lista,e) y 
guardala en el archivo busqueda_en_listas.py.
'''

def busqueda_lineal(lista, e):
    '''Si e está en la lista devuelve su posición, de lo
    contrario devuelve -1.
    '''
    lista.sort()
    
    pos = -1  # comenzamos suponiendo que e no está
    for i, z in enumerate(lista): # recorremos la lista
        if i <= e:
            if z == e:   # si encontramos a e
                pos = i  # guardamos su posición
                break    # y salimos del ciclo
        elif i > e:
            break
    return pos

resultado = busqueda_lineal([1, 4, 54, 3, 0, -1], 3)