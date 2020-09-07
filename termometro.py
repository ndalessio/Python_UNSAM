# -*- coding: utf-8 -*-
#termometro.py

#Ejercicio 4.11: Gaussiana
#La función random.normalvariate(mu,sigma) genera números aleatorios según esta distribución de probabilidades.
#Por ejemplo, usando mu = 0 y sigma = 1 podemos generar 6 valores aleatorios así

for i in range(6):
    print(f'{random.normalvariate(0,1):.2f}', end=', ')
    
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