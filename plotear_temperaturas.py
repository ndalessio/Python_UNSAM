# -*- coding: utf-8 -*-

#Ejercicio 4.14: Empezando a plotear

'''
Escribí un archivo plotear_temperaturas.py que lea el archivo de datos Temperaturas.npy con 999 mediciones 
simuladas que creaste recién y, usando el siguiente ejemplo, hacé un histograma de las temperaturas simuladas:
'''
temperaturas = np.load('../Data/temperaturas.npy') 

import matplotlib.pyplot as plt

plt.hist(temperaturas,bins=25)