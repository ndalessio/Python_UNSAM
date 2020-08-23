# -*- coding: utf-8 -*-
#Clase 3
# 3.1 Entorno de desarrollo integrado
# 3.2 Errores
#Ejercicio 3.1: Semántica - solucion_errores.py
#Ejercicio 3.2: Sintaxis
#Ejercicio 3.3: Tipos
#Ejercicio 3.4: Alcances
#Ejercicio 3.5: Pisando memoria
# 3.3 Listas y búsqueda lineal
#Ejercicio 3.6: Búsquedas de un elemento - busqueda_en_listas.py
#Ejercicio 3.7: Búsqueda de máximo y mínimo
#Ejercicio 3.8: Invertir una lista - invlista.py
#Ejercicio 3.9: Propagación - propaga.py xxxxxxxx
# 3.4 Comprensión de listas
#Ejercicio 3.10: Comprensión de listas
#Ejercicio 3.11: Reducción de secuencias
#Ejercicio 3.12: Consultas de datos
#Ejercicio 3.13: Extracción de datos
#Ejercicio 3.14: Extraer datos de una arhcivo CSV
# 3.5 Objetos
#Ejercicio 3.15: Datos de primera clase
#Ejercicio 3.16: Diccionarios
#Ejercicios 3.17: Fijando contenidos + Bonus
# 3.6 Arbolado porteño y comprensión de listas
#Ejercicio 3.18: Lectura de todos los árboles
#Ejercicio 3.19: Lista de altos de Jacarandá
#Ejercicio 3.20: Lista de altos y diámetros de Jacarandá
#Ejercicio 3.21: Diccionario con medidas

#%%
#Ejercicios de errores en el código
#Ejercicio 3.1: Semántica
#Comentario: Dos errores de tipo semántico. Línea 21 y Línea 25
#    Error línea 21: lo corregí modificando la expresión a minúscula.
#    Error línea 22: si la letra que estaba iterando no era 'a', se detenía el programa y devolvía False. No realizaba la suma i +=1. Lo corregí intercambiando el return por el i+=1
#    A continuación va el código corregido:

def tiene_a(expresion):
    expresion = expresion.lower()
    n = len(expresion)
    i = 0
    while i<n:
        if expresion[i] == 'a':
            return True
        else:
            i += 1
    return False

tiene_a('UNSAM 2020')
tiene_a('abracadabra')
tiene_a('La novela 1984 de George Orwell')

#%%
#Ejercicio 3.2: Sintaxis

#Comentario: Varios errores de tipo sintáxicos. Líneas 40, 43 y 47
#    Lo corregí añadiendo ":" para comenzar las intrucciones de c/ condición y escribiendo correctamente "False" en lugar de "Falso"
#    A continuación va el código corregido

def tiene_a(expresion):
    n = len(expresion)
    i = 0
    while i<n:
        if expresion[i] == 'a':
            return True
        i += 1
    return False
    
print(tiene_a('UNSAM 2020'))
print(tiene_a('abracadabra'))
print(tiene_a('La novela 1984 de George Orwell'))
#%%
#Ejercicio 3.3: Tipos
#Comentario: Error de tipo de ejecución en línea 60 (len=(expresion))
#    Lo corregí convirtiendo expresión a string
#    A continuación va el código corregido

def tiene_uno(expresion):
    expresion = str(expresion)
    n = len(expresion)
    i = 0
    tiene = False
    while (i<n) and not tiene:
        if expresion[i] == '1':
            tiene = True
        i += 1
    return tiene


print(tiene_uno('UNSAM 2020'))
print(tiene_uno('La novela 1984 de George Orwell'))
print(tiene_uno(1984))

#%%
#Ejercicio 3.4: Alcances
#La siguiente suma no da lo que debería:
#Comentario: Error de tipo de semántico en lìnea 82
#    Lo corregí ¡devolviendo la suma de ambos parámetros.
#    A continuación va el código corregido

def suma(a,b):
    return a + b
    
a = 2
b = 3
c = suma(a,b)
print(f"La suma da {a} + {b} = {c}")


