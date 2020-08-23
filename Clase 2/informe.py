import csv

# Acá van a quedar guardadas la lista de precios de venta y la lista con las compras realizadas:
precios = {}
compra_camion = []

def balance(archivo_precios, archivo_camion):
    #abro archivos
    f_precios = open(archivo_precios, 'rt')
    rows_precios = csv.reader(f_precios)
    
    f_camion = open(archivo_camion, 'rt')
    rows_camion = csv.reader(f_camion)
    encabezados = next(rows_camion)

    # leer_precios() {producto:precio de venta}
    for row in rows_precios:
        try:
            precios[row[0]] = float(row[1])
        except IndexError:
            pass
        
    # Sumo las ventas  
    total_venta = 0.0
    for k, v in precios.items():
        total_venta+= precios[k]
    print("El total de la venta fue:", total_venta)
    
    # leer_camion() {nombre: '', cajones: '', precio:''}
    # Sumo las compras
    total_compra = 0.0
    for row in rows_camion:
        camion = dict(zip(encabezados, row))
        total_compra += int(camion["cajones"]) * float(camion["precio"])
        compra_camion.append(camion) 
    print("El total de la compra fue:", total_compra)
    
    # Cierro los archivos
    f_precios.close()
    f_camion.close()
    
    # Calculo de la diferencia
    diferencia = total_venta - total_compra
    
    # Mensaje final:
    if diferencia < 0:
        print("Hubo pérdida por un total de:", diferencia)
    elif diferencia > 0:
        print("Hubo una ganancia por un total de:", diferencia)
          
                      
informe_balance = balance("../Data/precios.csv", "../Data/fecha_camion.csv")
informe_balance