import csv
import sys
from fileparse import parse_csv 

def leer_camion(nombre_archivo):
	contenido_camion = parse_csv(nombre_archivo, select=['nombre','cajones','precio'], types=[str, int, float])
	#f = open(nombre_archivo)
	#rows = csv.reader(f)
	#headers = next(rows)
	#contenido_camion = []
	#for n_row, row in enumerate(rows, start=1):
	 	#record = dict(zip(headers, row))
	 	#try:
	 		#contenido_camion.append({'nombre': record['nombre'], 'cajones': int(record['cajones']), 'precio': float(record['precio'])})
	 	#except ValueError:
	 		#print(f'Fila {n_row}: No pude interpretar: {row}')
	return contenido_camion

def leer_precios(nombre_archivo):
	lista_precios = parse_csv(nombre_archivo, types=[str, float], has_headers = False)
	# f = open(nombre_archivo, 'r')
	# rows = csv.reader(f)
	# lista_precios = {}
	# for n_row, row in enumerate(rows, start=1):
	# 	try:
	# 		lista_precios[row[0]] = float(row[1])
	# 	except:
	#		print(f'Fila {n_row}: No pude interpretar: {row}')
	return lista_precios

def imprimir_informe(nombre_archivo1,nombre_archivo2):
    camion = leer_camion(nombre_archivo1)
    precios = leer_precios(nombre_archivo2)
    headers = ('Nombre', 'Cajones', 'Precio', 'Cambio')
    sep = ('----------')
    print(f'{headers[0]:>10s} {headers[1]:>10s} {headers[2]:>10s} {headers[3]:>10s}')
    print(f'{sep:>10s} {sep:>10s} {sep:>10s} {sep:>10s}')
    for s in camion:
        lista = ((s['nombre'], s['cajones'], '$' + str(s['precio']), precios[0][1] - s['precio']))
        print('%10s %10d %10s %10.2f' % lista)
 
def informe_camion(nombre_archivo_camion, nombre_archivo_precios):
    leer_camion(nombre_archivo_camion)
    leer_precios(nombre_archivo_precios)
    imprimir_informe(nombre_archivo_camion, nombre_archivo_precios)


imprimir_informe('Data/camion.csv','Data/precios.csv')
informe_camion('Data/fecha_camion.csv','Data/precios.csv') #esta deberìa ser la última función en llamarse

#leer_camion('Data/fecha_camion.csv')
#leer_precios('Data/precios.csv')

files = ['Data/camion.csv', 'Data/camion2.csv']
for name in files:
    print(f'{name:-^43s}')
    informe_camion(name, 'Data/precios.csv')
    print()
    
    