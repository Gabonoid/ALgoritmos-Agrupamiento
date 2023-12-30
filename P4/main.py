import lectura

datos = lectura.leer_archivo(r"C:\Users\Lapnoid\OneDrive - Universidad Autónoma del Estado de México\UAEM\9no Semestre\Agrupamiento\Algoritmos\Algoritmo4\data\euclidea.csv")
tipo_algoritmo = lectura.tipo_algoritmo(datos)

# Seleccionar el algoritmo
if tipo_algoritmo == "FACTORES":
    from Factores.dicotomicas import *

    print("Se usará el algoritmo de factores\n")
    datos = datos.values.tolist()
    imprimir_lista(datos)

    a, b, c, d = distancia_dicotomica(datos)

    print("\nRelaciones")
    relaciones = calc_relacion(a, b, c, d)
    imprimir_lista(relaciones)
    
    print('\n¿Qué tipo de distancia desea calcular?')
    salida = int(input('1. Distancias Sockal\n2. Distancias Jaccard\n3. Ambas\n'))
    if salida == 1:
        print("\nDistancias Sockal")
        distancias = sockal(relaciones)
        imprimir_lista(distancias)
    elif salida == 2:
        print("\nDistancias Jaccard")
        distancias = jaccard(relaciones)
        imprimir_lista(distancias)
    elif salida == 3:
        print("\nDistancias Sockal")
        distancias = sockal(relaciones)
        imprimir_lista(distancias)
        print("\nDistancias Jaccard")
        distancias = jaccard(relaciones)
        imprimir_lista(distancias)

elif tipo_algoritmo == "EUCLIDEA":
    print("Se usará el algoritmo de euclidea (Eslabonamiento)")
    from Euclidea.eslabonamiento import *
    datos = datos.values.tolist()

    # Generando la tabla de puntuaciones z
    tabla_z = puntuacion_z(datos)

    # Generamos diccionario de combinaciones
    diccionario = diccionario_distancias(tabla_z)

    # Generamos la matriz de eslabonamiento
    tamanio_matriz = len(tabla_z)
    print('\n¿Qué tipo de eslabonamiento desea calcular?')
    salida = int(input('1. Minimo\n2. Maximo\n3. Promedio\n'))
    if salida == 1:
        tipo = MIN
    elif salida == 2:
        tipo = MAX
    elif salida == 3:
        tipo = MID
    Distancia.eslabonamiento(diccionario, tamanio_matriz, tipo)

    # Graficamos el dendrograma
    graficar_dendrograma(data=datos, tipo=tipo)

elif tipo_algoritmo == "GOWER":
    from Gower.algoritmo import *
    print("Se usará el algoritmo de Gower")
    
    binarias, cuantitativas, cualitativas = contador_tipos(datos)
    print('Binarias: ')
    mostra_array(binarias)
    print('Cuantitativas: ')
    mostra_array(cuantitativas)
    print('Cualitativas: ')
    mostra_array(cualitativas)
    distancias_variables_mixta(binarias, cuantitativas, cualitativas)