# -*- coding: utf-8 -*-
#figuritas.py

#4.4 El album de Figuritas figuritas.py
# ¿Cuántas figuritas hay que comprar para completar el álbum del Mundial?
# Álbum con 670 figuritas.
#Cada figurita se imprime en cantidades iguales y se distribuye aleatoriamente.
#Cada paquete trae cinco figuritas.

import random
import numpy as np


#Ejercicios con figus sueltas   
#Ejercicio 4.15: Crear
#Implementá la función crear_album(figus_total) que devuelve un álbum (vector) vacío con figus_total espacios 
#para pegar figuritas

def crear_album(figus_total):
    album = np.zeros(figus_total, dtype = np.int64)
    return album
    
#%%
#Ejercicio 4.16: Incompleto

def album_incompleto(A):
    if 0 in A:
        return True
    else:
        return False

#%%
#Ejercicio 4.17: Comprar

def comprar(figus_total):
    return random.choice(np.arange(0, figus_total))
    
def cuantas_figus(figus_total):
    album = crear_album(figus_total)
    cant_figuritas = 0
    
    while album_incompleto(album):
        album[comprar(figus_total)] += 1
        cant_figuritas+= figus_paquete
    return cant_figuritas 

#%%
#Ejercicio 4.19:
'''
Ejecutá n_repeticiones = 1000 veces la función anterior utilizando figus_total = 6 y guardá en una lista los 
resultados obtenidos en cada repetición. Con los resultados obtenidos estimá cuántas figuritas hay que comprar, 
en promedio, para completar el álbum de seis figuritas.

Ayuda: El comando np.mean(l) devuelve el promedio de la lista l.

¿Podés crear esta lista usando una comprensión de listas?     
'''

n_repeticiones = 100

repeticiones = []
repeticiones.append([cuantas_figus(6) for i in range(n_repeticiones)])

promedio_album_6 = np.mean(repeticiones)
print(promedio_album_6)

#%%
#Ejercicio 4.20: figuritas.py
'''
Calculá n_repeticiones=100 veces la función cuantas_figus(figus_total=670) y guardá los resultados obtenidos 
en cada repetición en una lista. Con los resultados obtenidos estimá cuántas figuritas hay que comprar,
en promedio, para completar el álbum (de 670 figuritas).

Guardá todo lo que hiciste hasta aquí sobre figuritas en un archivo figuritas.py. Lo que sigue profundiza un 
poco más en el asunto.
'''

n_repeticiones = 100
lista_repeticiones = []
lista_repeticiones.append([cuantas_figus(670) for i in range(n_repeticiones)])

print(f"Necesitas comprar {np.mean(lista_repeticiones)} de figuritas en promedio para completar un album de 670 figuritas")

#%%
#Ejercicios con paquetes:
#Ejercicio 4.21:
#Simulá la generación de un paquete con cinco figuritas, sabiendo que el álbum es de 670.
#Tené en cuenta que, como en la vida real, puede haber figuritas repetidas en un paquete.

total_figuritas = np.arange(0, 10)
paquete = np.random.choice(total_figuritas, 5)
#%%
#Ejercicio 4.22:
#Implementá una función comprar_paquete(figus_total, figus_paquete) que, dado el tamaño del álbum 
#(figus_total) y la cantidad de figuritas por paquete (figus_paquete), genere un paquete (vector) de figuritas
# al azar.

def comprar_paquete(figus_total, figus_paquete):
    paquete = np.random.choice(np.arange(0, figus_total), figus_paquete)
    return paquete

print(comprar_paquete(670,5))
#%%
#Ejercicio 4.23:
#Implementá una función cuantos_paquetes(figus_total, figus_paquete) que dado el tamaño del álbum y 
#la cantidad de figus por paquete, genere un álbum nuevo, simule su llenado y devuelva cuántos paquetes 
#se debieron comprar para completarlo.


def cuantos_paquetes(figus_total, figus_paquete):
    album = crear_album(figus_total)
    cant_figuritas = 0
    
    while album_incompleto(album):
        album[comprar_paquete(figus_total, figus_paquete)] += 1
        cant_figuritas+= figus_paquete
    return cant_figuritas / figus_paquete 
#%%
#Ejercicio 4.24:
#Calculá n_repeticiones = 100 veces la función cuantos_paquetes, utilizando figus_total = 670,
#figus_paquete = 5. Guarda los resultados obtenidos en una lista y calculá su promedio. Si te da la compu,
#hacelo con 1000 repeticiones.

n_repeticiones = 1000

lista = []
lista.append([cuantos_paquetes(670,5) for i in range(n_repeticiones)])
print(f"Es necesario comprar, en promedio, {np.mean(lista)} para llenar el album de figuritas")

#%%
#Ejercicios un toque más estadísticos:
##Ejercicio 4.26: Estimar cual es la probabiliad de necesitar comprar hasta 850 figuritas para llenar el album

n_paquetes_hasta_llenar = np.array(lista) #en lista tengo guardada las simulaciones
cantidad = (n_paquetes_hasta_llenar <= 850).sum() #sumo la cantidad de veces que necesité compprar hasta 850 paquetes de figus

