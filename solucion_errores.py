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