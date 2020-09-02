# -*- coding: utf-8 -*-
#Clase 4
# Debuggear
#Ejercicio 4.1: Debugger
#Ejercicio 4.2: Más debugger
# Análisis de alternativas para propagar
#Ejercicio 4.3: Propagar por vecinos x
#Ejercicio 4.4: Propagar por como el auto fantástico x
#Ejercicio 4.5: Propagar con cadenas x
# Random
#Ejercicio 4.6: Generala servida
#Ejercicio 4.7: Generala no necesariamente servida generala.py xdonde pero se puede mejorar...
#Ejercicio 4.8: Envido xxx
#Ejercicio 4.9: Calcular pi xxx
#Ejercicio 4.11: Gaussiana termometro.py 
# 4.3 NumPy
#Ejercicio 4.12: arange() y linspace()
#Ejercicio 4.13: Guardar temperaturas 
#Ejercicio 4.14: Empezando a plotear
# 4.4 El album de Figuritas figuritas.py
#Ejercicios con figus sueltas
#Ejercicio 4.15: Crear
#Ejercicio 4.16: Incompleto
#Ejercicio 4.17: Comprar
#Ejercicio 4.18: Cantidad de compras
#Ejercicio 4.19:
#Ejercicio 4.20:
#Ejercicio 4.21:
#Ejercicio 4.22:
#Ejercicio 4.23:
#Ejercicio 4.24:
#Ejercicios un toque más estadísticos:
#Ejercicio 4.25:
#Ejercicio 4.26: Plotear el histograma
#Ejercicio 4.27: 
#Ejercicio 4.28:
#Ejercicio 4.29: x
# 4.5 Gráficos del Arbolado porteño
#Ploteando datos reales
#Ejercicio 4.30: Histograma de altos de Jacarandás
#Ejercicio 4.31: Scatterplot (diámetro vs alto) de Jacarandás
##Ejercicio 4.32: Scatterplot para diferentes especies x
#%%

def tiene_a(expresion):
    n = len(expresion)
    i = 0
    while i<n:
        if expresion[i] == 'a':
            return True
        else:
            return False
        i += 1
#%%
#Ejercicio 4.1: Debugger
def invertir_lista(lista):
    '''Recibe una lista L y la develve invertida.'''
    invertida = []
    i=len(lista)
    while i > 0:    # tomo el último elemento 
        i=i-1
        invertida.append(lista[i])  # aquí estaba el bug. El método pop quitaba el elemento de l 
        print(lista)
    return invertida

l = [1, 2, 3, 4, 5]    
m = invertir_lista(l)
print(f'Entrada {l}, Salida: {m}')
#%%
# 4.2: Más debugger
#Siguiendo con los ejemplos del Ejercicio 3.1, usá el debugger para analizar el siguiente código:

import csv
from pprint import pprint

def leer_camion(nombre_archivo):
    camion=[]
    registro={} # acà está el problema. no está arreglado esto. 
    with open(nombre_archivo,"rt") as f:
        filas = csv.reader(f)
        encabezado = next(filas)
        for fila in filas:
            registro[encabezado[0]] = fila[0]
            registro[encabezado[1]] = int(fila[1])
            registro[encabezado[2]] = float(fila[2])
            camion.append(registro)
    return camion

camion = leer_camion(".../Data/camion.csv")
pprint(camion)

#%%
# Análisis de alternativas para propagar
#Ejercicio 4.3: Propagar por vecinos

def propagar_al_vecino(l):
    modif = False
    n = len(l)
    for i,e in enumerate(l):
        if e==1 and i<n-1 and l[i+1]==0:
            l[i+1] = 1
            modif = True
        if e==1 and i>0 and l[i-1]==0:
            l[i-1] = 1
            modif = True
    return modif

def propagar(l):
    m = l.copy()
    veces=0
    while propagar_al_vecino(l):
        veces += 1

    print(f"Repetí {veces} veces la función propagar_al_vecino.")
    print(f"Con input {m}")    
    print(f"Y obtuve  {l}")
    return m
#%%
propagar([0,0,0,0,1])
propagar([0,0,1,0,0])
propagar([1,0,0,0,0])

#%%
'''
Preguntas:

¿Por qué los tests l[i+1]==0 y l[i-1]==0 de la función propagar_al_vecino no causan un IndexError en los bordes 
de la lista?
¿Por qué propagar([0,0,0,0,1]) y propagar([1,0,0,0,0]), siendo entradas perfectamente simétricas, no generan 
la misma cantidad de repeticiones de llamadas a la función propagar_al_vecino?
Sobre la complejidad. Si te sale, calculá:
¿Cuántas veces como máximo se puede repetir el ciclo while en una lista de largo n?
¿Cuántas operaciones hace "propagar_al_vecino" en una lista de largo n?
Entonces, ¿cuántas operaciones hace como máximo esta versión de propagar en una lista de largo n? 
¿Es un algoritmo de complejidad lineal o cuadrática?
'''
#%%
#Ejercicio 4.4: Propagar por como el auto fantástico
def propagar_a_derecha(l):
    n = len(l)
    for i,e in enumerate(l):
        if e==1 and i<n-1:
            if l[i+1]==0:
                l[i+1] = 1
    return l