#%%
#Ejercicio 3.5: Pisando memoria
#El siguiente ejemplo usa el dataset de la clase anterior, pero no lo imprime como corresponde, ¿podés determinar por qué y explicarlo brevemente en la versión corregida?
#Comentario: Error de tipo de semántico en línea 102. variable registro = {}
#    Lo corregí cambiando el lugar de esta variable, dentro del bucle for
#    El problema era que en cada vuelta del ciclo, la variable se modificaba. El resultado era la última versión de esta variable, ya que era una variable global. 
#    A continuación va el código corregido

import csv
from pprint import pprint

def leer_camion(nombre_archivo):
    camion=[]
    with open(nombre_archivo,"rt") as f:
        filas = csv.reader(f)
        encabezado = next(filas)
        
        for fila in filas:
            registro={}
            registro[encabezado[0]] = fila[0]
            registro[encabezado[1]] = int(fila[1])
            registro[encabezado[2]] = float(fila[2])
            camion.append(registro)
    return camion

camion = leer_camion("../Data/camion.csv")
pprint(camion)

#%%

#Ejercicio 3.6: Búsquedas de un elemento
#busqueda_en_listas.py

'''
En este primer ejercicio tenés que escribir una función buscar_u_elemento() que reciba una lista y un elemento y devuelva la posición de la última aparición de ese elemento en la lista (o -1 si el elemento no pertenece a la lista).
Agregale a tu programa busqueda_en_listas.py una función buscar_n_elemento() que reciba una lista y un elemento y devuelva la cantidad de veces que aparece el elemento en la lista. Probá también esta función con algunos ejemplos.
'''

def buscar_u_elemento(lista, e):
    pos = -1
    for i, z in enumerate(lista):
        if z == e:
            pos = i
    return pos
    
print(buscar_u_elemento([1,2,3,2,3,4],1))
print(buscar_u_elemento([1,2,3,2,3,4],2)) 
print(buscar_u_elemento([1,2,3,2,3,4],3)) 
print(buscar_u_elemento([1,2,3,2,3,4],5))

#%%
#Ejercicio 3.7: Búsqueda de máximo y mínimo
'''
Agregale a tu archivo busqueda_en_listas.py una función maximo() que busque el valor máximo de una lista de números positivos. Python tiene el comando max que ya hace esto, pero como práctica te propomenos que completes el siguiente código:
'''
def maximo(lista):
    '''Devuelve el máximo de una lista, 
    la lista debe ser no vacía y de números positivos.
    '''
    # m guarda el máximo de los elementos a medida que recorro la lista. 
    m = lista[0] # Lo inicializo en 0
    for e in lista: # Recorro la lista y voy guardando el mayor
        if e > m:
            m = e
    return m

print(maximo([1,2,7,2,3,4]))
print(maximo([1,2,3,4]))
print(maximo([-5,4]))
print(maximo([-5,-4]))

#%%
#Ejercitación con iteradores y listas

#Ejercicio 3.8: Invertir una lista
#Escribí una función invertir_lista(lista) que dada una lista devuelva otra que tenga los mismos elementos pero en el orden inverso. Es decir, el que era el primer elemento de la lista de entrada deberá ser el último de la lista de salida y análogamente con los demás elementos.

def invertir_lista(lista):
    invertida = []
    for i in range(len(lista)):
        invertida.append(lista[i-1])
    return invertida

print(invertir_lista([1, 2, 3, 4, 5]))
print(invertir_lista(['Bogotá', 'Rosario', 'Santiago', 'San Fernando', 'San Miguel']))

#%%
#Ejercicio 3.9: Propagación
#Imaginate una fila con varios fósforos uno al lado del otro. Los fósforos pueden estar en tres estados: nuevos, prendidos fuego o ya gastados (carbonizados). Representaremos esta situación con una lista L con un elemento por fósforo, que en cada posición tiene un 0 (nuevo), un 1 (encendido) o un -1 (carbonizado). El fuego se propaga inmediatamente de un fósforo encendido a cualquier fósoforo nuevo que tenga a su lado. Los fósforos carbonizados no se encienden nuevamente.

