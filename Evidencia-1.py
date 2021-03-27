diccionario_ventas = {}
venta_total = 0
dict_total_venta = {}

while True:
    print("\n---------MENU NEGOCIO COSMETICA-------------")
    print("          1. Registrar una venta")
    print("          2. Consultar una venta")
    print("          3  Salir del programa")
    print('----------------------------------------------')
    opcion = input("Ingrese una opcion: ")

    if opcion == '1':
        llave = input("\nDime un numero identificador para la venta ")
        if llave in diccionario_ventas:
            print("\nEse identificador ya esta registrado, intenta con otro")
        else:
            diccionario_ventas[llave] = []
            while True:
                desc_articulo = input("Dime la descripcion de tu articulo: ")
                piezas_vendidas = int(input("Dime la cantidad de piezas que vendieron: "))
                precio_venta = float(input("Dime el precio de venta unitario: "))
                monto_total = piezas_vendidas * precio_venta
                print("Su monto total a pagar es de $ ",monto_total)
                venta_total = venta_total + monto_total
                diccionario_ventas[llave].append([desc_articulo, piezas_vendidas, precio_venta, monto_total])
                respuesta = input("\n¿Deseas capturar más articulo? (1-Si / 0-No): ")
                if respuesta == '0':
                    print("El total de la venta fue de: ",venta_total)
                    dict_total_venta[llave]=venta_total
                    venta_total = 0
                    break

    elif opcion == '2':
        llave = input("\nDime el identificador de la venta que deseas consultar: ")
        if llave in diccionario_ventas:
            print("la venta con esa llave es: ",llave)
            columnas = ["Descripción","Cantidad","Precio venta","Precio total"]
            for columna in range(4):
                print(columnas[columna],'\t',end="")
            print("\n")
            for articulo in diccionario_ventas[llave]:
                for i in range(4):
                    print(articulo[i],"\t\t",end="")
                print("\n")
            print(f'El precio total de la venta es: {dict_total_venta[llave]}') 

        else:
            print("\nLo siento, ese identificador no fue capturado")
    elif opcion == '3':
        break
    else: 
        print("Has introducido una opcion invalida") 