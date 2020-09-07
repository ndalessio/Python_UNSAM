# -*- coding: utf-8 -*-
#costo_camion.py

import informe_funciones as inf

def costo_camion(nombre_archivo):
	# f = open(nombre_archivo)
	# rows = csv.reader(f)
	# headers = next(rows)
	# costo_total=0.0
	# for n_row, row in enumerate(rows, start=1):
	# 	record = dict(zip(headers, row))
	# 	try:
	# 		ncajones = int(record['cajones'])
	# 		precio = float(record['precio'])
	# 		costo_total += ncajones * precio
	# 	except ValueError:
	# 		print(f'Fila {n_row}: No pude interpretar: {row}')
	camion = inf.leer_camion(nombre_archivo)
	lista = []
	for s in camion:
		lista.append((s['cajones'])*(s['precio']))
	print('%10.2f' % sum(lista))


