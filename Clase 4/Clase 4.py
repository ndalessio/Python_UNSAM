# -*- coding: utf-8 -*-
#Clase 4
# Debuggear
# Random
#Ejercicio 4.6: Generala servida
#Ejercicio 4.7: Generala no necesariamente servida generala.py donde pero se puede mejorar...
#Ejercicio 4.8:


#%%
# generala
import random

tirada = []

for i in range(5):
    tirada.append(random.randint(1,6))

print(tirada)

#%%
#Ejercicio 4.6: Generala servida
'''
Queremos estimar la probabilidad de obtener una generala servida en una tirada de dados. Podemos hacer la cuenta 
usando un poco de teoría de probabilidades, o podemos simular que tiramos los dados muchas veces y ver cuántas de 
esas veces obtuvimos cinco dados iguales. En este ejercicio vamos a usar el segundo camino.

Escribí una función tirar() que devuelva una lista con cinco dados generados aleatoriamente. Escribí otra función
llamada es_generala(tirada) que devuelve True si y sólo si los cinco dados de la lista tirada son iguales.

Luego analizá el siguiente código. Correlo con N = 100000 varias veces y observá los valores que obtenés.
Luego correlo algunas veces con N = 1000000 (ojo, hace un millón de experimentos, podría tardar un poco):
'''
def tirar():
    tirada = []
    for i in range(5):
        tirada.append(random.randint(1,6))
    return tirada

def es_generala(tirada):
    if len(set(tirada)) == 1:
        return True
    else:
        return False
    
N = 100000
G = sum([es_generala(tirar()) for i in range(N)])
prob = G/N
print(f'Tiré {N} veces, de las cuales {G} saqué generala servida.')
print(f'Podemos estimar la probabilidad de sacar generala servida mediante {prob:.6f}.')
#%%
#Ejercicio 4.7: Generala no necesariamente servida
'''
Si uno juega con las reglas originales (se puede volver a tirar algunos de los cinco dados hasta dos
veces, llegando hasta a tres tiradas en total) siguiendo una estrategia que intente obtener generala
(siempre guardar los dados que más se repiten y tirar nuevamente los demás) es más probable otener
una generala que si sólo consideramos la generala servida. Escribí un programa que estime la
probabilidad de obtener una generala en las tres tiradas de una mano y guardalo en un archivo 
generala.py.
'''
'''
primero lanzamos los dados. 
Si hay dados que se repiten, los tengo que guardar. 
'''
#%%
#Ejercicio 4.8: Envido
'''
Teniendo en cuenta las reglas del Truco, estimá la probabilidad de obtener 31, 32 o 33 puntos de envido en una 
mano. ¿Son iguales estas tres probabilidades? ¿Por qué?
'''


        

    
        



    
    











