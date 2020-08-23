# Ejercicio 2.33: Un desafío de formato

########## Para ejecutar hacer_informe() con formato, necesitas ejecutar estas dos funciones. Las separé para mayor legibilidad:

#### La primera: leer_precios()

def leer_precios(archivo_precios):
    with open(archivo_precios, 'rt') as f_precios:
        rows_precios = csv.reader(f_precios)
    
        for row in rows_precios:
            try:
                precios[row[0]] = float(row[1])
            except IndexError:
                pass

        for k, v in precios.items():
            global total_venta
            total_venta+= precios[k]
        return precios


precios = leer_precios("../Data/precios.csv")

#### Y la segunda: leer_camion() 
 
def leer_camion(archivo_camion):
    with open(archivo_camion, 'rt') as f_camion:
        rows_camion = csv.reader(f_camion)
        encabezados = next(rows_camion)

        for row in rows_camion:
            camion = {}
            global total_compra
            camion = dict(zip(encabezados, row))
            lista_camion.append(camion)
            total_compra += int(camion["cajones"]) * float(camion["precio"])
        return lista_camion
    
camion = leer_camion("../Data/camion.csv")

############# hacer_informe()
# No me quedó el signo $ tal cual pedía el ejercicio...

def hacer_informe(camion, precios): 
    fila_informe = []
    headers = [('Nombre', 'Cajones', 'Precio', 'Cambio')]
    
    for i in camion:
        for key, value in precios.items():
            if key == i['nombre']:
                cambio = round(float(value) - float(i['precio']), 2)
                dato = ((i['nombre'], int(i['cajones']), float(i['precio']), cambio))
                fila_informe.append(dato) 
    
    for nombre, cajones, precio, cambio in headers:
        print(f'{nombre:>10s} {cajones:>10s} {precio:>10s} {cambio:>10s}')
        print('---------- ---------- ---------- ----------')
    
    peso = '$'   
    
    for nombre, cajones, precio, cambio in fila_informe:
        print(f'{nombre:>10s} {cajones:>10d} {peso:>3s} {precio:>6.2f} {cambio:>10.2f}')

hacer_informe(camion, precios)