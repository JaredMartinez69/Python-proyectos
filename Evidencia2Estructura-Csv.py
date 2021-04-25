import datetime
import os
import csv

separador=("*"*20)
contador = 0
reporte={}
registro_ventas = {}
venta_total = 0
ventas = {}
fechas={}
estado_fechas=[]


while True:
    print(separador+separador)
    print("1=Registra Venta\n2=Consultar de ventas\n3=generar reporte\nSalir")
    opcion=int(input("¿Que opcion desea llevar acabo? : "))
    if opcion == 1:
            contador = contador+1
            registro_ventas[contador] = []
            reporte[contador]=[]
            fecha_capturada=input("Porfavor ingresa una fecha  en formato de dd/mm/yyyy: ")
            fecha_procesada = datetime.datetime.strptime(fecha_capturada, "%d/%m/%Y").date()
            while True:
                desc_articulo = input("Dime la descripcion del articulo: ")
                piezas_vendidas = int(input("Dime la cantidad de piezas vendidas: "))
                precio_venta = float(input("Dime el precio de venta: "))
                monto_total = piezas_vendidas * precio_venta
                print("Su monto total a pagar es de $ ",monto_total)
                venta_total = venta_total + monto_total
                fechaclave=str(fecha_procesada)
                registro_ventas[contador].append([desc_articulo, piezas_vendidas, precio_venta, monto_total])
                reporte[contador].append([fechaclave,contador,desc_articulo, piezas_vendidas, precio_venta, monto_total])
                estado_fechas.append([fechaclave,contador,desc_articulo, piezas_vendidas, precio_venta, monto_total])
                respuesta = input("\n¿Deseas capturar otro articulo? (1-Si / 0-No): ")
                if respuesta == '0':
                    fechas[fechaclave]= reporte[contador]
                    print("El monto total de la venta es: ",venta_total)
                    ventas[contador]=venta_total
                    venta_total = 0 
                    break

    elif opcion == 2:
        consulta_venta = int(input("\nDime el ID de la venta que se desea consultar: "))
        if consulta_venta in registro_ventas:
            print("\nLa venta con ese identificador es: ", consulta_venta)
            print(separador)
            print("Descripcion\t" "Cantidad\t" "Precio venta\t" "Precio total")
            print("-"*65)
            for articulo in registro_ventas[consulta_venta]:
                print(f'{articulo[0]}\t\t{articulo[1]}\t\t{articulo[2]}\t\t{articulo[3]}')
            print(f'El precio total fue de: {ventas[consulta_venta]}')

        else:
            print("Ese identificador no fue capturado")
    elif opcion == 3:
        #SE AGREGAN LAS COLUMNAS PARA EL CSV
        columnas=("Fecha", "Clave", "Descripcion", "Piezas Vendidas", "Precio venta", "Monto Total")
        fecha_captura=input("ingrese la fecha fecha  de la que quiere realizar el reporte en formato dd/mm/yyyy: ")
        fecha_procesada=datetime.datetime.strptime(fecha_captura, "%d/%m/%Y").date()
        clave_de_fechas=str(fecha_procesada)
        #SE AGREGA EL CSV EN CASO QUE NO EXISTA
        if os.path.isfile('registro.csv'):
            columnas= None
            with open("registro.csv", "a") as archivo:
                 writer = csv.writer(archivo)
                 writer.writerows(fechas[fecha_procesada])
        else: #SI YA EXISTE SIMPLEMENTE AGREGA LOS NUEVOS DATOS
            j=0
            with open("registro.csv", "w") as archivo:
                lista_fechareporte=[]
                for i in range (0,1):
                    for registro in estado_fechas:
                        if fechaclave in estado_fechas[j][i]:
                            lista_fechareporte.append(estado_fechas[j])
                        if j < len(estado_fechas):
                            j=j+1 
                fechas[clave_de_fechas]=lista_fechareporte
                writer = csv.writer(archivo)
                writer.writerow(columnas)
                writer.writerows(fechas[clave_de_fechas]) 
            break
    elif opcion==4: 
        break
    else: 
        print("Has introducido una opcion invalida")