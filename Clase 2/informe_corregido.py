def leer_camion(nombre_archivo):
    f = open(nombre_archivo, 'rt', encoding= 'UTF-8')
    rows = csv.reader(f)
    headers = next(rows)
    contenido_camion = []
    for n_row, row in enumerate(rows, start = 1):
        record = dict(zip(headers, row))
        try:
            contenido_camion.append({'nombre': record['nombre'], 'cajones' : int(record['cajones']),'precio' : float(record['precio'])})
        except: 
            print(f'Fila {n_row}: No pude interpretar: {row}')
    return contenido_camion
#%%
def leer_precios(nombre_archivo):
    f = open(nombre_archivo, 'rt', encoding='UTF-8')
    rows = csv.reader(f)
    lista_precios = {}
    for n_row, row in enumerate(rows, start = 1):
        try:
            lista_precios[row[0]] = float(row[1])
        except:
            print(f'Fila {n_row}: No pude interpretar: {row}')
    return lista_precios

#%%
def hacer_balance(nombre_archivo1, nombre_archivo2):
    camion = leer_camion(nombre_archivo1)
    precios = leer_precios(nombre_archivo2)
    pago_prod = 0.0 
    valor_mercado = 0.0
    res = ''
    for s in camion:
        pago_prod += s['cajones'] * s['precio']
        valor_mercado += precios[s['nombre']] * (s['cajones'])
    if pago_prod > valor_mercado:
        res = 'perdida'
    else:
        res = 'ganancia'
    return(print(f'El pago al productor fue de: ${pago_prod}, la venta fue de ${valor_mercado} y hubo {res}'))