probabilidad_hasta850 = (cantidad / np.mean(lista)) * 100
print(probabilidad_hasta850)
#%%
#Ejercicio 4.26: Plotear el histograma
#Usá un código similar al del Ejercicio 4.14 para hacer un histograma de la cantidad de paquetes que se 
#compraron en cada experimeto, ajustando la cantidad de bins para que el gráfico se vea lo mejor posible.

np.save('../Data/paquetes_necesarios.npy', n_paquetes_hasta_llenar)
#%%
paquetes = np.load('../Data/paquetes_necesarios.npy')

import matplotlib.pyplot as plt
#plt.hist(paquetes, bins=10)
#%%
#Ejercicio 4.27:
#Utilizando lo implementado, estimá cuántos paquetes habría que comprar para tener una chance del 90% de completar
# el álbum.

promedio = np.mean(lista)
probabilidad_90 = promedio * 90 /100
print(probabilidad_90)

#%%
#Ejercicio 4.28:
#Repetí suponiendo que no hay figuritas repetidas en un paquete. ¿Cuánto cambian las probabilidades?

#comprar_paquete toma como parámetro el total de figuritas que tiene el album y la cantidad de figus que vienen en un paquete.
#un paquete es un número del 0 a la cantidad de figuritas del album, y devuelve la cant de figus que viene en un paquete


def comprar_paquete(figus_total, figus_paquete):
    paquete = np.random.choice(np.arange(0, figus_total), figus_paquete, replace=False) 
    return paquete

#cuantos_paquetes toma como parámetro la cant de figus que tiene un album, y la cant de figus de c/paquete
#crea el album, que es un array vacío de 0. La cant de 0 depende del tamaño del album.
#album[array de figuritas que nos tocí] += 1 / es decir, suma 1 a esos lugares del album.
#el ciclo continua mientras haya ceros en el album, es decir, album_incompleto == True
#devuelve cant_figuritas / figus_paquete porque queremos saber cuàntos paquetes tuvimos que comprar, no figus. 
    
def cuantos_paquetes(figus_total, figus_paquete):
    album = crear_album(figus_total)
    cant_figuritas = 0
    
    while album_incompleto(album):
        album[comprar_paquete(figus_total, figus_paquete)] += 1
        cant_figuritas+= figus_paquete
    return cant_figuritas / figus_paquete 

#n_repeticiones = 1000

lista = []
lista.append([cuantos_paquetes(670,5) for i in range(n_repeticiones)])
#print(f"Es necesario comprar, en promedio, {np.mean(lista)} para llenar el album de figuritas")
#
#%%
#Ejercicio 4.29: Cooperar vs competir
'''
Por último, suponé que cinco amigues se juntan y deciden compartir la compra de figuritas y el llenado 
de sus cinco álbumes solidariamente. Calculá cuántos paquetes deberían comprar si deben completar todos.
Hacé 100 repeticiones y compará el resultado con la compra individual que calculaste antes
'''
#La diferencia con la fx anterior es que esta vez agregamos el parámetro cant de amigos. Por cada amigue que se sume
#se compra un nuevo paquete. Luego creamos un "total_paquetes" que es un array colaborativo. 

def comprar_paquetes_colab(cant_amigues,figus_total, figus_paquete):
    total_paquetes = []
    for amigue in range(cant_amigues):
        total_paquetes.append(np.random.choice(np.arange(0, figus_total), figus_paquete))
    total_paquetes = np.concatenate((total_paquetes))
    return total_paquetes

#Acá cantidad de amigues y cantidad de albums podrían ser la misma variable, pero decidí separarla en caso de que dos
#amigues quieran llenar el mismo album. 

#No me queda claro si el album se llena correctamente o no...
#porque deberìamos tener un if. Donde si un album[posicion] es > 0, pase al siguiente.
'''
def cuantos_paquetes_colab(cant_amigues, cant_albums, figus_total, figus_paquete):
    album_grande = [] #album_grande es una lista con listas de albums
    cant_figuritas = 0
    
    for album in range(cant_albums):
        album_grande.append(crear_album(figus_total)) 
    
    for album in album_grande:
        while album_incompleto(album):
                album[comprar_paquetes_colab(cant_amigues, figus_total, figus_paquete)] += 1
                print(album)
                cant_figuritas+= figus_paquete * cant_amigues # 
    
    return cant_figuritas / figus_paquete 
    
''' 
#%%
''' 
def cuantos_paquetes_colab(cant_amigues, cant_albums, figus_total, figus_paquete):
    album_grande = [] #album_grande es una lista con listas de albums
    cant_figuritas = 0
    
    for album in range(cant_albums):
        album_grande.append(crear_album(figus_total)) 
        
    while album_incompleto(album_grande):
        for album in album_grande:
            if 0 in album[comprar_paquetes_colab(cant_amigues, figus_total, figus_paquete)]:
                album[comprar_paquetes_colab(cant_amigues, figus_total, figus_paquete)] += 1
            else:
                  pass
        cant_figuritas+= figus_paquete * cant_amigues
   
    return cant_figuritas / figus_paquete
 '''    


