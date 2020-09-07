#envido.py

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
def envido_31(mano):
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
    
    if tantos == 31:
        return True
    else:
        return False
    
#%%
def envido_32(mano):
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
    
    if tantos == 32:
        return True
    else:
        return False
#%%
def envido_33(mano):
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
    
    if tantos == 33:
        return True
    else:
        return False       
#%%

G_31 = sum([envido_31(mezclo_y_reparto()) for i in range(N)])
prob_31 = G/N
print(f'Tiré {N} veces, de las cuales {G_31} saqué 31.')
print(f'Podemos estimar la probabilidad de sacar un envido con esos tantos es de {prob_31:.6f}.')

G_32 = sum([envido_32(mezclo_y_reparto()) for i in range(N)])
prob_32 = G/N
print(f'Tiré {N} veces, de las cuales {G_32} saqué 32.')
print(f'Podemos estimar la probabilidad de sacar un envido con esos tantos es de {prob_32:.6f}.')

G_33 = sum([envido_33(mezclo_y_reparto()) for i in range(N)])
prob_33 = G/N
print(f'Tiré {N} veces, de las cuales {G_33} saqué 33.')
print(f'Podemos estimar la probabilidad de sacar un envido con esos tantos es de {prob_33:.6f}.')