#%
def propagar_a_izquierda(l):
    return propagar_a_derecha(l[::-1])[::-1]
#%
def propagar(l):
    ld=propagar_a_derecha(l)
    lp = propagar_a_izquierda(ld)
    return lp
#%%
l = [0,0,0,-1,1,0,0,0,-1,0,1,0,0]
print("Estado original:  ",l)
print("Porpagando...")
lp=propagar(l)
print("Estado original:  ",l)
print("Estado propagado: ",lp)
#%%
'''
Preguntas:

¿Por qué se modificó la lista original?
¿Por qué no quedó igual al estado propagado?
Corregí el código para que no cambie la lista de entrada.
¿Cuántas operaciones hace como máximo propagar_a_derecha en una lista de largo n?
Sabiendo que invertir una lista ([::-1]) requiere una cantidad lineal de operaciones en la longitud de la lista 
¿Cuántas operaciones hace como máximo propagar en una lista de largo n?
'''
#%%
#Ejercicio 4.5: Propagar con cadenas
#Esta versión usa métodos de cadenas para resolver el problema separando los fósforos en grupos sin 
#fósforos quemados y analizando cada grupo. Sin embargo algo falla...

def trad2s(l):
    '''traduce una lista con 1,0 y -1 
    a una cadena con 'f', 'o' y 'x' '''
    d={1:'f', 0 :'o', -1:'x'}
    s=''.join([d[c] for c in l])
    return s

def trad2l(ps):
    '''traduce cadena con 'f', 'o' y 'x'
    a una lista con 1,0 y -1'''
    inv_d={'f':1, 'o':0, 'x':-1}
    l = [inv_d[c] for c in ps]
    return l

def propagar(l, debug = True):
    s = trad2s(l)
    if debug:
        print(s)#, end = ' -> ')
    W=s.split('x')
    PW=[w if ('f' not in w) else 'f'*len(w) for w in W]
    ps=''.join(PW)
    if debug:
        print(ps)
    return trad2l(ps)

#%%
l = [0,0,0,-1,1,0,0,0,-1,0,1,0,0]
lp = propagar(l)
print("Estado original:  ",l)
print("Estado propagado: ",lp)
#%%
'''
Preguntas:

¿Porqué se acorta la lista?
¿Podés corregir el error agregando un solo caracter al código?
¿Te parece que este algoritmo es cuadrático como el Ejercicio 4.3 o lineal como el Ejercicio 4.4?
'''
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
    
#N = 100000
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
# HECHO EN OTRO ARCHIVO
#%%
#Elección con reposición
caras = ['uno', 'dos', 'tres', 'cuatro', 'cinco', 'seis']
print(random.choice(caras))
print(random.choices(caras, k=3))

#Elección sin reposición
print(random.sample(caras, k = 4))
#%%
import random
#Primero armamos el mazo:
valores = [1, 2, 3, 4, 5, 6, 7, 10, 11, 12]
palos = ['oro', 'copa', 'basto', 'espada']
naipes = [(valor,palo) for valor in valores for palo in palos]   

#naipes = [dict(zip(valor, palo)) for valor in valores for palo in palos]  
#print(random.sample(naipes, k=3))
    
#%%
#Ejercicio 4.8: Envido
'''
Teniendo en cuenta las reglas del Truco, estimá la probabilidad de obtener 31, 32 o 33 puntos de envido en una mano.
¿Son iguales estas tres probabilidades? ¿Por qué?
Observación: como corresponde, en esta materia jugamos al truco sin flor.
Guardá este ejercicio en un archivo envido.py para entregar.        
'''
import random

def mezclo_y_reparto():
    valores = [1, 2, 3, 4, 5, 6, 7, 10, 11, 12]
    palos = ['oro', 'copa', 'basto', 'espada']
    naipes = [(valor,palo) for valor in valores for palo in palos]
    random.shuffle(naipes)
    mano = naipes[-3:]
    
    return mano

def envido(mano):
    tengo = {'oro': [], 'copa': [], 'basto': [], 'espada': []}
    tantos = 0
    n_envido = [4,5,6,7] #números con los que puedo hacer envido de 30,31,32

    # acá lleno el diccionario
    for carta in mano:
        if carta[1] in tengo:
            tengo[carta[1]].append(carta[0])
    
    #por cada "juego/mismo palo":
    for juego in tengo:
        #si son dos cartas del mismo palo y están entre el 4 y el 7
        if (len(tengo[juego]) == 2) and (min(tengo[juego]) >= 4) and (max(tengo[juego]) <= 7):
            tantos = sum(tengo[juego]) + 20
            
        #si son tres cartas del mismo palo, sumo las 3 y le resto la más chica. 
        elif(len(tengo[juego]) > 2) and (min(tengo[juego]) >= 4) and (max(tengo[juego]) <= 7):
            tantos = (sum(tengo[juego])) + 20 - (min(tengo[juego]))
    
    if tantos > 30 and tantos < 34:
        return True
    else:
        return False
    
