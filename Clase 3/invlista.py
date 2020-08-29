#Ejercitación con iteradores y listas

#Ejercicio 3.8: Invertir una lista
#Escribí una función invertir_lista(lista) que dada una lista devuelva otra que tenga los mismos elementos pero en el orden inverso. Es decir, el que era el primer elemento de la lista de entrada deberá ser el último de la lista de salida y análogamente con los demás elementos.
# en la primer vuelta voy a pedir el elemento en la posición -1, en la 2da el -2, etc.

def invertir_lista(lista):
    invertida = []
    resto = 0 # empiezo en cero
    for i in range(len(lista)):
        resto -= 1 
        invertida.append(lista[resto]) 
    return invertida

print(invertir_lista([1, 2, 3, 4, 5]))
print(invertir_lista(['Bogotá', 'Rosario', 'Santiago', 'San Fernando', 'San Miguel']))