import math
import pandas as pd


def contador_tipos(datos):
    # Crear un DataFrame para las columnas que contienen solo 0 y 1
    variables_binarias = datos.loc[:, (datos.nunique() == 2) & (
        datos.max() == 1) & (datos.min() == 0)]
    # Eliminar las columnas de 0 y 1 del DataFrame original
    datos = datos.drop(columns=variables_binarias.columns)

    # Crear dos DataFrames separados para enteros y decimales
    variables_cuantitativas = datos.select_dtypes(include='int64')
    variables_cualitativas = datos.select_dtypes(include='float64')

    return variables_binarias.values.tolist(), variables_cuantitativas.values.tolist(), variables_cualitativas.values.tolist()


def distancias_variables_mixta(binarias, cuantitativas, cualitativas):
    G = g(cualitativas)
    p1 = len(cuantitativas[0])
    p2 = len(binarias[0])
    p3 = len(cualitativas[0])
    print(f"G = {G}")
    print(f"p1 = {p1}, p2 = {p2}, p3 = {p3}")

    for i in range(len(binarias)):
        for j in range(i+1, len(binarias)):

            print(f"\nCombinacion ({i+1},{j+1})")
            fila_uno_binarias = binarias[i]
            fila_dos_binarias = binarias[j]
            a, d = factor_a_d(fila_uno_binarias, fila_dos_binarias)

            print(f"a = {a}, d = {d}")

            fila_uno_cuantitativas = cuantitativas[i]
            fila_dos_cuantitativas = cuantitativas[j]
            alpha = coincidencia(fila_uno_cuantitativas,
                                 fila_dos_cuantitativas)
            print(f"alpha = {alpha}")

            fila_uno_cualitativas = cualitativas[i]
            fila_dos_cualitativas = cualitativas[j]
            s = similaridad(fila_uno_cualitativas,
                            fila_dos_cualitativas, G, p1, p2, p3, d, a, alpha)
            print(f"S({i+1},{j+1}) = {s}")

            d_2 = distancia_gower(s)
            print(f"D({i+1},{j+1})^2 = {d_2}")

            d = round(math.sqrt(d_2), 3)
            print(f"D({i+1},{j+1}) = {d}")


def g(cualitativas):
    # Obtener el número de columnas
    num_columnas = len(cualitativas[0])
    # Inicializar listas para almacenar los máximos y mínimos de cada columna
    maximos = [float('-inf')] * num_columnas
    minimos = [float('inf')] * num_columnas
    # Encontrar el máximo y mínimo de cada columna
    for fila in cualitativas:
        for i, valor in enumerate(fila):
            if valor > maximos[i]:
                maximos[i] = valor
            if valor < minimos[i]:
                minimos[i] = valor
    # Calcular la diferencia entre el máximo y el mínimo de cada columna y guardarla en una lista
    G = [round(maximos[i] - minimos[i], 2) for i in range(num_columnas)]
    return G

# Paso 3


def factor_a_d(fila_uno, fila_dos):
    a = 0
    d = 0

    if all(x == 1 for x in fila_uno):
        a += 1
    if all(x == 1 for x in fila_dos):
        a += 1
    if all(x == 0 for x in fila_uno):
        d += 1
    if all(x == 0 for x in fila_dos):
        d += 1

    return a, d

# Paso 4


def coincidencia(fila_uno, fila_dos):
    alpha = 0
    if all(valor == fila_uno[0] for valor in fila_uno):
        alpha += 1
    if all(valor == fila_dos[0] for valor in fila_dos):
        alpha += 1
    return alpha

# Paso 5


def similaridad(fila_uno, fila_dos, G, p1, p2, p3, d, a, alpha):
    valores = []
    for i in range(len(fila_uno)):
        valor = 1 - (abs(fila_uno[i] - fila_dos[i]) / G[i])
        valores.append(valor)
    numerador = sum(valores) + alpha + a
    denominador = p1 + (p2-d) + p3
    return numerador/denominador


def distancia_gower(s):
    return round(1-s, 3)


def mostra_array(datos):
    for dato in datos:
        print(dato)
    print("\n")