#Escribí una función llamada propagar que reciba un vector con 0's, 1's y -1's y devuelva un vector en el que los 1's se propagaron a sus vecinos con 0. Guardalo en un archivo propaga.py.
#  0 (nuevo), un 1 (encendido) o un -1 (carbonizado).

def propagar(lista):
    print(lista)
 

print(propagar([ 0, 0, 0,-1, 1, 0, 0, 0,-1, 0, 1, 0, 0]))
#%%
# 3.4 Comprensión de listas

# Ejemplos

a = [1, 2, 3, 4, 5]
b = [2* x for x in a]
print(b)    

nombres = ['Edmundo', 'Juana']
nombres_min = [nombre.lower() for nombre in nombres]
print(nombres_min)  
#%%
#Ejercicio 3.10: Comprensión de listas
nums = [1,2,3,4]
cuadrados = [ x * x for x in nums ]    
dobles = [ 2 * x for x in nums if x > 2 ]
  
#%%  
# Funciones necesarias para los próximos ejercicios:
import csv
import sys

# leer_camion()

def leer_camion(nombre_archivo):
    f = open(nombre_archivo, 'rt', encoding= 'UTF-8')
    rows = csv.reader(f)
    headers = next(rows)
    contenido_camion = []
    
    for n_row, row in enumerate(rows, start = 1):
        record = dict(zip(headers, row))
        print("record", record)
        try:
            contenido_camion.append({'nombre': record['nombre'], 'cajones' : int(record['cajones']),'precio' : float(record['precio'])})
        except: 
            print(f'Fila {n_row}: No pude interpretar: {row}')
    return contenido_camion
contenido = leer_camion('../Data/camion.csv')

def leer_precios(nombre_archivo):
    f = open(nombre_archivo, 'rt', encoding='UTF-8')
    rows = csv.reader(f)
    lista_precios = {}
    for n_row, row in enumerate(rows, start = 1):
        try:
            lista_precios[row[0]] = float(row[1])
        except:
            print(f'Fila {n_row}: No pude interpretar: {row}')

    return lista_precios

def hacer_balance(nombre_archivo1, nombre_archivo2):
    camion = leer_camion(nombre_archivo1)
    precios = leer_precios(nombre_archivo2)
    pago_prod = 0.0 
    valor_mercado = 0.0
    res = ''
    for s in camion:
        pago_prod += s['cajones'] * s['precio']
        valor_mercado += precios[s['nombre']] * (s['cajones'])
    if pago_prod > valor_mercado:
        res = 'perdida'
    else:
        res = 'ganancia'
    return(print(f'El pago al productor fue de: ${pago_prod}, la venta fue de ${valor_mercado} y hubo {res}'))
#%%      
#Ejercicio 3.11: Reducción de secuencias
camion = leer_camion('../Data/camion.csv')
costo = sum(s['cajones'] * s['precio'] for s in camion)
print(costo)

precios = leer_precios('../Data/precios.csv')
print("precios", precios)

valor = sum(s['cajones'] * precios[s['nombre']] for s in camion)
print(valor)

#%%
#Ejercicio 3.12: Consultas de datos

mas100 = [s for s in camion if s['cajones'] > 100]
print(mas100)

myn = [s for s in camion if s['nombre'] in {'Mandarina', 'Naranja'}]
print("Mandarina y naranja:", myn)

costo10k = [s for s in camion if s['cajones'] * s['precio'] > 10000]
print(costo10k)

#%%
# Ejercicio 3.13: Extracción de datos
'''
Usando un comprensión de listas, construí una lista de tuplas (nombre, cajones) que indiquen la cantidad de cajones de cada fruta tomando los datos de camion.
'''
nombres_cajones = [(s['nombre'], s['cajones']) for s in camion]
print(nombres_cajones)

# Comprensión de conjuntos:
# Si cambiás los corchetes ([,]) por llaves ({, }), obtenés algo que se conoce como comprensión de conjuntos. Vas a obtener valores únicos.
nombres = {s['nombre'] for s in camion}
print('nombres:', nombres)

# Si especificás pares clave:valor, podés construir un diccionario. 
# que es una comprensión de diccionario.
stock = {nombre : 0 for nombre in nombres}
print("stock", stock)

