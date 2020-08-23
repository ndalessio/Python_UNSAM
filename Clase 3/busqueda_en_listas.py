# -*- coding: utf-8 -*-
# 3.3 Listas y búsqueda lineal
# Ejercicios:
#Ejercicio 3.6: Búsquedas de un elemento
#Ejercicio 3.7: Búsqueda de máximo y mínimo

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

