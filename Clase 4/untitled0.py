# -*- coding: utf-8 -*-
"""
Created on Wed Sep  2 00:37:53 2020

@author: nolis
"""


import random

def mezclo_y_reparto():
    valores = [1, 2, 3, 4, 5, 6, 7, 10, 11, 12]
    palos = ['oro', 'copa', 'basto', 'espada']
    naipes = [(valor,palo) for valor in valores for palo in palos]
    random.shuffle(naipes)
    mano = naipes[-3:]
    
    return mano

mano = [(12, 'espada'), (12, 'copa'), (2, 'basto')]

def tengo_envido(mano):
    print(mano)
    tengo = {'oro': [], 'copa': [], 'basto': [], 'espada': []}
    tantos = []
    valen_0 = [10, 11, 12]
    
    for carta in mano:
        if carta[1] in tengo:
            tengo[carta[1]].append(carta[0])
            
    for juego in tengo:
        if len(tengo[juego]) == 2:
            if any(valen_0 for x in tengo[juego]):
                tengo[juego][tengo[juego].index(10)] = 0
                tantos.append(sum(tengo[juego]) + 20)
            else:
                tantos.append(sum(tengo[juego]) + 20)
            
        if len(tengo[juego]) == 3:
            tantos.append(sum(tengo[juego]) + 20 - min(tengo[juego]))
        
        if len(tengo[juego]) == 1:
            maximo = max(tengo[juego])
            tantos.append(set(tengo[juego])
                         
    return tantos