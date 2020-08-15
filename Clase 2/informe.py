# informe.py
total_compra = 0.0
total_venta = 0.0
ganancia = 0.0
precios = {}
camion = {}

def balance(archivo_precios, archivo_camion):
    
    f_precios = open(archivo_precios, 'rt')
    rows_precios = csv.reader(f_precios)
    
    f_camion = open(archivo_camion, 'rt')
    rows_camion = csv.reader(f_camion)
    encabezados = next(rows_camion)
    
    #'Fx para construir el diccionario de precios-ventas y calculo ventas'
    for row in rows_precios:
        try:
            precios[row[0]] = float(row[1])
        except IndexError:
            pass
    for k, v in precios.items():
        global total_venta
        total_venta+= precios[k]
    
    
    print("El total de la venta fue:", total_venta)
    
    #'Fx para construir la lista de dic de las compras del camion y calculo compras'   
    for row in rows_camion:
        global total_compra
        camion = dict(zip(encabezados, row))
        total_compra += int(camion["cajones"]) * float(camion["precio"])
    
    print("El total de la compra fue:", total_compra)
    
    #'Calculo de la diferencia'
    diferencia = total_venta - total_compra
    
    # Mensaje final:
    if diferencia < 0:
        print("Hubo pérdida por un total de:", diferencia)
    elif diferencia > 0:
        print("Hubo una ganancia por un total de:", diferencia)
          
            
            
informe_balance = balance("../Data/precios.csv", "../Data/camion.csv")
informe_balance