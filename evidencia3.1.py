import sqlite3
import datetime
import sys
from sqlite3 import Error
import os
import csv

separador = ("*"*60)
contador=0 


if os.path.isfile('registro.db'):
    pass
else:
    try:
        with sqlite3.connect("registro.db") as conn:
            c = conn.cursor()
            c.execute("CREATE TABLE IF NOT EXISTS ventas(ID_venta INTEGER, Descripcion TEXT, cantidad INT, Precio DECIMAL(6,2), Fecha TIMESTAMP NOT NULL);")
            print("Tabla creada exitosamente")
    except Error as e:
        print (e)
    except:
        print(f"Se produjo el siguiente error: {sys.exc_info()[0]}")





while True:
    print(separador) 
    print("Opcion 1.- registro de ventas")
    print("Opcion 2.- Consulta de ventas")
    print("Opcion 3.- Reporte registro fecha")
    print("Opcion 4.- Salir")
    print(separador) 
    opcion = int(input("Porfavor elige una opción :"))






    if opcion == 1:
        print(separador) 


        contador=contador+1   
        fecha_Capturada = input("Iingrese la fecha de la venta a capturar en formato dd/mm/yyyy. ")

        venta_total = []

        fecha_procesada = datetime.datetime.strptime(fecha_Capturada, "%d/%m/%Y").date()
        fecha_con_tiempo = datetime.datetime.combine(fecha_procesada, datetime.datetime.min.time()) #Es importante complementar la fecha con la parte horaria
        x = 1
        while True:
            

            Descripcion = input("Ingresa la descripcion del producto ")
            cantidad = int(input("Ingrese la cantidad de piezas vendidas "))
            precio = float(input("Ingrese el precio por unidad "))

            precio_venta = precio * cantidad
            venta_total.append(precio_venta)



            try:
                with sqlite3.connect("registro.db") as conn:
                    print("Conexión establecida")
                    mi_cursor = conn.cursor()               
                    criterios = {"Folio":contador, "Descripcion":Descripcion, "cantidad":cantidad, "Precio":precio, "Fecha":fecha_con_tiempo}
                    mi_cursor.execute("INSERT INTO ventas (IDventa, Descripcion, cantidad, Precio, Fecha) VALUES(:Folio, :Descripcion, :cantidad, :Precio, :Fecha)", criterios)
                    print("venta agregada exitosamente")
            except Error as e:
                print (e)
            except:
                print(f"Se produjo el siguiente error: {sys.exc_info()[0]}")
            finally:
                if (conn):
                    conn.close()
                    print("Se ha cerrado la conexión")
            opcion = int(input("¿Desea registrar otra venta? SI-(1)  NO-(0) "))


            if opcion == 0:
                print("El monto total de la venta es: ",venta_total[-1])
                venta_total = []
                break
            elif opcion == 1:
                pass
            else:
                print("Ha ingresado una opcion inválida")
                break

    elif opcion == 2:
        print(separador) 

        identificador = int(input("Dime el ID a consultar"))

        try:
            with sqlite3.connect("registro.db") as conn:
                mi_cursor = conn.cursor()
                criterios = {"identificador":identificador}
                mi_cursor.execute("SELECT * FROM ventas WHERE (IDventa) = :identificador;", criterios)
                registros = mi_cursor.fetchall()
                print(separador) 
                for IDventa, Descripcion, Piezas, Precio, Fecha in registros:
                    print("IDventa: ",IDventa)
                    print("Descripción: ",Descripcion)
                    print("Piezas: ", Piezas)
                    print("Precio: ", Precio)
                    print("Fecha: ",Fecha,"\n",separador)
        except sqlite3.Error as e:
            print (e)
        except Exception:
            print(f"Se produjo el siguiente error: {sys.exc_info()[0]}")
        finally:
            if (conn):
                conn.close()
                print("Se ha cerrado la conexión con la base de datos")







    elif opcion == 3:
        print(separador) 

        fecha_consultar = input("Dime una fecha (dd/mm/aaaa): ")
        fecha_consultar = datetime.datetime.strptime(fecha_consultar, "%d/%m/%Y").date()

        try:
            with sqlite3.connect("registro.db", detect_types = sqlite3.PARSE_DECLTYPES | sqlite3.PARSE_COLNAMES) as conn:
                mi_cursor = conn.cursor()
                criterios = {"fecha":fecha_consultar}
                mi_cursor.execute("SELECT * FROM ventas WHERE DATE(Fecha) = :fecha;", criterios)
                registros = mi_cursor.fetchall()

                print(f"\nDatos registrados en {fecha_consultar}:\n",separador) 
                for Folio_numerico, Descripcion, Piezas, Precio, Fecha in registros:
                    print(f"IDventa: \t\t{Folio_numerico}")
                    print(f"Descripción:\t{Descripcion}")
                    print(f"Piezas: \t{Piezas}")
                    print(f"Precio: \t{Precio}")
                    print(f"Fecha: \t\t{Fecha}\n",separador)
        except sqlite3.Error as e:
            print (e)
        except Exception:
            print(f"Se produjo el siguiente error: {sys.exc_info()[0]}")
        finally:
            if (conn):
                conn.close()
                print("Se ha cerrado la conexión con la base de datos")
    elif opcion == 4:
        print("chasquido de thanos")
        break









