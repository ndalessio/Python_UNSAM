# tablamult.py
lista_mayor = []

for i in range(10):
    lista_inicial = []
    suma = 0
    lista_suma = []
    
    for x in range(9):
        lista_inicial.append(i)
        suma = sum(lista_inicial)
        lista_suma.append(suma)
    lista_mayor.append(lista_suma) 
    
for list in lista_mayor:
    print(list)