N = 10000
G = sum([envido(mezclo_y_reparto()) for i in range(N)])
prob = G/N
print(f'Tiré {N} veces, de las cuales {G} saqué 31, 32 o 33.')
print(f'Podemos estimar la probabilidad de sacar un envido con esos tantos es de {prob:.6f}.')
#%%
#Ejercicio 4.9: Calcular pi   

#random.random() genera números aleatorios entre 0 y 1

def generar_punto:
    x = random.random()
    y = random.random()
return x,y

 x^2 + y^2 < 1

#%%
#Ejercicio 4.11: Gaussiana
#La función random.normalvariate(mu,sigma) genera números aleatorios según esta distribución de probabilidades.
#Por ejemplo, usando mu = 0 y sigma = 1 podemos generar 6 valores aleatorios así

for i in range(6):
    print(f'{random.normalvariate(0,1):.2f}', end=', ')
    
#%%
# termómetro.py
'''
Supongamos que una persona se compra un termómetro que mide la temperatura con un error aleatorio normal 
con media 0 y desvío estándar de 0.2 grados (error gaussiano). Si la temperatura real de la persona 
es de 37.5 grados, simulá usando normalvariate() (con mu y sigma adecuados) n = 99 valores medidos por el 
termómetro.

Imprimí los valores obtenidos en las mediciones de temperatura simuladas y luego, como resumen, cuatro líneas 
indicando el valor máximo, el mínimo, el promedio y la mediana de estas n mediciones. Guardá tu programa en el 
archivo termometro.py.
'''

mediciones = []

for i in range(99):
    mediciones.append(round(random.normalvariate(37.5, 0.2), 2))


print('Valor máximo:', max(mediciones))
print('Valor mìnimo:', min(mediciones))
print('Valor promedio:', sum(mediciones)/len(mediciones))
mediciones.sort()
print('Mediana mediciones:', mediciones[49])

#%%
# 4.3 NumPy
import numpy as np

a = np.array([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]])

#Ejercicio 4.12: arange() y linspace()
#Generá un vector que tenga los números impares entre el 1 y el 19 inclusive usando arange().
#Repetí el ejercicio usando linspace(). ¿Qué diferencia hay en el resultado?

b = np.arange(1, 19, 2)
c = np.linspace(1,19,8)

# Por omisión, el tipo de datos es flotante. Pero podes especificarlo:
#x = np.ones(2, dtype=np.int64)

# Ordenar
arr = np.array([2, 1, 5, 3, 7, 4, 6, 8])
np.sort(arr) # ordenarlos

#Concatenar
np.concatenate((b, c))

x = np.array([[1, 2], [3, 4]])
y = np.array([[5, 6]])

np.concatenate((x, y), axis=0)

#Shape, size, ndim
#reshape
#slicing
data = np.array([1, 2, 3])
data[-2:]

#slicing po condicion
a = np.array([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]])

print(a[a<5])

pares = a[a%2==0]

print(pares)

#imprimir índices
#%%
#Podés usar np.nonzero() para imprimir los índices de los elementos que son, digamos, menores que 5:
a = np.array([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]])
b = np.nonzero(a < 5)
print(b)

lista_de_coordenadas = list(zip(b[0], b[1]))
#%%
#Ejercicio 4.13: Guardar temperaturas
#Ampliá el código de termometro.py que escribiste en el Ejercicio 4.11 para que guarde el vector con las 
#temperaturas simuladas en el directorio Data de tu carpeta de ejercicios, en un archivo llamado Temperaturas.npy. 
#Hacé que corra 999 veces en lugar de solo 99.
import random
import numpy as np

mediciones = []

for i in range(999):
    mediciones.append(round(random.normalvariate(37.5, 0.2), 2))
    
mediciones = np.array(mediciones)
np.save('../Data/temperaturas.npy', mediciones)
#%%
#Ejercicio 4.14: Empezando a plotear

'''
Escribí un archivo plotear_temperaturas.py que lea el archivo de datos Temperaturas.npy con 999 mediciones 
simuladas que creaste recién y, usando el siguiente ejemplo, hacé un histograma de las temperaturas simuladas:
'''
temperaturas = np.load('../Data/temperaturas.npy')

import matplotlib.pyplot as plt

plt.hist(temperaturas,bins=25)
#%%
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

#No me queda claro si el album se llena correctamente o no. 
#porque deberìamos tener un if. Donde si un album no es cero, pase al sigu
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
                cant_figuritas+= figus_paquete * cant_amigues #acà quizá habrìa que multiplicar por cant de amigos
    
    return cant_figuritas / figus_paquete 
#%%
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

#%%
#Ejercicio 4.30: Histograma de altos de Jacarandás

#%%
#Ejercicio 4.31: Scatterplot (diámetro vs alto) de Jacarandás

#%%
#Ejercicio 4.32: Scatterplot para diferentes especies