for s in camion:
    stock[s['nombre']] += s['cajones']
    
print(stock)

# Otro ejemplo útil podría ser generar un diccionario de precios de venta de aquellos 
#productos que están efectivamente cargados en el camión:

camion_precios = {nombre : precios[nombre] for nombre in nombres}
print(camion_precios)

#%%
# Ejercicio 3.14: Extraer datos de una arhcivo CSV
import csv
f = open('../Data/fecha_camion.csv')
rows = csv.reader(f)
headers = next(rows)
print(headers)

# definamos una lista que tenga las columnas que nos importan:
select = ['nombre', 'cajones', 'precio']

# Ubiquemos los índices de esas columnas en el CSV:
indices = [headers.index(ncolumna) for ncolumna in select]
print(indices)

#Y finalmente leamos los datos y armemos un diccionario usando comprensión de diccionarios:
row = next(rows)
record = {ncolumna: row[index] for ncolumna, index in zip(select, indices)}
print(record)

camion = [ { ncolumna: row[index] for ncolumna, index in zip(select, indices) } for row in rows ]
print(camion)

#%%
# 3.5 Objetos
# Ejercicio 3.15: Datos de primera clase

types = [str, int, float]

import csv
f = open('../Data/camion.csv')
rows = csv.reader(f)
headers = next(rows)
row = next(rows)
row = next(rows)
print(row)

types[1](row[1]) # Es equivalente a int(row[1])
    
# Hagamos un Zip de la lista de tipos con la de datos y veamos el resultado:

r = list(zip(types, row))
print(r)
# [(<class 'str'>, 'Naranja'), (<class 'int'>, '50'), (<class 'float'>, '91.1')]
#%%
# Esta lista zipeada es útil si querés realizar conversiones de todos los valores. Por ejemplo:

converted = []
for func, val in zip(types, row):
    converted.append(func(val))

print(converted)
print(converted[1] * converted[2]) # ahora sí se pueden multiplicar

# La última función puede abreviarse:
converted = [func(val) for func, val in zip(types, row)]

#%%
#Ejercicio 3.16: Diccionarios
#¿Te acordás que la función dict() te permite hacer fácilmente un diccionario si tenés una secuencia de tuplas con claves y valores? Hagamos un diccionario usando el encabezado de las columnas:    

carga_camion = { name: func(val) for name, func, val in zip(headers, types, row) }
print(carga_camion)

#%%
#Ejercicio 3.17: Fijando ideas
import csv
f = open('../Data/dowstocks.csv')
rows = csv.reader(f)
headers = next(rows)
row = next(rows)

print(headers)
print(row)

types = [str, float, str, str, float, float, float, float, int]
converted = [func(val) for func, val in zip(types, row)]
record = dict(zip(headers, converted))
print(record)

print(record['name'])

#%%
#Bonus: ¿Cómo modificarías este ejemplo para transformar la fecha (date) en una tupla como (6, 11, 2007)?

#%%
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
print('Altura Jacarandá:', altura)

#%%
#Ejercicio 3.20: Lista de altos y diámetros de Jacarandá
'''
En el ejercicio anterior usaste una sola linea para seleccionar las alturas de los Jacarandás en parques porteños. 
Ahora te proponemos que armes una nueva lista que tenga pares (tuplas de longitud 2) conteniendo no solo el alto 
sino también el diámetro de cada Jacarandá en la lista.
'''
medidas = [(float(arbol['altura_tot']), int(arbol['diametro'])) for arbol in arboleda if arbol['nombre_com'] == 'Jacarandá']
print(medidas)

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
medidas2 = []
for especie in especies:
    medidas2.append([{especie:(float(arbol['altura_tot']), int(arbol['diametro']))} for arbol in arboleda if arbol['nombre_com'] == especie])

especies = ['Eucalipto', 'Palo borracho rosado', 'Jacarandá']

def medidas_de_especies(especies, arboleda):
    medidas = []
    medidas.append([{e:(float(arbol['altura_tot']), int(arbol['diametro']))}for e in especies for arbol in arboleda if arbol['nombre_com'] == especie])
    return medidas

medidas = medidas_de_especies(especies, arboleda)

