# -*- coding: utf-8 -*-
"""
generala.py
"""

def tirar(cant_dados):
   tirada = []
   for i in range(cant_dados):
       tirada.append(random.randint(1,6))
   return tirada   

#%%
  
def tirar_3_veces():
    # tiro dados 1 vez
    caras = {1: [], 2: [], 3: [], 4: [], 5: [], 6: []}
    tiro_1 = tirar(5)
    #print("tiro_1:", tiro_1)

    #agrupo y veo qué salió
    for dado in tiro_1:
        caras[dado].append(dado)
    #print(caras)
    
    #eligo con los dados que me voy a quedar:
    dados_selec = []
    for rep in caras:
        if len(caras[rep]) > len(dados_selec):
            dados_selec = caras[rep]
            
    #print("dados select", dados_selec) 

    # tiro 2 de acuerdo a la cantidad de dados que no "guardé"
    # tengo que resolver la posibilidad de que en el primer tiro sean todos dif, y en el segundo agarre 2
    tiro_2 = tirar(5-len(dados_selec))
    
    #print("tiro_2", tiro_2)
    
    for i in tiro_2:
        if i in dados_selec:
            dados_selec.append(i)


    #print("dados al tiro dos:", dados_selec)
    
    tiro_3 = tirar(5-len(dados_selec))
    
    for i in tiro_3:
        if i in dados_selec:
            dados_selec.append(i)
            
    #print("dados al tiro tres:", dados_selec)
    
    if len(dados_selec) == 5:
        return True
    else:
        return False

N = 10000
G = sum([tirar_3_veces() for i in range(N)])
prob = G/N
print(f'Tiré {N} veces, de las cuales {G} saqué generala servida.')
print(f'Podemos estimar la probabilidad de sacar generala servida mediante {prob:.6f}.')


